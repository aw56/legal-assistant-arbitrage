#!/bin/bash
# fix_git.sh — очистка Git-репозитория от venv и лишних файлов
set -euo pipefail

PROJECT_DIR="/home/admin/my_projects/legal-assistant-arbitrage"

cd "$PROJECT_DIR"

echo "📝 Обновляем .gitignore..."
cat > .gitignore <<EOF
# Python
__pycache__/
*.pyc
*.pyo

# Virtual env
venv/

# Local configs
.env
*.log

# Backup dirs
backup_legal_assistant/
EOF

echo "🧹 Чистим индекс Git от мусора..."
git rm -r --cached venv || true
git rm -r --cached __pycache__ || true
git rm --cached .env || true
git rm -r --cached backup_legal_assistant || true

echo "📦 Добавляем изменения в индекс..."
git add .gitignore
git add .

echo "✅ Готово! Теперь сделай коммит:"
echo "   git commit -m 'Clean repo: add .gitignore, remove venv/env/backups from git'"
