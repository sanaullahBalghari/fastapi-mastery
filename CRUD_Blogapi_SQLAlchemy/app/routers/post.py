from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import PostCreate, PostResponse
from app.crud.post import create_post ,get_posts ,get_post_by_id

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=PostResponse)
def create(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post)


@router.get("/", response_model=list[PostResponse])
def read_posts(db: Session = Depends(get_db)):
    return get_posts(db)


@router.get("/{post_id}", response_model=PostResponse)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = get_post_by_id(db, post_id)

    if post is None:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    return post