from rest_framework.serializers import ValidationError


class HabitValidator:
    """Икслючает одновременный выбор связанной привычки и указания вознаграждения."""

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        value_1 = dict(value).get(self.field_1)
        value_2 = dict(value).get(self.field_2)

        if value_1 and value_2:
            raise ValidationError('Нельзя одновременно выбирать связанную привычку и указания вознаграждение.')


class TimeValidator:
    """Валидация времени выполнения привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if int(tmp_value) > 120:
            raise ValidationError('Время выполнения не должно быть больше 120 секунд')


class ConnectedHabitValidator:
    """валидация связанной привычки на признак приятной"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if tmp_value:
            if not tmp_value.is_useful:
                raise ValidationError(
                    "В связанные привычки могут попадать только привычки с признаком приятной привычки")


class RewardHabitValidator:
    """Валидация привычки.
    Если привычка приятная, значит исключается выбор вознаграждения и связанной привычки"""

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        value_1 = dict(value).get(self.field_1)
        value_2 = dict(value).get(self.field_2)
        value_3 = dict(value).get(self.field_3)
        if value_1 is True and (value_2 is not None or value_3 is not None):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")
