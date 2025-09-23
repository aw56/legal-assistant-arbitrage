from pydantic import BaseModel
from typing import List

class ClientRequest(BaseModel):
    client_name: str
    dispute_summary: str
    stage: str
    region: str
    goals: List[str]
    amount: float
