from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.oauth import create_access_token
from app.schemas import Token
from app.utils import verify_password

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
async def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> Any:
    """
    ### Login user
    """
    user = db.query(User).filter(User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    if not verify_password(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    access_token = create_access_token(data={"id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
