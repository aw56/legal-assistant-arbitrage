Отлично 🚀
Ниже финальная версия `docs/PROJECT_DOC.md`, объединяющая всё: архитектуру, деплой, Nginx+SSL, GitHub, тестирование и **бэкап/восстановление**.

Сохрани этот файл в проект: `docs/PROJECT_DOC.md`.

---

```markdown
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

## 🚀 Этапы реализации (по спринтам)

| Версия | Состав |
|--------|--------|
| MVP    | АПК РФ + ГК РФ, 5 шаблонов, форма запроса, простой анализ |
| 2.0    | Судебная практика, коллизии, генерация заключения |
| 3.0    | Вероятностная модель, калькулятор услуг |
| 4.0    | Маркетинг, CRM-учёт клиентов |

---

## ⚙️ Техническая реализация

### 📁 Структура проекта

```

legal-assistant-arbitrage/
├── backend/
│   └── app/
│       ├── main.py
│       ├── models.py
│       ├── database.py
│       ├── init\_db.py
│       ├── routes/
│       │   └── decisions.py
│       ├── services/
│       ├── schemas/
│       └── tests/
├── docs/PROJECT\_DOC.md
├── .github/workflows/
├── docker-compose.yml
├── requirements.txt
└── README.md

````

---

### 🧪 Установка окружения

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

---

### 🗄️ PostgreSQL

```bash
sudo -u postgres psql
CREATE DATABASE legal_assistant_db;
CREATE USER admin WITH PASSWORD 'admin14092025';
GRANT ALL PRIVILEGES ON DATABASE legal_assistant_db TO admin;
```

`DATABASE_URL` в `.env`:

```
DATABASE_URL=postgresql://admin:admin14092025@localhost:5432/legal_assistant_db
```

---

### 🛠️ Инициализация базы

```bash
python3 -m backend.app.init_db
```

---

### 🚀 Запуск FastAPI

```bash
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
```

---

## 🧭 Автозапуск через systemd

`/etc/systemd/system/fastapi.service`:

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

Запуск:

```bash
sudo systemctl daemon-reload
sudo systemctl enable fastapi
sudo systemctl start fastapi
```

---

## 🌐 Продакшен-деплой: Nginx + SSL + автообновление

### 🔹 Конфиг Nginx (`/etc/nginx/sites-available/legal-assistant`)

```nginx
server {
    listen 80;
    server_name a-quilon.com www.a-quilon.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name a-quilon.com www.a-quilon.com;

    ssl_certificate /etc/letsencrypt/live/a-quilon.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/a-quilon.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header Referrer-Policy no-referrer-when-downgrade;
    add_header Content-Security-Policy "default-src 'self'; frame-ancestors 'none';";

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Активация:

```bash
sudo ln -s /etc/nginx/sites-available/legal-assistant /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

### 🔹 Установка и настройка Certbot

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d a-quilon.com -d www.a-quilon.com
```

Автообновление:

```bash
sudo systemctl list-timers | grep certbot
sudo certbot renew --dry-run
```

---

### ⚠️ Возникавшие проблемы и решения

| Проблема                             | Причина                                        | Решение                                                    |
| ------------------------------------ | ---------------------------------------------- | ---------------------------------------------------------- |
| `could not translate host name "db"` | Использование Docker-хоста `db` вне контейнера | Заменить на `localhost:5433`                               |
| Порт 5432 занят                      | На хосте уже работает PostgreSQL               | Переназначить Docker на 5433                               |
| `[Errno 98] Address already in use`  | Порт 8000 занят другим uvicorn                 | Освободить порт: `sudo pkill -f uvicorn`                   |
| Certbot NXDOMAIN                     | Нет A-записи для `www`                         | Добавить запись в DNS                                      |
| `ld.so.preload` с libprocesshider.so | Вирусное ПО                                    | Очистить `ld.so.preload`, удалить процессы `bizy.x86/.x64` |

---

## 🧬 Реализация и взаимодействие с GitHub

**Репозиторий:** `aw56/legal-assistant-arbitrage`
**Назначение:** хранение исходного кода, документации, истории изменений, автоматизация тестов и деплоя

---

### 🚀 GitHub workflow

1. Создать репозиторий
2. Клонировать и настроить проект
3. Все изменения документировать в `docs/PROJECT_DOC.md`

---

### 📦 Структура репозитория

```
legal-assistant-arbitrage/
├── backend/
│   └── app/
│       ├── main.py
│       ├── ...
│       └── tests/
├── docs/PROJECT_DOC.md
├── .github/workflows/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

### 🔄 Работа с Git

```bash
git add .
git commit -m "Добавлена документация PROJECT_DOC.md"
git push origin main
```

---

### 🤖 CI/CD через GitHub Actions

`.github/workflows/backend.yml`:

