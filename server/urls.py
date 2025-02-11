"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from rest_framework_jwt import views as jwt_views


def health_check_view(request):
    print('test OK!!')
    return HttpResponse(status=200)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/token/', jwt_views.obtain_jwt_token, name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.refresh_jwt_token, name='token_refresh'),
    path('auth/token/verify/', jwt_views.verify_jwt_token, name='token_verify'),

    path('api/accounts/', include('accounts.urls')),
    path('api/sample/', include('myapp_1.urls')),
    path('', health_check_view),
]
