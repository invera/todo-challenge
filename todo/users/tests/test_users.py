# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from todo.utils.authenticate import get_tokens_for_user

# Model
from todo.management.models import Task
from todo.users.models import User, Profile


class UserAPITestCase(APITestCase):
    """Member invitation API test case."""

    def setUp(self):
        """Test case setup."""

        # URL
        self.url = '/users/'

        # Data base

        self.data = {
            'email': 'test@gmail.com',
        }

        # Data

        self.user = User.objects.create_user(
            email='test@gmail.com',
            username='admin@testSRL',
            password='admin123',
            is_verified=True,
        )

        self.profile = Profile.objects.create(
            user=self.user,
            first_name='Test profile',
            last_name='Test lastName'
        )

        self.user2 = User.objects.create_user(
            email='test22@gmail.com',
            username='admin22@testSRL',
            password='admin123',
            is_verified=True,
        )

        self.profile2 = Profile.objects.create(
            user=self.user2,
            first_name='Test profile222',
            last_name='Test lastName222'
        )

        self.task = Task.objects.create(
            user=self.user,
            title='Test task'
        )

        # Auth
        self.token = get_tokens_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(self.token))

    def test_view_clients_user(self):
        """Testeo de vista de tareas que crearon diferentes usuarios"""
        # User1
        # Creacion
        url = '/tasks/'
        create_data = {
            'title': 'TestTask2'
        }

        response = self.client.post(url, create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Vista
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

        # User 2
        # Auth
        self.token = get_tokens_for_user(self.user2)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(self.token))

        response = self.client.post(url, create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Vista
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_signup_user(self):
        """Testeo de la creacion de cuenta"""
        url = self.url
        url = url + 'signup/'

        create_data = {
            'email': 'test2@gmail.com',
            'username': 'Pedro123',
            'first_name': 'NameTest',
            'last_name': 'LastTest',
            'password': 'admin1234',
            'phone_number': '+512664647851'
        }

        response = self.client.post(url, create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)

        # Profile test
        self.assertEqual(Profile.objects.count(), 3)

        # Case 1
        response = self.client.post(url, create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Case 2
        create_data['email'] = 'test3333@gmail.com'
        response = self.client.post(url, create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login(self):
        """Testeo de inicio de sesion"""
        url = self.url
        url = url + 'login/'

        login_data = {
            'username': self.user.username,
            'password': 'admin123'
        }

        response = self.client.post(url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['username'], self.user.username)
        self.assertEqual(response.data['profile']['first_name'], self.profile.first_name)

        # Cambiar el username
        login_data['username'] = 'NombreFalso'
        response = self.client.post(url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Cambiar la password
        login_data['username'] = self.user.username
        login_data['password'] = 'PasswordFalsa'
        response = self.client.post(url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user(self):
        """Testeo de la obtencion del usuario"""

        # Retrieve
        url = self.url
        url = url + '{}/'.format(
            self.user.username,
        )

        response = self.client.get(url)
        profile_id = Profile.objects.get(user=self.user).pk
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['username'], self.user.username)
        self.assertEqual(response.data['profile']['id'], profile_id)

    def test_update_user(self):
        # Update
        url = self.url
        url = url + '{}/'.format(
            self.user.username,
        )
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        update_data = {
            'username': 'TestFall',
            'email': 'testfall@gmail.com',
        }

        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], update_data['username'])
        self.assertEqual(response.data['email'], update_data['email'])

    def test_change_password_user(self):
        """Testeo del cambio de contraseña"""
        # Change password
        url = self.url
        url = url + 'change_password/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.user.set_password('admin123')
        self.user.save()

        password_data = {
            'old_password': 'admin123',
            'new_password': 'admin1234',
            'new_password_confirmation': 'admin1234'
        }

        response = self.client.post(url, password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(username=self.user.username)
        self.assertEqual(user.check_password('admin1234'), True)

        # Caso 1
        response = self.client.post(url, password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Caso 2
        password_data = {
            'old_password': 'admin1234',
            'new_password': 'admin1234567',
            'new_password_confirmation': 'admin1234'
        }
        response = self.client.post(url, password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user(self):
        """Testeo de eliminacion de cuenta"""
        # Eliminar cuenta
        url = self.url
        url = url + '{}/'.format(
            self.user.username,
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        users = User.objects.filter(username=self.user.username).count()
        self.assertEqual(users, 0)
