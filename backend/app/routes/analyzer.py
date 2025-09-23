from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.client_request import ClientRequest
from app.schemas.legal_opinion import LegalAnalysis
from app.services.analyzer import analyze_request
from app.database import get_db

router = APIRouter(prefix="/analyze", tags=["analyze"])

@router.post("/", response_model=LegalAnalysis)
def analyze_client_request(request: ClientRequest, db: Session = Depends(get_db)):
    """
    Эндпоинт для анализа клиентского запроса.
    Возвращает ключевые нормы, связанные дела и рекомендации.
    """
    # Передаем запрос в модуль анализа
    analysis_result = analyze_request(request, db=db)
    return analysis_result
