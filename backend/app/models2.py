# backend/app/models2.py
from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ClientRequestModel(Base):
    __tablename__ = "client_requests"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    dispute_summary = Column(Text, nullable=False)
    stage = Column(String, nullable=False)
    region = Column(String, nullable=False)
    goals = Column(Text, nullable=False)  # будем хранить как ; разделённый список
    amount = Column(Float, nullable=False)

class LegalOpinionModel(Base):
    __tablename__ = "legal_opinions"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    dispute_summary = Column(Text, nullable=False)
    stage = Column(String, nullable=False)
    region = Column(String, nullable=False)
    goals = Column(Text, nullable=False)
    amount = Column(Float, nullable=False)
    key_statutes = Column(Text, nullable=True)
    related_cases = Column(Text, nullable=True)
    priority_notes = Column(Text, nullable=True)
    conflict_detected = Column(String, nullable=True)  # "True"/"False"
