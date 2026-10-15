import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.models import Post, Comment
from routers.schemas import CommentBase


def create(db: Session, request: CommentBase, username: str):
    post = db.query(Post).filter(Post.id == request.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {request.post_id} not found")
    new_comment = Comment(
        text = request.text,
        username = username,
        post_id = request.post_id,
        timestamp = datetime.datetime.now(),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(db:Session, post_id:int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()
