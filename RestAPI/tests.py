from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Task
from .serializers import TaskSerializer


# Create your tests here.

class TestListTask(APITestCase):
    @classmethod
    def setUpTestData(cls):
        setup = [
            {
                "Job": "Create Django project",
                "Auto_Date": "2022-06-29T03:28:25.110170Z",
                "Date": "06-29-2022",
                "Done": 0
            },
            {
                "Job": "Update Django Code",
                "Auto_Date": "2022-06-29T03:28:40.408833Z",
                "Date": "06-29-2022",
                "Done": 0
            },
            {
                "Job": "Delete Django App",
                "Auto_Date": "2022-06-30T06:31:40.408833Z",
                "Date": "06-30-2022",
                "Done": 0
            },
            # {
            #     "Job": "Read Database",
            #     "Auto_Date": "2022-07-01T06:31:40.408833Z",
            #     "Date": "07-01-2022",
            #     "Done": 0
            # },
        ]

        cls.tasks = [Task.objects.create(**item) for item in setup]
        cls.task = cls.tasks[0]

    def test_all_tasks(self):
        response = self.client.get(reverse('task-list'))

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.tasks), len(response.data))

        for task in self.tasks:
            self.assertIn(
                TaskSerializer(instance=task).data,
                response.data
            )

    def test_specific_task(self):
        response = self.client.get(
            reverse("task-detail", args=[self.task.id])
        )

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(
            TaskSerializer(instance=self.task).data,
            response.data
        )

    def test_new_task(self):

        payload = {
            "Job": "Rollback Git",
            "Date": "06-30-2022",
            "Done": 0
        }

        response = self.client.post(reverse("task-list"), payload)
        created_task = Task.objects.get(Job=payload["Job"])

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)

        for k, v in payload.items():
            self.assertEquals(v, response.data[k])
            self.assertEquals(v, getattr(created_task, k))

    def test_edit_task(self):

        task_data = {
            "Job": "Rollback Gitttttt",
            "Date": "14-30-2022",
            "Done": 0
        }
        task = Task.objects.create(**task_data)

        payload = {
            "Job": "Rollback Git",
            "Date": "06-30-2022",
            "Done": 1
        }

        response = self.client.patch(
            reverse("task-detail", args=[self.task.id])
        )

        task.refresh_from_db()

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        for k, v in payload.items():
            self.assertEquals(v, response.data[k])
            self.assertEquals(v, getattr(task, k))

    def test_delete_task(self):
        response = self.client.delete(
            reverse("task-detail", args=[self.task.id])
        )

        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertFalse(Task.objects.filter(pk=self.task.id))
