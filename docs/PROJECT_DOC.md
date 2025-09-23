Отлично 🙌 Давай соберём финальный единый файл `docs/PROJECT_DOC.md` целиком — с учётом **архитектуры, установки, systemd, Nginx+SSL, GitHub и инструкций по документации**.

Сохрани этот файл в проект:

```
legal-assistant-arbitrage/docs/PROJECT_DOC.md
```

---

# 📘 Legal Assistant API — Полная документация

**Дата фиксации:** 23 сентября 2025
**Автор:** Aleksej
**Проект:** Цифровой помощник юриста по арбитражным делам

---

## 🎯 Цель проекта

Создание цифрового юриста по арбитражным делам — платформы, объединяющей:

* нормативную базу и судебную практику
* экспертный правовой анализ
* автоматическую генерацию документов
* прогнозирование исхода спора
* сервисы для клиента и юриста
* маркетинговые инструменты для юридических компаний

---

## 🧱 Архитектура проекта

🔹 1. Нормативная и процессуальная база

База данных законов, кодексов, постановлений Пленума, судебной практики

Источники: pravo.gov.ru, vsrf.ru, арбитражные суды, Консультант/Гарант

Хранение редакций, связей: «норма ↔ практика ↔ разъяснение»

Автоматизация: парсинг через RSS/API/скрипты

🔹 2. Актуализация базы

Фоновый сервис обновлений

Журнал изменений

Указание действующей редакции на дату спора

🔹 3. Стандартизированная форма клиентского запроса

Веб-форма или Telegram-бот

Структура: данные клиента, суть спора, стадия, цели, сроки, регион

🔹 4. Правовой анализ проблемы

Выделение ключевых норм

Поиск аналогичной практики

Иерархия: Конституция → кодекс → спец. закон → практика → локальные акты

🔹 5. Подсветка коллизий права

Сравнение норм

Приоритеты и рекомендации по разрешению

🔹 6. Мотивированное решение

Юридическое заключение: ввод, ссылки на нормы, практика, вывод

🔹 7. Вероятность успеха

NLP-модель на корпусе решений

Классификация: положительное/отрицательное

Учёт суда, региона, суммы

Выход: «65% положительное решение»

🔹 8. Субъективные предпосылки

Проверка правоспособности

Представительство

Возможность удалённого участия

🔹 9. Типовые документы

Шаблоны: иск, отзыв, ходатайство, жалоба

Автогенерация с реквизитами

Форматы: DOCX/PDF

🔹 10. Автономность и локализация

Работа офлайн

Синхронизация обновлений

Локализация под российскую юрисдикцию

🔹 11. Калькулятор стоимости услуг

Среднерыночные тарифы

Коэффициенты: регион, сложность, стадия

Диапазон: «от 80 000 до 120 000 руб.»

🔹 12. Маркетинговая стратегия

Позиционирование: цифровой юрист

Каналы: SEO, реклама, Telegram

УТП: скорость, документы, прогноз

Контент: кейсы, цифры, ссылки на практику
---

## 🚀 Этапы реализации

* **MVP**: АПК РФ + ГК РФ, 5 шаблонов, форма запроса
* **2.0**: Судебная практика, анализ, заключения
* **3.0**: Вероятностная модель, калькулятор
* **4.0**: Маркетинг, CRM, Telegram-бот

---

## ⚙️ Техническая реализация

### 📁 Структура проекта

```
legal-assistant-arbitrage/
├── backend/
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       ├── database.py
│       ├── init_db.py
│       ├── routes/
│       │   └── decisions.py
│       ├── services/
│       │   └── analyzer.py
│       ├── schemas/
│       │   ├── client_request.py
│       │   └── legal_opinion.py
│       └── tests/
│           └── test_analyzer.py
├── docs/
│   └── PROJECT_DOC.md   # Полная документация
├── .github/workflows/   # CI/CD
├── docker-compose.yml
├── requirements.txt
└── README.md
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

```sql
CREATE DATABASE legal_assistant_db;
CREATE USER admin WITH PASSWORD 'admin14092025';
GRANT ALL PRIVILEGES ON DATABASE legal_assistant_db TO admin;
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

### 🧭 Автозапуск через systemd

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

Активация:

```bash
sudo systemctl daemon-reload
sudo systemctl enable fastapi
sudo systemctl start fastapi
```

---

## 🌐 Продакшен-деплой: Nginx + SSL + автообновление

### Конфиг Nginx

`/etc/nginx/sites-available/legal-assistant`

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
    ssl_ciphers HIGH:!aNULL:!MD5;

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
sudo systemctl restart nginx
```

---

### Установка SSL

```bash
sudo certbot --nginx -d a-quilon.com -d www.a-quilon.com
```

Тест обновления:

```bash
sudo certbot renew --dry-run
```

Проверка таймеров:

```bash
systemctl list-timers | grep certbot
```

---

## ⚠️ Возникавшие проблемы и решения

| Проблема                                    | Причина                       | Решение                          |
| ------------------------------------------- | ----------------------------- | -------------------------------- |
| `could not translate host name "db"`        | FastAPI запускался вне Docker | использовать `localhost:5432`    |
| `Address already in use :8000`              | uvicorn висел в фоне          | `sudo pkill -f uvicorn`          |
| NXDOMAIN для www                            | нет DNS-записи                | добавили `A-запись`              |
| `Temporary failure in name resolution`      | UFW блокировал DNS            | разрешили 53/tcp,53/udp          |
| `/etc/ld.so.preload` с `libprocesshider.so` | руткит                        | убрали и очистили crontab        |
| Certbot ошибки                              | DNS/фаервол                   | открыли 80/443, проверили записи |

---

## 🧬 Реализация и взаимодействие с GitHub

**Репозиторий проекта:** `aw56/legal-assistant-arbitrage`
**Назначение:** хранение кода, документации, CI/CD

---

### 🚀 Шаги по созданию проекта на GitHub

```bash
git clone https://github.com/aw56/legal-assistant-arbitrage.git
cd legal-assistant-arbitrage
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 📦 Структура репозитория

```
legal-assistant-arbitrage/
├── backend/      # FastAPI
├── docs/         # Документация
├── .github/      # CI/CD
├── requirements.txt
└── README.md
```

---

### 🔄 Работа с Git

```bash
git add .
git commit -m "Обновлена документация"
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
        pip install -r backend/requirements.txt
        pytest
```

---

### 📘 Инструкция по документации

1. Все изменения отражать в `docs/PROJECT_DOC.md`
2. Перед пушем проверять:

   ```bash
   git diff docs/PROJECT_DOC.md
   ```
3. Коммитить:

   ```bash
   git add docs/PROJECT_DOC.md
   git commit -m "Обновлена документация (деплой, SSL, GitHub)"
   git push origin main
   ```

---

## 📌 Текущее состояние

📌 Текущее состояние

✅ PostgreSQL работает

✅ Таблицы инициализированы

✅ FastAPI под systemd

✅ Nginx + SSL настроены

✅ UFW настроен

✅ CI/CD пайплайн готов

⚠️ Следующие шаги: анализ, генерация документов, калькулятор, Telegram-бот
---

Хочешь, я теперь сделаю ещё отдельный **README.md (краткий, для GitHub)**, а `PROJECT_DOC.md` оставить как полный технический мануал?
