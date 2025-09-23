from pydantic import BaseModel, ConfigDict


class LegalOpinionSchema2(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # важно для model_validate
    client_name: str
    dispute_summary: str
    stage: str
    region: str
    goals: list[str]
    amount: float
