install:
	PIPENV_VENV_IN_PROJECT=true pipenv install --dev
build:
	docker compose build
start:
	docker-compose up
create-migration:
	docker-compose exec web python manage.py makemigrations
migrate:
	docker-compose exec web python manage.py migrate
create-superuser:
	docker-compose exec web python manage.py createsuperuser
