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

```

---

Хочешь, я сразу подготовлю для тебя `backup.sh` и `restore_all.sh` как отдельные файлы, чтобы ты мог их просто скопировать на сервер?
```
