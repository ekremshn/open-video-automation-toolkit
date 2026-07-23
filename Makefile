.PHONY: install run test lint docker-up docker-down

install:
	pip install -r requirements-dev.txt

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 3101

test:
	pytest -q

lint:
	ruff check .

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down
