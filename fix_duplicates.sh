#!/bin/bash
set -euo pipefail

PROJECT_DIR="/home/admin/my_projects/legal-assistant-arbitrage"
DUP_DIR="$PROJECT_DIR/legal-assistant-arbitrage"

echo "🧹 Проверка структуры проекта..."

if [[ -d "$DUP_DIR" ]]; then
  echo "⚠️ Найдена вложенная папка: $DUP_DIR"
  
  echo "📦 Переносим содержимое наверх..."
  mv -n "$DUP_DIR"/* "$PROJECT_DIR"/ 2>/dev/null || true
  mv -n "$DUP_DIR"/.[!.]* "$PROJECT_DIR"/ 2>/dev/null || true

  echo "🗑 Удаляем лишнюю вложенную директорию..."
  rm -rf "$DUP_DIR"

  echo "🔧 Выравниваем владельцев..."
  sudo chown -R admin:admin "$PROJECT_DIR"

  echo "✅ Структура проекта исправлена!"
else
  echo "✅ Дублирующей папки нет, всё в порядке."
fi

