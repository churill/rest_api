from django.urls import path
from .views import custom_user_view, custom_user_list_view, custom_user_detail_view


urlpatterns = [
    path('', custom_user_view, name='user_view'),
    path('list/', custom_user_list_view, name='user_list_view'),
    path('detail/<int:pk>/', custom_user_detail_view, name='user_detail_view'),
]
