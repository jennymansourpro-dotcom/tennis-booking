#!/usr/bin/env bash
# Installe les dépendances Python et le navigateur Chromium pour Playwright.
set -euo pipefail

cd "$(dirname "$0")"

pip install -r requirements.txt
python -m playwright install --with-deps chromium

echo "Setup OK."
