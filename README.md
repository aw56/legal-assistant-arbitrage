# Legal Assistant Arbitrage

Проект: автоматизированный помощник юриста по арбитражным делам.

## Возможности
- база нормативных актов (материальное и процессуальное право)
- судебная практика
- анализ клиентских запросов
- правовые заключения с вероятностью успеха
- API (FastAPI) для интеграции
- калькулятор стоимости услуг

## Стек
- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic
- Docker Compose

## Быстрый старт
```bash
docker compose up -d
source venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
# Project documentation
