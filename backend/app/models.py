from sqlalchemy import Column, Integer, String
from backend.app.database import Base

class Decision(Base):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True, index=True)
    case_number = Column(String, unique=True, nullable=False)
    court = Column(String, nullable=False)
    date = Column(String, nullable=False)
    summary = Column(String, nullable=False)
