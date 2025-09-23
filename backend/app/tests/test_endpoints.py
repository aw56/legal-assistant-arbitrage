# backend/app/tests/test_endpoints.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.main import app
from backend.app.database import get_db
from backend.app.models2 import Base, Decision, Statute, CourtDecision
from backend.app.schemas.client_request import ClientRequest

# -----------------------------
# Настройка тестовой БД SQLite
# -----------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # in-memory для тестов
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# -----------------------------
# Фикстура для базы данных
# -----------------------------
@pytest.fixture(scope="function")
def db_session():
    session = TestingSessionLocal()

    # Предзагрузка тестовых данных
    session.add(Statute(code="ГК РФ", article="ст. 395", content="Проценты за пользование чужими денежными средствами"))
    session.add(CourtDecision(case_number="А40-12345/2023", summary="Нарушение сроков поставки", region="Москва", amount=850000))
    session.commit()

    try:
        yield session
    finally:
        session.close()

# -----------------------------
# Переопределяем зависимость get_db
# -----------------------------
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# -----------------------------
# Тест GET /
# -----------------------------
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Legal Assistant API is running"}

# -----------------------------
# Тест POST /analyze/
# -----------------------------
def test_analyze_post(db_session):
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
    assert isinstance(data["priority_notes"], str)

# -----------------------------
# Тест GET /decisions/
# -----------------------------
def test_decisions_get(db_session):
    response = client.get("/decisions/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

# -----------------------------
# Тест POST /decisions/
# -----------------------------
def test_decisions_post(db_session):
    payload = {
        "case_number": "А40-54321/2025",
        "court": "Арбитражный суд г. Москва",
        "date": "2025-09-16",
        "summary": "Задержка оплаты по договору"
    }

    response = client.post("/decisions/", json=payload)
    assert response.status_code == 200

    # Проверяем, что решение сохранилось
    get_resp = client.get("/decisions/")
    assert any(d["case_number"] == "А40-54321/2025" for d in get_resp.json())
