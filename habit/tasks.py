from celery import shared_task

from habit.services import HabitFilter


@shared_task
def check_time():
    """Функция запуска проверки наступления времени уведомления.
    Работает с классом HabitFilter и его методами.
    Поочередно запускаются методы класса для проверки наступления временного события"""

    habit_send = HabitFilter()
    habit_send.new_habit()
    habit_send.daily_habit()
    habit_send.weekly_habit()
