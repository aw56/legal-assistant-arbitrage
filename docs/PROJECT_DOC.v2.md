Отлично 🚀
Я собрал для тебя **финальный `docs/PROJECT_DOC.md`**. В нём теперь встроены:

* ASCII-схема модулей (в разделе Архитектура).
* Mermaid-диаграмма архитектуры.
* Mermaid workflow бэкапа/рестора.
* Все предыдущие разделы (Git Workflow, Disaster Recovery Checklist, Plesk и т.д.).

---

```markdown
# 📘 Legal Assistant API — Полная документация

Дата фиксации: 25 сентября 2025  
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

## 🧱 Архитектура проекта (по модулям)

### 🔹 1. Нормативная и процессуальная база
- База данных законов, кодексов, постановлений Пленума, судебной практики
- Источники: pravo.gov.ru, vsrf.ru, арбитражные суды, Консультант/Гарант
- Хранение редакций, связей: «норма ↔ практика ↔ разъяснение»
- Автоматизация: парсинг через RSS/API/скрипты

### 🔹 2. Актуализация базы
- Фоновый сервис обновлений
- Журнал изменений
- Указание действующей редакции на дату спора

### 🔹 3. Стандартизированная форма клиентского запроса
- Веб-форма или Telegram-бот
- Структура: данные клиента, суть спора, стадия, цели, сроки, регион

### 🔹 4. Правовой анализ проблемы
- Выделение ключевых норм
- Поиск аналогичной практики
- Иерархия: Конституция → кодекс → спец. закон → практика → локальные акты

### 🔹 5. Подсветка коллизий права
- Сравнение норм
- Приоритеты и рекомендации по разрешению

### 🔹 6. Мотивированное решение
- Юридическое заключение: ввод, ссылки на нормы, практика, вывод

### 🔹 7. Вероятность успеха
- NLP-модель на корпусе решений
- Классификация: положительное/отрицательное
- Учет суда, региона, суммы
- Выход: «65% положительное решение»

### 🔹 8. Субъективные предпосылки
- Проверка правоспособности
- Представительство
- Возможность удалённого участия

### 🔹 9. Типовые документы
- Шаблоны: иск, отзыв, ходатайство, жалоба
- Автогенерация с реквизитами
- Форматы: DOCX/PDF

### 🔹 10. Автономность и локализация
- Работа офлайн
- Синхронизация обновлений
- Локализация под российскую юрисдикцию

### 🔹 11. Калькулятор стоимости услуг
- Среднерыночные тарифы
- Коэффициенты: регион, сложность, стадия
- Диапазон: «от 80 000 до 120 000 руб.»

### 🔹 12. Маркетинговая стратегия
- Позиционирование: цифровой юрист
- Каналы: SEO, реклама, Telegram
- УТП: скорость, документы, прогноз
- Контент: кейсы, цифры, ссылки на практику

---

### 📊 ASCII-схема архитектуры

```

[ Клиент ] → [ API Gateway / FastAPI ]
↓
┌───────────────┐
│  Аналитика    │
│  NLP-модуль   │
└───────────────┘
↓
[ PostgreSQL база ]
↓
[ Обновление базы норм ]
↓
[ Генерация документов / PDF ]

````

---

### 🖼 Mermaid-диаграмма архитектуры

```mermaid
graph TD
    A[Клиент: Web/Telegram] --> B[FastAPI Backend]
    B --> C[PostgreSQL]
    B --> D[NLP Аналитика]
    B --> E[Генерация документов]
    C --> F[База норм и практики]
    F --> B
    D --> B
    E --> A
````

---

## ⚙️ Техническая реализация

### 📁 Структура проекта

```

my_projects/
├── etc
│   ├── letsencrypt
│   │   ├── cli.ini
│   │   ├── options-ssl-nginx.conf
│   │   ├── renewal
│   │   │   └── a-quilon.com.conf
│   │   ├── renewal-hooks
│   │   │   ├── deploy
│   │   │   ├── post
│   │   │   └── pre
│   │   └── ssl-dhparams.pem
│   ├── nginx
│   │   └── sites-available
│   │       └── legal-assistant
│   └── systemd
│       └── system
│           └── fastapi.service
├── home
│   └── admin
│       └── my_projects
│           └── legal-assistant-arbitrage
├── legal-assistant-arbitrage
│   ├── Makefile
│   ├── README.md
│   ├── backend
│   │   └── app
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       ├── database.py
│   │       ├── db.py
│   │       ├── init_db.py
│   │       ├── legal_opinion.py
│   │       ├── main.py
│   │       ├── main.py.bak
│   │       ├── models.py
│   │       ├── models2.py
│   │       ├── models2.py.bak
│   │       ├── parser.py
│   │       ├── routes/
│   │       ├── routes2/
│   │       ├── schemas/
│   │       ├── schemas2/
│   │       ├── services/
│   │       ├── services2/
│   │       ├── tests/
│   │       ├── tests2/
│   │       └── utils/
│   ├── backup_legal_assistant
│   │   ├── db_20250924_0728.sql
│   │   └── project_20250924_0728.tar.gz
│   ├── data
│   │   └── legal_assistant_mvp.json
│   ├── db
│   │   ├── import_to_postgres.py
│   │   └── schema.sql
│   ├── docker-compose.yml
│   ├── docs
│   │   ├── PROJECT_DOC.md
│   │   ├── api.md
│   │   ├── architecture.md
│   │   ├── contributing.md
│   │   ├── deployment.md
│   │   └── legal-model.md
│   ├── etc
│   │   ├── letsencrypt/
│   │   ├── nginx/
│   │   └── systemd/
│   ├── fix_duplicates.sh
│   ├── fix_git.sh
│   ├── github
│   │   ├── ISSUE_TEMPLATE/
│   │   └── workflows/
│   ├── legal_opinion.py
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── uvicorn.log
│   └── venv
│       ├── bin/
│       ├── include/
│       └── lib/
└── tmp_restore
```

---

### 🧪 Установка окружения

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 🗄️ PostgreSQL

```bash
sudo -u postgres psql
CREATE DATABASE legal_assistant_db;
CREATE USER admin WITH PASSWORD 'admin14092025';
GRANT ALL PRIVILEGES ON DATABASE legal_assistant_db TO admin;
```

`.env`:

```
DATABASE_URL=postgresql://admin:admin14092025@localhost:5432/legal_assistant_db
```

---

### 🚀 Запуск FastAPI

```bash
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
```

---

### 🧭 Автозапуск через systemd

```ini
[Unit]
Description=FastAPI app
After=network.target