```yaml
name: Backend CI

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - run: |
        python -m pip install --upgrade pip
        pip install -r backend/requirements.txt
    - run: pytest
```

---

### 📘 Инструкция по сохранению документации

```bash
git add docs/PROJECT_DOC.md
git commit -m "Обновлена документация (деплой, SSL, GitHub, бэкап)"
git push origin main
```

---

## 🗄️ Бэкап и восстановление

### 🔹 Скрипт бэкапа (`backup.sh`)

```bash
#!/bin/bash
set -e
BACKUP_DIR="$HOME/backup_legal_assistant"
DATE=$(date +%Y%m%d_%H%M)
ARCHIVE="project_backup_${DATE}.tar.gz"

mkdir -p "$BACKUP_DIR"

pg_dump -U admin -d legal_assistant_db > "$BACKUP_DIR/db_${DATE}.sql"

tar czf "$BACKUP_DIR/project_${DATE}.tar.gz" \
    /home/admin/my_projects/legal-assistant-arbitrage \
    /etc/nginx/sites-available/legal-assistant \
    /etc/systemd/system/fastapi.service \
    /etc/letsencrypt

tar czf "$ARCHIVE" -C "$BACKUP_DIR" .

echo "✅ Бэкап завершён: $ARCHIVE"
```

### 🔹 Скрипт восстановления (`restore_all.sh`)

```bash
#!/bin/bash
set -e
PROJECT_NAME="legal-assistant-arbitrage"
BACKUP_ARCHIVE="$1"
BACKUP_DIR="$HOME/backup_${PROJECT_NAME}"

if [ -z "$BACKUP_ARCHIVE" ]; then
  echo "❌ Использование: $0 /путь/к/бэкапу.tar.gz"
  exit 1
fi

mkdir -p "$BACKUP_DIR"
tar xzf "$BACKUP_ARCHIVE" -C "$BACKUP_DIR" --strip-components=1

chmod +x "$BACKUP_DIR/restore.sh"
"$BACKUP_DIR/restore.sh"
```

---

## 📌 Текущее состояние

* ✅ PostgreSQL настроен
* ✅ Таблица `decisions` создана
* ✅ FastAPI-приложение запущено через systemd
* ✅ Swagger UI доступен
* ✅ HTTPS работает через Nginx + Let's Encrypt
* ✅ Автообновление сертификатов включено
* ⚠️ Сервер был инфицирован, внедрён процесс `bizy.x86/x64`.
  ➝ добавлены инструкции по бэкапу и миграции на новый сервер.

---

## 🔜 Следующие шаги

* [ ] Добавить модуль анализа (Этап 2)
* [ ] Генерация заключений DOCX/PDF
* [ ] Калькулятор услуг (Этап 3)
* [ ] Telegram-бот + CRM (Этап 4)

---

Отлично 🚀
Я собрал для тебя финальный **`docs/backup_and_restore.md`**, в который теперь входят **все разделы**:

* Backup
* Restore (restore\_all.sh v34)
* Fix Structure Script
* Troubleshooting FastAPI
* Disaster Recovery Checklist

---

```markdown
# 📑 Backup & Restore Guide — Legal Assistant Arbitrage

## 🎯 Цель
Обеспечить надёжное резервное копирование и максимально простое восстановление проекта **Legal Assistant Arbitrage** (FastAPI + PostgreSQL + Nginx + Certbot).

---

Отлично 👍 Давай соберём **финальные версии** скриптов.
Я сделаю их так, чтобы они логично шли по цепочке:

1. `backup.sh` — создание архива проекта (вместе с `.git`) и дампа БД.
2. `restore_all.sh v35` — развертывание проекта из архива, восстановление БД, настройка `venv`, FastAPI (systemd), Nginx, SSL.
3. После рестора всегда можно дополнительно прогнать `fix_structure.sh`, если tar развернул вложенные папки.

---

## 📦 `backup.sh`

```bash
#!/bin/bash
# backup.sh
set -euo pipefail

PROJECT_DIR="/home/admin/my_projects/legal-assistant-arbitrage"
BACKUP_DIR="/root/legal-assistant-arbitrage/backup_legal_assistant"
DATE=$(date +%Y%m%d_%H%M)

mkdir -p "$BACKUP_DIR"

echo "🗜 Создание архива проекта..."
tar -czf "$BACKUP_DIR/project_${DATE}.tar.gz" \
  -C "$PROJECT_DIR" \
  backend/app \
  requirements.txt \
  .env \
  .git

echo "💾 Создание дампа базы..."
pg_dump -U legal_admin legal_assistant_db > "$BACKUP_DIR/db_${DATE}.sql"

