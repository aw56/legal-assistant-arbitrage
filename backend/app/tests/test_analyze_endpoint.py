# backend/app/tests/test_analyze_endpoint.py
import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.models2 import Base

# Настраиваем тестовую БД SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Переопределяем зависимость get_db
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_analyze_post():
    payload = {
        "client_name": "ООО Тест",
        "dispute_summary": "Просрочка поставки",
        "stage": "первая инстанция",
        "region": "Москва",
        "goals": ["взыскание неустойки"],
        "amount": 850000.0
    }

    response = client.post("/analyze/", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["client_name"] == payload["client_name"]
    assert data["dispute_summary"] == payload["dispute_summary"]
    assert "key_statutes" in data
    assert "related_cases" in data
    assert isinstance(data["conflict_detected"], bool)
