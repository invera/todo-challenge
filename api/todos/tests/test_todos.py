from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class TodoTestCase(TestCase):

    def setUp(self):
        """Define el cliente para el test y otros variables"""
        self.user = User.objects.create_user(
            username='test@test.com', password='realpassword')
        self.client = APIClient()
        self.todo_data = {
            "name": "Go to Ibiza",
            "description": "A mediados de Junio",
            "completed": False,
            "usuario": self.user.pk
        }
        self.response = self.client.post(
            reverse('todos'),
            data=self.todo_data,
            format="json"
        )

    def test_api_can_create_a_todo(self):
        """Confirmamos si se creo correctamente el TODO"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_api_can_get_a_todo(self):
        """Consultamos el TODO creado"""
        id = self.response.data.get('id')
        url = reverse('todo_list', kwargs={'pk':id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_todo(self):
        """Modificamos el TODO creado"""
        id = self.response.data.get('id')
        change_todo = {'completed': True}
        url = reverse('todo_list', kwargs={'pk':id})
        res = self.client.patch(
            url,
            change_todo,
            'json'
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_todo(self):
        """Eliminamos el TODO creado."""
        id = self.response.data.get('id')
        url = reverse('todo_list', kwargs={'pk': id})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)