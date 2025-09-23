# Развёртывание Legal Assistant API

## 1. Установка зависимостей
- Python 3.10+
- PostgreSQL
- FastAPI, SQLAlchemy, Uvicorn

## 2. Настройка базы данных
- Создание базы
- Установка пароля
- Переменная DATABASE_URL

## 3. Инициализация таблиц
- `init_db.py`

## 4. Запуск приложения
- `uvicorn main:app --host 0.0.0.0 --port 8000`

## 5. Автозапуск через systemd
- Юнит-файл
- Команды `systemctl`

## 6. CI/CD через GitHub Actions
- Пример workflow
- Проверка зависимостей и тестов

## 7. Docker (опционально)
- `docker-compose.yml`
- Сборка и запуск контейнеров
