from pydantic import BaseModel


class StatuteSchema(BaseModel):
    id: int
    code: str
    article: str
    content: str

    class Config:
        orm_mode = True
