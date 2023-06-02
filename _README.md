# Challenge for Invera

## Pre-requisites:
- docker
- docker compose

## Steps:
1. Create a file called `.env` with environment variables in the root of the backend project. *Important!*
2. Build with `docker compose build`
3. Run with `docker compose up`

## How to use (in terminal run):
   - `docker compose exec web python manage.py migrate`
   - `docker compose exec web python manage.py createsuperuser`. *Optional!*
   - `docker compose exec web pytest -v`
   - Go to `http://localhost:8000/admin/` or `http://localhost:8000/swagger/`.
   - You can use your preference rest client and test the endpoints

## Environments (`.env`)
- SECRET_KEY = "Generate secret key"
- POSTGRES_DB = 
- POSTGRES_USER =
- POSTGRES_PASSWORD =