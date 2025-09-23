from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.client_request import ClientRequest
from app.schemas2.legal_opinion2 import LegalOpinionSchema2
from app.services2.legal_service import analyze_with_db

router = APIRouter(prefix="/legal-opinions2", tags=["Legal Opinions 2"])


@router.post("/", response_model=LegalOpinionSchema2)
def create_legal_opinion(request: ClientRequest, db: Session = Depends(get_db)):
    return analyze_with_db(db, request)
