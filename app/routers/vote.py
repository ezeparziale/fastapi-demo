from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import CurrentUser
from app.models import Post, Vote
from app.schemas import Vote as VoteSchema

router = APIRouter(prefix="/votes", tags=["Vote"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(
    vote: VoteSchema,
    db: Session = Depends(get_db),
    current_user: CurrentUser = None,  # type: ignore
) -> Any:
    """
    ### Vote a post
    """
    stmt_select = select(Post).where(Post.id == vote.post_id)
    post = db.execute(stmt_select).scalars().first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {vote.post_id} does not exist",
        )

    stmt_select_vote = select(Vote).where(
        Vote.post_id == vote.post_id, Vote.user_id == current_user.id
    )

    found_vote = db.execute(stmt_select_vote).scalars().first()

    if vote.dir == 1:
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"user {current_user.id} has already voted on post {vote.post_id}",  # noqa: E501
            )
        new_vote = Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist"
            )

        stmt_delete_vote = (
            delete(Vote)
            .where(Vote.post_id == vote.post_id, Vote.user_id == current_user.id)
            .execution_options(synchronize_session=False)
        )
        db.execute(stmt_delete_vote)
        db.commit()
        return {"message": "successfully deleted vote"}
