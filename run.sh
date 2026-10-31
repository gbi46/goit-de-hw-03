#!/bin/bash

set -e

if [ ! -d ".venv" ]; then
	echo "Creating virtual env ..."
	python -m venv .venv
fi

source .venv/bin/activate

pip install -r requirements.txt

if ! command -v java >/dev/null 2>&1; then
	echo "Java is not installed. Installing OpenJDK 17 ..."
	sudo apt update
	sudo apt install openjdk-17-jdk
fi

python main.py
