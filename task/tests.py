import datetime
import json
import logging
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Task

logger = logging.getLogger('tarea-debug')




class TaskViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="ldalsasso", password="Aa12345678")
        # self.token = Token.objects.create(user=self.user)

        data = {
                "username" : "ldalsasso",
                "password" : "Aa12345678"
               }
        response = self.client.post("/api/v1/user/auth/login/", data, format='json')

        # logger.debug(response)

        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.token = response.data["token"]

        # logger.debug("token: " + self.token)

        self.api_authentication()


        self.task = Task (title = "Primer tarea", description = "Se crea la primer tarea")
        self.task.save()

        self.task = Task (title = "Segunda tarea", description = "Se crea la segunda tarea")
        self.task.save()



    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + self.token)


    def test_profile_list_authenticated(self):
        # logger.debug("test_create_account")      
        response = self.client.get("/api/v1/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        # logger.debug("test_create_account")      
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/v1/users/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_register_task_un_authenticated(self):
        self.client.force_authenticate(user=None)
        data = {
                "title" : "Nueva tarea",
                "description" : "Se crea una nueva tarea"
                }
        response = self.client.post("/api/v1/tareas/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_register_task_test_authenticated(self):
        self.api_authentication()
        data = {
                "title" : "Nueva tarea",
                "description" : "Se crea una nueva tarea"
                }
        response = self.client.post("/api/v1/tareas/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], 0)

        guid = response.data["guid"]

        response = self.client.get("/api/v1/tareas/" + guid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["guid"], guid)

    def test_register_task_test_without_title(self):
        data = {
                "description" : "Se crea una nueva tarea sin titulo"
                }
        response = self.client.post("/api/v1/tareas/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_task_test_without_description(self):
        data = {
                    "title" : "Nueva tarea",
                }
        response = self.client.post("/api/v1/tareas/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_getAll_task(self):
        response = self.client.get("/api/v1/tareas/")
        logger.debug(response.data["count"])      
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

    def test_getAll_task_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/v1/tareas/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_task_un_authenticated(self):
        data = {
                    "status" : 1,
                }
        self.client.force_authenticate(user=None)
        response = self.client.patch("/api/v1/tareas/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_update_task_authenticated(self):
        self.api_authentication()
        data = {
                    "description" : "Se modifica la segunda tarea",
                    "status" : 1
                }

        response = self.client.patch("/api/v1/tareas/" + self.task.guid, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], "Se modifica la segunda tarea")
        self.assertEqual(response.data['status'], 1)

    def test_delete_task_authenticated(self):
        response = self.client.delete("/api/v1/tareas/" + self.task.guid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "delete success")
        
        response = self.client.get("/api/v1/tareas/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

        response = self.client.delete("/api/v1/tareas/" + self.task.guid)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertEqual(response.data, "The task was already deleted")

        t = Task.objects.get(guid = self.task.guid)
        self.assertEqual(t.status, 3)


    def test_delete_task_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete("/api/v1/tareas/" + self.task.guid)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_search_task_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete("/api/v1/tareas/search/" + "segu")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_task_authenticated(self):
        self.api_authentication()
        response = self.client.get("/api/v1/tareas/search/seg")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_search_task_range_date(self):
        self.api_authentication()

        today = datetime.today()
        date = datetime.strptime(str(today)[0:10], "%Y-%m-%d")

        fromDate = str(date - timedelta(days=7))[0:10]
        toDate = str(date)[0:10]

        url = "/api/v1/tareas/search/" + fromDate + "/" + toDate + "/"

        logger.debug("url: " + url) 

        self.api_authentication()
        response = self.client.get(url, format='json')

        logger.debug("response.data['count']: " + str(response.data["count"])) 

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

    def test_search_task_range_date_2(self):
        self.api_authentication()

        today = datetime.today()
        date = datetime.strptime(str(today)[0:10], "%Y-%m-%d")

        fromDate = str(date)[0:10]
        toDate = str(date)[0:10]

        url = "/api/v1/tareas/search/" + fromDate + "/" + toDate + "/"

        logger.debug("url: " + url) 

        response = self.client.get(url)

        t = Task.objects.get(guid = self.task.guid)
        logger.debug("created_date: " + str(t.created_date))      

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

    def test_search_task_range_date_3(self):
        self.api_authentication()
        today = datetime.today()
        date = datetime.strptime(str(today)[0:10], "%Y-%m-%d")

        fromDate = str(date + timedelta(days=1))[0:10]
        toDate = str(date + timedelta(days=2))[0:10]

        url = "/api/v1/tareas/search/" + fromDate + "/" + toDate + "/"

        logger.debug("url: " + url) 

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)

    def test_search_task_range_date_and_text(self):
        self.api_authentication()
        today = datetime.today()
        date = datetime.strptime(str(today)[0:10], "%Y-%m-%d")

        fromDate = str(date - timedelta(days=7))[0:10]
        toDate = str(date)[0:10]

        url = "/api/v1/tareas/search/" + fromDate + "/" + toDate + "/pri"
        logger.debug("url: " + url) 

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_search_task_range_date_and_text(self):
        self.api_authentication()
        today = datetime.today()
        date = datetime.strptime(str(today)[0:10], "%Y-%m-%d")

        fromDate = str(date - timedelta(days=7))[0:10]
        toDate = str(date - timedelta(days=1))[0:10]

        url = "/api/v1/tareas/search/" + fromDate + "/" + toDate + "/pri"
        logger.debug("url: " + url) 

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)



