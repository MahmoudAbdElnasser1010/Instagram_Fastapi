from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from authentication.oauth2 import get_current_user
from db import comment

from db.database import get_db
from routers.schemas import CommentBase, UserAuth

router = APIRouter(
    prefix="/comment",
    tags=["comment"],
)

@router.get('/all/{post_id}')
def comments(post_id: int,db: Session =Depends(get_db)):
    return comment.get_all(db, post_id)

@router.post('')
def create(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return comment.create(db, request, current_user.username)
