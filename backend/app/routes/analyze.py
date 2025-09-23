# backend/app/routes/analyze.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.models2 import Base, ClientRequestModel, LegalOpinionModel
from backend.app.schemas.client_request import ClientRequest
from backend.app.schemas.legal_opinion import LegalAnalysis
from backend.app.database import get_db

router = APIRouter(prefix="/analyze", tags=["Analyze"])

@router.post("/", response_model=LegalAnalysis)
def analyze_request(request: ClientRequest, db: Session = Depends(get_db)):
    # Сохраняем запрос клиента
    db_request = ClientRequestModel(
        client_name=request.client_name,
        dispute_summary=request.dispute_summary,
        stage=request.stage,
        region=request.region,
        goals=";".join(request.goals),
        amount=request.amount
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)

    # Здесь логика анализа (пока заглушка)
    analysis = LegalAnalysis(
        client_name=request.client_name,
        dispute_summary=request.dispute_summary,
        stage=request.stage,
        region=request.region,
        goals=request.goals,
        amount=request.amount,
        key_statutes=["ГК РФ ст. 395"],
        related_cases=["А40-12345/2023"],
        priority_notes="Проверить соответствие сумм требованиям закона",
        conflict_detected=False
    )

    # Сохраняем юридическое заключение
    db_opinion = LegalOpinionModel(
        client_name=analysis.client_name,
        dispute_summary=analysis.dispute_summary,
        stage=analysis.stage,
        region=analysis.region,
        goals=";".join(analysis.goals),
        amount=analysis.amount,
        key_statutes=";".join(analysis.key_statutes),
        related_cases=";".join(analysis.related_cases),
        priority_notes=analysis.priority_notes,
        conflict_detected=str(analysis.conflict_detected)
    )
    db.add(db_opinion)
    db.commit()
    db.refresh(db_opinion)

    return analysis
