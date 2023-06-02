import pytest

from api_tasks.models import User

payload = {
    "title": "Make challenge",
    "description": "For 7 days"
}

class TestViews:
    """A class with tests for the Tasks and Record views
    """
    @pytest.fixture
    def client(self, token, api_client):
        """Method with authenticated client

        Args:
            token: (JWT): Access token
            api_client: (APIClient):  instance of APIClient

        Returns:
            A client with authorization
        """
        api_client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token['access']}",
        )
        return api_client

    @pytest.mark.django_db
    def test_register_user(self, api_client):
        """Test registering a user

        Args:
            api_client: (APIClient): instance of api_client

        Returns:
            None
        """
        payload = {
            "password": "invera.com",
            "password2": "invera.com",
            "email": "invera@invera.com",
            "first_name": "Invera",
            "last_name": "Invera Software",
            "username": "invera"
        }
        response = api_client.post('/api/register/', data=payload, format="json")
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_tasks(self, client):
        """Test create a task

        Args:
            client: (APIClient): api_client with authorization

        Returns:
            None
        """
        response = client.post('/api/tasks/', data=payload, format="json")
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_get_all_tasks(self, client):
        """Test that lists all the tasks of the current user

        Args:
            client: (APIClient): api_client with authorization

        Returns:
            None
        """
        data = [{
            "title": "Make challenge",
            "description": "For 7 days"
        }, {
            "title": "Make tests",
            "description": "For the challenge",
            "is_completed": True
        }]
        for _payload in data:
            response = client.post('/api/tasks/', data=_payload, format="json")
            assert response.status_code == 201

        response = client.get(f'/api/tasks/', format="json")
        assert len(response.json()['results']) == len(data)

    @pytest.mark.django_db
    def test_get_task_by_pk(self, client):
        """Test that retrieves a task by pk

        Args:
            client: (APIClient): api_client with authorization

        Returns:
            None
        """
        response = client.post('/api/tasks/', data=payload, format="json")
        assert response.status_code == 201

        pk = response.json()['id']
        response = client.get(f'/api/tasks/{pk}/', format="json")
        assert response.status_code == 200
        assert response.json()['title'] == payload['title']

    @pytest.mark.django_db
    def test_update_task_by_pk(self, client):
        """Test that update a task by pk

        Args:
            client: (APIClient): api_client with authorization

        Returns:
            None
        """
        response = client.post('/api/tasks/', data=payload, format="json")
        assert response.status_code == 201

        pk = response.json()['id']
        payload["title"] = "Challenge completed"
        payload["is_completed"] = "true"

        response = client.patch(f'/api/tasks/{pk}/', data=payload, format="json")
        assert response.status_code == 200
        assert response.json()['title'] == 'Challenge completed'

    @pytest.mark.django_db
    def test_delete_task_by_pk(self, client):
        """Test that delete a task by pk

        Args:
            client: (APIClient): api_client with authorization

        Returns:
            None
        """
        response = client.post('/api/tasks/', data=payload, format="json")
        assert response.status_code == 201

        pk = response.json()['id']
        response = client.delete(f'/api/tasks/{pk}/')
        assert response.status_code == 204

    @pytest.mark.django_db
    def test_filter_task_by_created_at(self, client):
        """Test that filter a task by date

        Args:
             client: (APIClient): api_client with authorization

        Returns:
            None
        """
        response = client.post('/api/tasks/', data=payload, format="json")
        assert response.status_code == 201

        date = response.json()['created_at'][0:10]
        expected = response.json()['title']

        response = client.get(f'/api/tasks/', {"created_at": date})
        assert response.json()['results'][0]['title'] == expected

    @pytest.mark.django_db
    def test_get_all_tasks_by_admin(self, user, client, task):
        """Test that retrieves all tasks. Endpoint available only for admin

        Args:
            user: (User): instance of User
            client: (APIClient): api_client with authorization
            task: (Tasks): instance of Tasks

        Returns:
            None
        """
        User.objects.filter(pk=user.id).update(is_staff=True)
        response = client.get('/api/tasks/all/')
        assert response.status_code == 200
        assert response.json()['count'] == 1