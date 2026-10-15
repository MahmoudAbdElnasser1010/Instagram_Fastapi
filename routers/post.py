from fastapi import APIRouter, HTTPException, Depends, status, UploadFile, File
from sqlalchemy.orm.session import Session

from authentication.oauth2 import get_current_user
from db.database import get_db
from routers.schemas import PostBase, PostDisplay, UserAuth
from db import post
from typing import List
import string
import random
import shutil

router = APIRouter(
    prefix="/post",
    tags=["post"],
)

image_url_types = ['absolute', 'relative']

@router.post('/new', response_model=PostDisplay)
def create(request: PostBase, db:Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                            detail='Image type is not supported')
    return post.create(db, request, current_user.id)

@router.get('/all', response_model=List[PostDisplay])
def get_all(db:Session = Depends(get_db)):
    return post.get_all_posts(db)



@router.post('/image')
def upload_image(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, "wb+") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}

@router.delete('/delete/{id}')
def delete(id: int, db:Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return post.delete_post(db, id, current_user.id)
