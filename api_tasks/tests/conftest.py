import pytest
from rest_framework.test import APIClient

from api_tasks.models import User, Tasks


@pytest.fixture(scope="function")
def api_client():
    yield APIClient()

@pytest.fixture
def user():
    payload = {
        "password": "invera.com",
        "email": "invera@invera.com",
        "first_name": "Invera",
        "last_name": "Invera Software",
        "username": "invera"
    }
    user = User.objects.create(**payload)
    user.set_password(payload['password'])
    user.save()
    return user

@pytest.fixture
def task(user):
    payload = {
        "title": "Make challenge",
        "description": "For 7 days",
        'owner': user
    }
    task = Tasks.objects.create(**payload)
    task.save()
    return task
@pytest.fixture
def token(user, api_client):
    payload = {
	"username": "invera",
	"password": "invera.com"
}
    response = api_client.post('/api/token/', data=payload)
    return response.json()