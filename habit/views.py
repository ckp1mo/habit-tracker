from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habit.models import Habit
from habit.paginations import HabitPaginator
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Привязка создателя привычки к ее автору"""

        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Просмотр списка привычек"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self, *args, **kwargs):
        """Отображение списка привычек. Показывает только те, которые создал пользователь"""

        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Детальный просмотр привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitPublicListAPIView(generics.ListAPIView):
    """Просмотр всех публичных привычек"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get_queryset(self):
        """Метод возвращает только публичные привычки"""

        queryset = super().get_queryset()
        return queryset.filter(is_public=True)