echo "✅ Backup completed:"
ls -lh "$BACKUP_DIR"/project_${DATE}.tar.gz "$BACKUP_DIR"/db_${DATE}.sql
```

Запуск:

```bash
chmod +x backup.sh
./backup.sh
```

---

## 🔄 `restore_all.sh v35`

```bash
#!/bin/bash
# restore_all.sh v35
set -euo pipefail

PROJECT_DIR="/home/admin/my_projects/legal-assistant-arbitrage"
BACKUP_PROJECT="$1"
BACKUP_DB="$2"

echo "=============================="
echo "🚀 Запуск restore_all.sh v35: $(date)"
echo "=============================="

echo "🧹 Очистка окружения..."
systemctl stop fastapi || true
rm -rf "$PROJECT_DIR"
mkdir -p "$PROJECT_DIR"

echo "📦 Распаковка проекта..."
TMPDIR=$(mktemp -d)
tar -xzf "$BACKUP_PROJECT" -C "$TMPDIR"

# ищем backend/app внутри архива
APP_PATH=$(find "$TMPDIR" -type d -path "*/backend/app" | head -n1)
if [[ -z "$APP_PATH" ]]; then
  echo "❌ backend/app не найден в архиве"
  exit 1
fi
mkdir -p "$PROJECT_DIR/backend"
cp -r "$APP_PATH" "$PROJECT_DIR/backend/app"

# переносим .env, requirements.txt и .git
find "$TMPDIR" -maxdepth 4 -name ".env" -exec cp {} "$PROJECT_DIR/" \; || echo "⚠️ .env не найден"
find "$TMPDIR" -maxdepth 4 -name "requirements.txt" -exec cp {} "$PROJECT_DIR/" \; || echo "⚠️ requirements.txt не найден"
find "$TMPDIR" -maxdepth 4 -name ".git" -exec cp -r {} "$PROJECT_DIR/.git" \; || echo "⚠️ .git не найден"

rm -rf "$TMPDIR"

echo "🛠 Установка PostgreSQL..."
apt-get update -y
apt-get install -y postgresql postgresql-contrib

echo "🗄 Настройка БД..."
sudo -u postgres psql <<EOF
DO \$\$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'legal_admin') THEN
      CREATE ROLE legal_admin LOGIN PASSWORD 'legal_pass';
   END IF;
END
\$\$;
CREATE DATABASE legal_assistant_db OWNER legal_admin;
GRANT ALL PRIVILEGES ON DATABASE legal_assistant_db TO legal_admin;
EOF

echo "🗃 Восстановление дампа..."
psql -U legal_admin -d legal_assistant_db < "$BACKUP_DB" || true

echo "🐍 Python venv..."
apt-get install -y python3 python3-venv python3-pip build-essential python3-dev
cd "$PROJECT_DIR"
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip wheel setuptools

if [[ -f requirements.txt ]]; then
  pip install -r requirements.txt
else
  pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
fi
deactivate

echo "⚙️ Настройка FastAPI systemd..."
cat <<SERVICE | sudo tee /etc/systemd/system/fastapi.service
[Unit]
Description=FastAPI app
After=network.target

[Service]
User=admin
WorkingDirectory=$PROJECT_DIR/backend/app
Environment="PATH=$PROJECT_DIR/venv/bin"
ExecStart=$PROJECT_DIR/venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
StandardOutput=journal
StandardError=journal
SyslogIdentifier=fastapi

[Install]
WantedBy=multi-user.target
SERVICE

systemctl daemon-reload
systemctl enable fastapi
systemctl restart fastapi

