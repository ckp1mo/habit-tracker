from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserAPITestCase(APITestCase):
    """Тестирование создание пользователя"""

    def setUp(self):
        pass

    def test_create_user(self):
        """Создание пользователя"""

        data = {
            'username': 'test_name',
            'chat_id': 123456,
            'password': 'dbreyz',
        }
        response = self.client.post('/users/user-create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.all().exists())
