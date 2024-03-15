from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Periodicity(models.TextChoices):
    DAILY = 'daily', 'Раз в день'
    WEEKLY = 'weekly', 'Раз в неделю'


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    place = models.CharField(max_length=100, verbose_name='Место выполнения')
    time = models.TimeField(verbose_name='Во сколько выполнять')
    action = models.CharField(verbose_name='Действие')
    is_useful = models.BooleanField(default=True, verbose_name='Приятная привычка')
    connected_habit = models.ForeignKey('Habit', on_delete=models.CASCADE, verbose_name='Связанная привычка',
                                        **NULLABLE)
    periodicity = models.CharField(choices=Periodicity.choices, default=Periodicity.DAILY,
                                   verbose_name='Периодичность')
    reward = models.CharField(max_length=200, **NULLABLE, verbose_name='Вознаграждение')
    duration = models.PositiveIntegerField(default=60, verbose_name='Время выполнения в секундах')
    is_public = models.BooleanField(default=False, verbose_name='Общий доступ')
    last_launch = models.DateField(**NULLABLE, verbose_name='предыдущий запуск')

    def __str__(self):
        return f'Пользователь - {self.owner}, действие - {self.action}, периодичность {self.periodicity}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
