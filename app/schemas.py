from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase): # will check if the data is valid
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True # 'orm_mode' has been renamed to 'from_attributes'

class Post(PostBase): # Controls response data
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True # 'orm_mode' has been renamed to 'from_attributes'

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True # 'orm_mode' has been renamed to 'from_attributes'

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: Optional[int] = None
    dir: conint(ge=0, le=1)

