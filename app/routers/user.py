from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import oauth2

from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_exist = db.query(models.User).filter(models.User.email == user.email).first()
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"User exists",
        )
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with: {id} does not exists",
        )
    return user

@router.get("/", response_model=list[schemas.UserOut])
def get_users(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
    limit: int = 10,
    skip: int = 0,
    search: str | None = "",
):
    users = (
        db.query(models.User)
        .filter(models.User.email.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )
    return users