from sqlalchemy.orm import Session

from app.models import Post
from app.schemas import PostCreate


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



