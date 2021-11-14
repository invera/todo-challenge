# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from todo.utils.authenticate import get_tokens_for_user

# Model
from todo.management.models import Task
from todo.users.models import User, Profile


class TaskAPITestCase(APITestCase):
    """Member invitation API test case."""

    def setUp(self):
        """Test case setup."""

        # URL
        self.url = '/tasks/'

        # Data

        self.user = User.objects.create_user(
            email='test@gmail.com',
            username='admin@testSRL',
            password='admin123',
            is_verified=True
        )

        self.profile = Profile.objects.create(
            user=self.user,
            first_name='Test profile',
            tasks_pending=1,
            tasks_created=1
        )

        self.task = Task.objects.create(
            user=self.user,
            title='Test task'
        )

        # Auth
        self.token = get_tokens_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(self.token))

    def test_list_tasks(self):
        """Testeo de la lista de tareas"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)

    def test_create_task(self):
        """Testeo de la creacion de tareas"""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Creacion
        create_data = {
            'title': 'TestTask2',
            'description': 'Descripcion Extensa',
            'priority': 'P1',
            'color': 'C1'
        }

        response = self.client.post(self.url, create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'TestTask2')

        # Revisamos las metricas
        profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(profile.tasks_created, self.profile.tasks_created + 1)
        self.assertEqual(profile.tasks_pending, self.profile.tasks_pending + 1)

    def test_update_Task(self):
        """Testeo de la actualizacion del Taske"""
        url = self.url
        url = url + '{}/'.format(
            self.task.pk
        )

        # Update
        update_data = {
            'title': 'TestTask22',
            'is_finalize': True
        }
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'TestTask22')

        # Detectamos los cambios en el perfil
        profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(profile.tasks_finalize, self.profile.tasks_finalize + 1)
        self.assertEqual(profile.tasks_pending, self.profile.tasks_pending - 1)

        # Caso 1
        update_data['priority'] = 'C2412'
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_Task(self):
        """Testeo de la destruccion de un Taske"""
        url = self.url
        url = url + '{}/'.format(
            self.task.pk
        )

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
