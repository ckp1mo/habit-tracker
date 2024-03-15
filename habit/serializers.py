from rest_framework import serializers

from habit.models import Habit
from habit.validators import HabitValidator, TimeValidator, ConnectedHabitValidator, RewardHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели привычек"""

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            HabitValidator(field_1='connected_habit', field_2='reward'),
            TimeValidator(field='duration'),
            ConnectedHabitValidator(field='connected_habit'),
            RewardHabitValidator(field_1='is_useful', field_2='connected_habit', field_3='reward'),
        ]
