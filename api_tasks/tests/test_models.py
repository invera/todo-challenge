import pytest
from django.db import IntegrityError

from api_tasks.models import User, Tasks

payload_user = {
    "password": "invera.com",
    "email": "invera@invera.com",
	"first_name": "Invera",
	"last_name": "Invera Software",
	"username": "invera"
}

payload_task = [{
		"title": "Make challenge",
		"description": "For 7 days"
	},
	{
		"title": "Make tests",
		"description": "For the challenge",
        "is_completed": True
	}
]

params = [(payload_task[0], False), (payload_task[1], True)]

class TestModels:
    """A class with tests for the User and Tasks models
    """
    @pytest.mark.django_db
    def test_user_created_ok(self, user):
        """Test to verifies that a user was saved in the db

        Args:
            user (User): instance of User

        Returns:
            None
        """
        expected = payload_user['username']
        assert user.username == expected

    @pytest.mark.django_db
    def test_username_unique_ok(self, user):
        """Test to verify that the username field is unique and raise an exception

        Args:
            user:

        Returns:
            None

        """
        with pytest.raises(IntegrityError):
            new_instance = User.objects.create(**payload_user)
            new_instance.save()


    @pytest.mark.django_db
    @pytest.mark.parametrize("payload, expected", params)
    def test_task_created_ok(self, user, payload, expected):
        """Test to verifies that a task was saved in the db

        Args:
            user: (User): instance of User
            payload: (Dict): payload with data
            expected: (Boolean): status of is_completed current

        Returns:
            None
        """
        payload['owner'] = user

        task = Tasks.objects.create(**payload)
        task.save()

        assert task.title == payload['title']
        assert task.is_completed == expected


