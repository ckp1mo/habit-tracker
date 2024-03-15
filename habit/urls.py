from django.urls import path
from habit.apps import HabitConfig
from habit.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDeleteAPIView, HabitPublicListAPIView

app_name = HabitConfig.name


urlpatterns = [
    path('create-habit/', HabitCreateAPIView.as_view(), name='create-habit'),
    path('list-habit/', HabitListAPIView.as_view(), name='list-habit'),
    path('retrieve-habit/<int:pk>', HabitRetrieveAPIView.as_view(), name='retrieve-habit'),
    path('update-habit/<int:pk>', HabitUpdateAPIView.as_view(), name='update-habit'),
    path('delete-habit/<int:pk>', HabitDeleteAPIView.as_view(), name='delete-habit'),

    path('list-public-habit/', HabitPublicListAPIView.as_view(), name='list-public-habit'),
]
