import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models2 import Base, Statute, CourtDecision
from app.services2.legal_service import analyze_with_db
from app.schemas.client_request import ClientRequest


@pytest.fixture(scope="function")
def db_session():
    # Создаем SQLite in-memory для тестов
    engine = create_engine("sqlite:///:memory:", echo=False)
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()

    # Добавляем тестовые данные
    session.add(
        Statute(
            code="ГК РФ",
            article="ст. 395",
            content="Проценты за пользование чужими денежными средствами"
        )
    )
    session.add(
        CourtDecision(
            case_number="А40-12345/2023",
            summary="Нарушение сроков поставки",
            region="Москва",
            amount=850000
        )
    )
    session.commit()

    yield session
    session.close()


def test_analyze_with_db(db_session):
    request = ClientRequest(
        client_name="ООО 'Тест'",
        dispute_summary="Просрочка поставки",
        stage="первая инстанция",
        region="Москва",
        goals=["взыскание неустойки"],
        amount=850000
    )

    result = analyze_with_db(db_session, request)

    # Проверяем, что Pydantic корректно создал объект
    assert result.client_name == "ООО 'Тест'"
    assert result.dispute_summary == "Просрочка поставки"
    assert result.stage == "первая инстанция"
    assert result.region == "Москва"
    assert result.goals == ["взыскание неустойки"]
    assert result.amount == 850000
