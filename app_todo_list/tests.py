from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User


class ListToDoGenerics(APITestCase, APIClient):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser('xavelli', 'foo@bar.com', 'CodeChallenge123')
        self.token = Token.objects.create(user=self.user)

    def test_get(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/v1/todo', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        data = {"title": "Title 15",
                "description": "Description test 15",
                "completed": False}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(path='/api/v1/todo', format='json', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(path='/api/v1/todo/3', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch(self):
        data = {"title": "Title 15",
                "description": "Description test 15",
                "completed": False}
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(path='/api/v1/todo/URL_NON_VALID', format='json', data=data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
