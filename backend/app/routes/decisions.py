from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal
from backend.app.models import Decision
from pydantic import BaseModel

class DecisionCreate(BaseModel):
    case_number: str
    court: str
    date: str
    summary: str

router = APIRouter(
    prefix="/decisions",
    tags=["Decisions"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[dict])
def read_decisions(db: Session = Depends(get_db)):
    decisions = db.query(Decision).all()
    return [d.__dict__ for d in decisions]

@router.get("/{decision_id}", response_model=dict)
def read_decision(decision_id: int, db: Session = Depends(get_db)):
    decision = db.query(Decision).filter(Decision.id == decision_id).first()
    if not decision:
        raise HTTPException(status_code=404, detail="Decision not found")
    return decision.__dict__

@router.post("/", response_model=dict)
def create_decision(decision: DecisionCreate, db: Session = Depends(get_db)):
    db_decision = Decision(
        case_number=decision.case_number,
        court=decision.court,
        date=decision.date,
        summary=decision.summary
    )
    db.add(db_decision)
    db.commit()
    db.refresh(db_decision)
    return db_decision.__dict__
