from django.urls import path
from .views import custom_user_view


urlpatterns = [
    path('', custom_user_view, name='user_view'),
]
