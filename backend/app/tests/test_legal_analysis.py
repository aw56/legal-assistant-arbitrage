# backend/app/tests/test_legal_analysis.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.main import app
from backend.app.database import get_db
from backend.app.models2 import Base, Statute, CourtDecision
from backend.app.schemas.client_request import ClientRequest

# -----------------------------
# Настройка тестовой БД SQLite
# -----------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# -----------------------------
# Фикстура для базы данных
# -----------------------------
@pytest.fixture(scope="function")
def db_session():
    session = TestingSessionLocal()

    # Загружаем несколько норм и судебных решений для тестов
    session.add_all([
        Statute(code="ГК РФ", article="ст. 309", content="Исполнение обязательств"),
        Statute(code="ГК РФ", article="ст. 395", content="Проценты за пользование чужими денежными средствами"),
        Statute(code="ФЗ №230", article="ст. 15", content="Обеспечение исполнения решений суда")
    ])
    session.add_all([
        CourtDecision(case_number="А40-12345/2023", summary="Нарушение сроков поставки", region="Москва", amount=850000),
        CourtDecision(case_number="А40-67890/2024", summary="Неустойка за просрочку", region="Санкт-Петербург", amount=500000)
    ])
    session.commit()

    try:
        yield session
    finally:
        session.close()

# -----------------------------
# Переопределяем get_db
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
# Тест POST /analyze/ с коллизиями
# -----------------------------
@pytest.mark.parametrize(
    "request_data",
    [
        {
            "client_name": "ООО А",
            "dispute_summary": "Просрочка поставки и неоплата",
            "stage": "первая инстанция",
            "region": "Москва",
            "goals": ["взыскание неустойки", "исполнение обязательств"],
            "amount": 850000.0
        },
        {
            "client_name": "ООО Б",
            "dispute_summary": "Задержка оплаты по договору аренды",
            "stage": "апелляция",
            "region": "Санкт-Петербург",
            "goals": ["взыскание процентов", "восстановление сроков"],
            "amount": 500000.0
        }
    ]
)
def test_analyze_with_multiple_norms(request_data):
    response = client.post("/analyze/", json=request_data)
    assert response.status_code == 200

    data = response.json()
    # Проверка структуры ответа
    assert data["client_name"] == request_data["client_name"]
    assert isinstance(data["key_statutes"], list)
    assert isinstance(data["related_cases"], list)
    assert isinstance(data["priority_notes"], str)
    assert isinstance(data["conflict_detected"], bool)
    # Проверка наличия хотя бы одной нормы
    assert len(data["key_statutes"]) >= 1
    # Проверка наличия хотя бы одного связанного дела
    assert len(data["related_cases"]) >= 1