[Service]
User=admin
WorkingDirectory=/home/admin/my_projects/legal-assistant-arbitrage/backend/app
Environment="PATH=/home/admin/my_projects/legal-assistant-arbitrage/venv/bin"
ExecStart=/home/admin/my_projects/legal-assistant-arbitrage/venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 📑 Backup & Restore Guide

### 📦 backup.sh

```bash
#!/bin/bash
set -euo pipefail

PROJECT_DIR="/home/admin/my_projects/legal-assistant-arbitrage"
BACKUP_DIR="/root/legal-assistant-arbitrage/backup_legal_assistant"
DATE=$(date +%Y%m%d_%H%M)

mkdir -p "$BACKUP_DIR"

tar -czf "$BACKUP_DIR/project_${DATE}.tar.gz" \
  -C "$PROJECT_DIR" \
  backend/app requirements.txt .env .git

pg_dump -U legal_admin legal_assistant_db > "$BACKUP_DIR/db_${DATE}.sql"

echo "✅ Backup complete"
```

---

### 🔄 restore_all.sh v35

```bash
#!/bin/bash
set -euo pipefail

PROJECT_DIR="/home/admin/my_projects/legal-assistant-arbitrage"
BACKUP_PROJECT="$1"
BACKUP_DB="$2"

systemctl stop fastapi || true
rm -rf "$PROJECT_DIR"
mkdir -p "$PROJECT_DIR"

TMPDIR=$(mktemp -d)
tar -xzf "$BACKUP_PROJECT" -C "$TMPDIR"

APP_PATH=$(find "$TMPDIR" -type d -path "*/backend/app" | head -n1)
mkdir -p "$PROJECT_DIR/backend"
cp -r "$APP_PATH" "$PROJECT_DIR/backend/app"

find "$TMPDIR" -name ".env" -exec cp {} "$PROJECT_DIR/" \; || true
find "$TMPDIR" -name "requirements.txt" -exec cp {} "$PROJECT_DIR/" \; || true
find "$TMPDIR" -name ".git" -exec cp -r {} "$PROJECT_DIR/.git" \; || true

psql -U legal_admin -d legal_assistant_db < "$BACKUP_DB" || true
```

---

### 🖼 Mermaid Workflow: Backup & Restore

```mermaid
flowchart LR
    A[Run backup.sh] --> B[Create project archive]
    B --> C[Dump PostgreSQL DB]
    C --> D[Copy to backup dir]
    D --> E[Transfer to new server]
    E --> F[Run restore_all.sh]
    F --> G[Unpack project + .env + .git]
    G --> H[Restore DB]
    H --> I[Setup venv + FastAPI + Nginx]
    I --> J[App running at https://a-quilon.com/docs]
```

---

## 🛠 Troubleshooting FastAPI

* **`ModuleNotFoundError: No module named 'backend'`** → запустить `fix_structure.sh`.
* **`sqlalchemy not found`** → `pip install -r requirements.txt`.
* **`OSError: [Errno 98] Address already in use`** → `sudo lsof -i:8000 && kill -9 <PID>`.

---

## 🚨 Disaster Recovery Checklist

1. Установить пакеты: `apt-get install python3 postgresql nginx certbot`.
2. Скопировать архивы `project_*.tar.gz` и `db_*.sql`.
3. Выполнить `restore_all.sh`.
4. Проверить FastAPI: `systemctl status fastapi`.
5. Проверить HTTPS: `https://a-quilon.com/docs`.

---

## 🌱 Git Workflow

```bash
git status
git add .
git commit -m "Update"
git pull origin main --rebase
git push origin main
```

---

## 👤 Работа с пользователем admin на Plesk

* Смена пароля:

```bash
plesk bin admin --set-password -passwd "NEW_SECURE_PASS"
```

* Добавление sudo:

```bash
usermod -aG sudo admin
```

* SSH без пароля:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo "PUB_KEY" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

---

```

---

Хочешь, я ещё добавлю **Mermaid sequenceDiagram**, показывающий цепочку действий при входе клиента (клиент → API → БД → ответ), чтобы завершить документ наглядным юзкейсом?
```
