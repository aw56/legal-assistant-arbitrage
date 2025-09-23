import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.database import Base, engine, SessionLocal
from backend.app.models import Decision

# Клиент для тестов
client = TestClient(app)

# Фикстура для чистой базы перед каждым тестом
@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_create_and_get_decision():
    # 1️⃣ Создаём решение через POST
    response = client.post(
        "/decisions/",
        json={
            "case_number": "А40-12345/2023",
            "court": "Арбитражный суд Москвы",
            "date": "2023-09-01",
            "summary": "Просрочка поставки"
        }
    )
    assert response.status_code == 200
    created = response.json()
    assert created["id"] > 0
    assert created["case_number"] == "А40-12345/2023"

    # 2️⃣ Получаем список решений (GET /decisions)
    response = client.get("/decisions/")
    assert response.status_code == 200
    decisions = response.json()
    assert len(decisions) == 1
    assert decisions[0]["summary"] == "Просрочка поставки"

    # 3️⃣ Получаем по ID (GET /decisions/{id})
    decision_id = created["id"]
    response = client.get(f"/decisions/{decision_id}")
    assert response.status_code == 200
    fetched = response.json()
    assert fetched["court"] == "Арбитражный суд Москвы"