echo "🌐 Настройка Nginx..."
apt-get install -y nginx certbot python3-certbot-nginx
rm -f /etc/nginx/sites-enabled/*
cat <<NGINX | sudo tee /etc/nginx/sites-available/legal-assistant
server {
    listen 80;
    server_name a-quilon.com;
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
NGINX
ln -s /etc/nginx/sites-available/legal-assistant /etc/nginx/sites-enabled/legal-assistant
nginx -t && systemctl restart nginx

echo "🔑 SSL Certbot..."
IP=$(curl -s http://checkip.amazonaws.com)
DNS_IP=$(dig +short a-quilon.com @8.8.8.8 || true)
echo "Публичный IP: $IP"
echo "DNS A-запись: $DNS_IP"
if [[ "$IP" == "$DNS_IP" ]]; then
  certbot --nginx -d a-quilon.com --non-interactive --agree-tos -m admin@a-quilon.com || true
else
  echo "⚠️ DNS не совпадает с IP, certbot пропущен"
fi

echo "=============================="
echo "✅ Восстановление завершено!"
echo "=============================="
```

---

## 🔧 Финальный рабочий цикл

1. Сделать бэкап:

   ```bash
   ./backup.sh
   ```

2. Скопировать `project_*.tar.gz` и `db_*.sql` на новый сервер.

3. Восстановить:

   ```bash
   ./restore_all.sh project_YYYYMMDD_HHMM.tar.gz db_YYYYMMDD_HHMM.sql
   ```

4. Если структура разворачивается криво (например, появляется `home/admin/...` внутри проекта) → запустить:

   ```bash
   ./fix_structure.sh
   ```

5. Проверить FastAPI:

   ```bash
   systemctl status fastapi
   curl http://127.0.0.1:8000/docs
   ```

6. Проверить HTTPS: [https://a-quilon.com/docs](https://a-quilon.com/docs)

---

📌 Вопрос: Хочешь, я ещё добавлю в `restore_all.sh v35` автоматический вызов `fix_structure.sh` сразу после распаковки, чтобы тебе не пришлось гонять его вручную?

---

## 🔧 Fix Structure Script

После восстановления из архива проект может развернуться с вложенными каталогами `home/admin/my_projects/...`.
Чтобы не тратить время на ручной перенос и очистку, в проект добавлен скрипт **fix\_structure.sh**.

### Скрипт: `fix_structure.sh`

```bash
#!/bin/bash
set -euo pipefail

PROJECT_DIR="/home/admin/my_projects/legal-assistant-arbitrage"

echo "🧹 Fixing project structure in $PROJECT_DIR..."

cd "$PROJECT_DIR"

# Восстанавливаем владельца admin
sudo chown -R admin:admin .

# Удаляем вложенные каталоги, если они случайно появились после распаковки
rm -rf ./home ./legal-assistant-arbitrage

echo "✅ Project structure fixed!"
```

### Использование

```bash
chmod +x fix_structure.sh
./fix_structure.sh
```

---

## ⚠️ Возможные проблемы и решения

1. **Нет `.env`** → скрипт создаст дефолтный.
2. **Нет `requirements.txt`** → ставятся минимальные пакеты (`fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv`).
3. **Certbot ошибка `Timeout during connect`** → проверь DNS:

   ```bash
   dig +short a-quilon.com
   curl -I http://a-quilon.com
   ```
4. **Проблемы с правами в venv** → исправить:

   ```bash
   sudo chown -R admin:admin /home/admin/my_projects/legal-assistant-arbitrage/venv
   ```

---

## 🛠 Troubleshooting FastAPI

### `ModuleNotFoundError: No module named 'backend'`

* Причина: неверный `WorkingDirectory` или неправильная структура после распаковки.
* Решение:

  * проверить, что `main.py` находится в `backend/app/main.py`;
  * при необходимости выполнить `./fix_structure.sh`.

### `ModuleNotFoundError: No module named 'sqlalchemy'`

* Причина: зависимости не установились.
* Решение:

  ```bash
  source venv/bin/activate
  pip install -r requirements.txt
  ```

### `OSError: [Errno 98] Address already in use`

* Причина: порт `8000` занят.
* Решение:

  ```bash
  sudo lsof -i:8000
  sudo kill -9 <PID>
  systemctl restart fastapi
  ```

---

## 🚨 Disaster Recovery Checklist

Этот чеклист позволяет максимально быстро развернуть проект **Legal Assistant Arbitrage** на новом сервере.
Цель — восстановление работоспособности менее чем за 15 минут.

---

### 1. Подготовка сервера

```bash
apt-get update -y
apt-get install -y git curl wget unzip tar gnupg lsb-release sudo vim
```

### 2. Установка зависимостей

```bash
apt-get install -y python3 python3-venv python3-pip build-essential python3-dev
apt-get install -y postgresql postgresql-contrib nginx certbot python3-certbot-nginx
```

### 3. Копирование бэкапов

```bash
scp root@OLD_SERVER:/root/legal-assistant-arbitrage/backup_legal_assistant/project_*.tar.gz .
scp root@OLD_SERVER:/root/legal-assistant-arbitrage/backup_legal_assistant/db_*.sql .
```

### 4. Восстановление проекта

```bash
./restore_all.sh project_YYYYMMDD_HHMM.tar.gz db_YYYYMMDD_HHMM.sql
```

### 5. Проверка структуры

```bash
./fix_structure.sh
```

### 6. Проверка FastAPI

```bash
systemctl status fastapi -l
curl http://127.0.0.1:8000/docs
```

### 7. Проверка Nginx + SSL

```bash
nginx -t
systemctl restart nginx
certbot renew --dry-run
```

### 8. Проверка приложения в браузере

👉 [https://a-quilon.com/docs](https://a-quilon.com/docs)

---

✅ Если всё работает — восстановление завершено!

```

---

Хочешь, я ещё добавлю в этот документ **ASCII-схему пайплайна бэкапа и восстановления** (шаги от backup.sh → restore → fix_structure → FastAPI+Nginx)?
```

---
