from sqlalchemy.orm import Session

from app.models import Post
from app.schemas import PostCreate, PostUpdate


def create_post(db: Session, post: PostCreate):
    db_post = Post(
        title=post.title,
        content=post.content,
        author=post.author
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post


def get_posts(db: Session):
    return db.query(Post).all()


def get_post_by_id(db:Session,post_id:int):
    return db.query(Post).filter(Post.id ==post_id).first()


def update_post(db: Session, post_id: int, post_data: PostUpdate):
    post = db.query(Post).filter(Post.id == post_id).first()

    if post is None:
        return None

    post.title = post_data.title
    post.content = post_data.content
    post.author = post_data.author

    db.commit()
    db.refresh(post)

    return post


def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if post is None:
        return None

    db.delete(post)
    db.commit()

    return post