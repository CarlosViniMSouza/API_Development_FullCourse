from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy import func

from .. import models, schemas, oauth2
from .. database import get_db


router = APIRouter(prefix="/posts", tags=['Posts'])


@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),
              current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):

    posts = db.query(models.Post, func.count(models.Vote.post_id))\
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)\
        .group_by(models.Post.id)\
        .filter(models.Post.title.contains(search))\
        .limit(limit)\
        .offset(skip)\
        .all()

    return posts


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int,
             db: Session = Depends(get_db),
             current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post, func.count(models.Vote.post_id)\
                    .label("votes"))\
                    .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)\
                    .group_by(models.Post.id)\
                    .filter(models.Post.id == id)\
                    .first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return post



