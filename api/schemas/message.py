from pydantic import BaseModel, Field


class IncrementLike(BaseModel):
    id: int


class MessageBase(BaseModel):
    user: str | None = Field(None, description='ユーザー名')
    text: str = Field('', description='メッセージ')


class MessageAdd(MessageBase):
    pass


class MessageAddResponse(MessageAdd):
    id: int

    class Config:
        orm_mode = True


class Message(MessageBase):
    id: int
    like: int = Field(0, description='いいねの数')

    class Config:
        orm_mode = True
