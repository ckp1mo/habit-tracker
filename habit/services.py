import requests
from django.conf import settings
import datetime
from habit.models import Habit


def send_notification(habit):
    """Отправляет уведомление в телеграм чат.
    Получает модель привычки"""
    requests.post(
        url=f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage',
        data={
            'chat_id': habit.owner.chat_id,
            'text': f"Я буду {habit.action} в {habit.time} в {habit.place}",
        },
    )


class HabitFilter:
    """Класс для фильтрации привычек.
    метод daily_habit - делает выборку по ежедневным привычкам, которые не запускались сутки,
    отправляет запрос на отправку уведомления.
    метод weekly_habit - делает выборку по еженедельным привычкам, которые не запускались неделю,
    отправляет запрос на отправку уведомления.
    метод new_habit - делает выборку по привычкам по новым привычкам, которые еще не запускалсиь,
    отправляет запрос на отправку уведомления"""

    HABIT_LIST = Habit.objects.all()
    REMINDER = (datetime.datetime.now() + datetime.timedelta(minutes=30)).time()
    DATE_NOW = datetime.datetime.now().date()
    DATETIME_NOW = datetime.datetime.now()

    def daily_habit(self):
        habit_daily = self.HABIT_LIST.filter(periodicity='daily')
        for habit in habit_daily:
            if habit.last_launch:
                if (self.DATE_NOW - habit.last_launch).days >= 1:
                    if self.REMINDER > habit.time:
                        send_notification(habit)
                        habit.last_launch = datetime.datetime.now()
                        habit.save()

    def weekly_habit(self):
        habit_daily = self.HABIT_LIST.filter(periodicity='weekly')
        for habit in habit_daily:
            if habit.last_launch:
                if (self.DATE_NOW - habit.last_launch).days >= 7:
                    if self.REMINDER > habit.time:
                        send_notification(habit)
                        habit.last_launch = datetime.datetime.now()
                        habit.save()

    def new_habit(self):
        for habit in self.HABIT_LIST:
            if habit.last_launch is None:
                if self.REMINDER > habit.time:
                    send_notification(habit)
                    habit.last_launch = datetime.datetime.now()
                    habit.save()
