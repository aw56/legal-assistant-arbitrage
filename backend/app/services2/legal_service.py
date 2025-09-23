from sqlalchemy.orm import Session
from app.models2 import LegalOpinion2
from app.schemas2.legal_opinion2 import LegalOpinionSchema2
from app.schemas.client_request import ClientRequest


def analyze_with_db(db: Session, request: ClientRequest) -> LegalOpinionSchema2:
    # создаем запись в БД
    opinion = LegalOpinion2(
        client_name=request.client_name,
        dispute_summary=request.dispute_summary,
        stage=request.stage,
        region=request.region,
        goals=request.goals,  # сохраняем список напрямую
        amount=request.amount,
    )
    db.add(opinion)
    db.commit()
    db.refresh(opinion)

    # Pydantic v2 метод
    return LegalOpinionSchema2.model_validate(opinion)
