from pydantic import BaseModel
from typing import List

class LegalAnalysis(BaseModel):
    client_name: str
    dispute_summary: str
    stage: str
    region: str
    goals: List[str]
    amount: float
    key_statutes: List[str]
    related_cases: List[str]
    priority_notes: str
    conflict_detected: bool
