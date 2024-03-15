from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    chat_id = models.PositiveIntegerField(verbose_name='telegram id')

    def __str__(self):
        return f'{self.username}, {self.chat_id}'
