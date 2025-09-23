from pydantic import BaseModel
from typing import Optional


class CourtDecisionSchema(BaseModel):
    id: int
    case_number: str
    summary: str
    region: Optional[str]
    amount: Optional[float]

    class Config:
        orm_mode = True
