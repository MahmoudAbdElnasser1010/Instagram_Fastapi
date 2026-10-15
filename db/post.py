import datetime
from fastapi import HTTPException, status

from sqlalchemy.orm.session import Session
from db.models import Post
from routers.schemas import PostBase


def create(db: Session, request: PostBase, creator_id: int):
    new_post  = Post(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.datetime.now(),
        creator_id = creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts(db:Session):
    return db.query(Post).all()



def delete_post(db: Session, post_id: int, user_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
       raise HTTPException(status_code=404, detail="Post not found")
    if post.creator_id != user_id:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="Only creator of the post can delete the post")
    db.delete(post)
    db.commit()

    return 'ok'

