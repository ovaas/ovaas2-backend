install:
	PIPENV_VENV_IN_PROJECT=true pipenv install --dev
build:
	docker compose build
start:
	docker-compose up
