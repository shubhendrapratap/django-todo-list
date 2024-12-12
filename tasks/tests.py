from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Task
from rest_framework.test import APIClient
from rest_framework import status

class TaskTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'due_date': '2024-12-31',
            'tags': 'tag1,tag2',
            'status': 'OPEN'
        }

    def test_create_task(self):
        response = self.client.post('/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_task(self):
        self.test_create_task()
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add additional tests for update and delete operations
