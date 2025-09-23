Отлично 🙌 Я добавлю раздел **✍️ Работа с документацией** в конец твоего `docs/PROJECT_DOC.md`. Вот обновлённый файл:

````markdown
# 📘 Legal Assistant API — Полная документация
Дата фиксации: 23 сентября 2025  
Автор: Aleksej  
Проект: Цифровой помощник юриста по арбитражным делам  
Формат: Автономная, масштабируемая backend-платформа с экспертной аналитикой, справочной системой и сервисным блоком  

---

## 🎯 Цель проекта
Создание цифрового юриста по арбитражным делам — платформы, объединяющей:  
- нормативную базу и судебную практику  
- экспертный правовой анализ  
- автоматическую генерацию документов  
- прогнозирование исхода спора  
- сервисы для клиента и юриста  
- маркетинговые инструменты для юридических компаний  

---

## 📚 Функциональные цели
1. Создание материальной и процессуальной базы арбитражных споров  
2. Регулярная актуализация правовой базы  
3. Стандартизированная форма клиентского запроса  
4. Правовой анализ запроса в иерархии норм  
5. Подсветка коллизий права и рекомендации  
6. Мотивированное решение с опорой на НПА  
7. Оценка вероятности успеха (% прогноз)  
8. Проверка субъективных предпосылок (правоспособность, представительство, онлайн-процесс)  
9. Типовые документы (иск, отзыв, жалоба)  
10. Автономность и локализация  
11. Калькулятор стоимости юридических услуг  
12. Маркетинговая стратегия юридической компании  

---

## 🧱 Архитектура проекта

```plaintext
legal-assistant-arbitrage/
├── backend/
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       ├── database.py
│       ├── init_db.py
│       ├── api/          # Эндпоинты FastAPI
│       │   └── decisions.py
│       ├── services/     # Логика анализа
│       ├── schemas/      # Pydantic-схемы
│       └── tests/        # Pytest-тесты
├── docker-compose.yml
├── requirements.txt
├── .env
├── pytest.ini
└── docs/
    └── PROJECT_DOC.md
````

---

## ⚙️ Установка окружения

```bash
git clone https://github.com/aw56/legal-assistant-arbitrage.git
cd legal-assistant-arbitrage

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Файл `.env`:

```env
DATABASE_URL=postgresql://admin:admin14092025@localhost:5432/legal_assistant_db
```

### 🗄️ PostgreSQL

**Запуск через Docker**

```bash
docker compose up -d db
```

**Проверка подключения**

```bash
docker exec -it legal-assistant-arbitrage-db-1 psql -U admin -d legal_assistant_db
```

**Инициализация таблиц**

```bash
python3 -m backend.app.init_db
```

Вывод:

```
Database tables created successfully!
```

---

## 🚀 Запуск приложения

**В разработке**

```bash
uvicorn backend.app.main:app --reload
```

Чтобы не блокировать терминал, можно использовать `nohup`, `screen` или `systemd`.

**В продакшене через systemd**

Файл `/etc/systemd/system/fastapi.service`:

```ini
[Unit]
Description=FastAPI app
After=network.target

[Service]
User=admin
Group=admin
WorkingDirectory=/home/admin/my_projects/legal-assistant-arbitrage
Environment="DATABASE_URL=postgresql://admin:admin14092025@localhost:5432/legal_assistant_db"
ExecStart=/home/admin/my_projects/legal-assistant-arbitrage/venv/bin/uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

---

## 🧪 Тестирование

Файл `pytest.ini`:

```ini
[pytest]
pythonpath = backend
testpaths = backend/app/tests
```

Запуск:

```bash
pytest -v backend/app/tests
```

---

## 🤖 CI/CD (GitHub Actions)

Файл `.github/workflows/backend.yml`:

```yaml
name: Backend CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: "3.12"
    - run: python -m pip install --upgrade pip
    - run: pip install -r requirements.txt
    - run: pytest -v backend/app/tests
```

---

## ⚠️ FAQ: типовые ошибки

* ❌ `could not translate host name "db"` → заменить на `localhost` или запустить контейнер
* ❌ `Address already in use` → освободить порт: `sudo pkill -f uvicorn`
* ❌ `database "admin" does not exist` → создать БД:

  ```bash
  psql -U admin -h localhost -c "CREATE DATABASE legal_assistant_db;"
  ```

---

## 📌 Текущее состояние

* ✅ PostgreSQL настроен (5432/5433)
* ✅ Таблица `decisions` создана
* ✅ FastAPI-приложение запущено через systemd
* ✅ Swagger UI доступен (/docs)
* ⚠️ Внешний доступ требует настройки UFW/nginx

---

## 🔜 Следующие шаги

* [ ] Добавить `POST /decisions` (Pydantic-схема)
* [ ] Вынести конфигурацию в `.env`
* [ ] Настроить nginx + HTTPS
* [ ] Подготовить Docker-контейнер и CI/CD
* [ ] Реализовать модули анализа, прогнозирования и генерации документов
* [ ] Расширить БД: `statute`, `article`, `court_decision`, `plenum_resolution`, `client_request`, `legal_opinion`, `document_template`

---

## ✍️ Работа с документацией

Для удобства фиксации изменений документации используется `Makefile`.

### Установка

В корне проекта (`~/my_projects/legal-assistant-arbitrage`) создайте файл `Makefile` со следующим содержимым:

```makefile
# Makefile для упрощённой работы с документацией

# Основная ветка
BRANCH = main

# Цель "docs" — автоматизация коммита документации
docs:
	# Подтягиваем свежие изменения из GitHub (чтобы не было конфликтов)
	git pull origin $(BRANCH)

	# Добавляем все изменения в папке docs/
	git add docs/

	# Делаем коммит с фиксированным сообщением
	git commit -m "docs: обновлена документация (PROJECT_DOC.md)"

	# Отправляем изменения в GitHub
	git push origin $(BRANCH)
```

### Использование

После изменения `docs/PROJECT_DOC.md` или других файлов документации выполните:

```bash
make docs
```

Эта команда автоматически:

1. Подтянет свежие изменения (`git pull origin main`)
2. Добавит изменённые файлы документации (`git add docs/`)
3. Сделает коммит с сообщением по умолчанию
4. Отправит изменения на GitHub (`git push origin main`)

### Кастомные сообщения коммита

Можно расширить `Makefile`, чтобы передавать своё сообщение:

```makefile
docs:
	git pull origin $(BRANCH)
	git add docs/
	git commit -m "$(MSG)"
	git push origin $(BRANCH)
```

И запускать так:

```bash
make docs MSG="docs: добавлен раздел о тестировании"
```

Таким образом, документация всегда будет обновляться централизованно и консистентно.

```

---

Хочешь, я сразу подготовлю тебе команду, чтобы перезаписать `docs/PROJECT_DOC.md` новым содержимым и закоммитить его?
```
