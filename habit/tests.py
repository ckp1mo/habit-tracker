from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habit.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):
    """Тестирование CRUD модели привычек"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='test_name', password='dbreyz', chat_id=123456)
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place='Test place',
            time='9:00',
            action='Test action',
            duration=70,
        )

    def test_create_habit(self):
        """Тест создания привычки"""

        data = {
            'owner': self.user.id,
            'place': 'Test place',
            'time': '9:00',
            'action': 'Test Action',
            'duration': 70,
        }
        response = self.client.post('/create-habit/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Habit.objects.all().exists())

    def test_list_habit(self):
        """Тест просмотр привычек"""

        response = self.client.get('/list-habit/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_habit(self):
        """Просмотр одной привычки"""

        response = self.client.get(f'/retrieve-habit/{self.habit.pk}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        """Редактирование привычки"""

        data = {'duration': 90}
        response = self.client.patch(f'/update-habit/{self.habit.pk}', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['duration'], 90)

    def test_delete_habit(self):
        """Удаление привычки"""

        response = self.client.delete(f'/delete-habit/{self.habit.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_public_list_habit(self):
        """Вывод публичных привычек"""

        Habit.objects.create(
            owner=self.user,
            place='Test place',
            time='12:00',
            action='Test action',
            duration=70,
            is_public=True,
        )
        response = self.client.get('/list-public-habit/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Habit.objects.filter(is_public=True))
