from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str
    author: str


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author: str

    class Config:
        from_attributes = True