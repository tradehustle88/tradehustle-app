#!/usr/bin/env bash
set -euo pipefail
sudo apt update && sudo apt install -y python3 python3-venv python3-pip unzip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
[ -f .env ] || cp .env.sample .env
uvicorn main:APP --host 0.0.0.0 --port 8080
