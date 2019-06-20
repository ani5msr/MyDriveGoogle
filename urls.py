"""untitled4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from MyDrive.views import FileView
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from MyDrive.views import LoginView,LogoutView,user_login,user_logout

from django.conf import urls

urlpatterns = [
  url(r'^admin/', admin.site.urls), url('MyDrive/', include('MyDrive.urls')),
  url('api/v1/auth/login/', LoginView.as_view()),
  url('api/v1/auth/logout/', LogoutView.as_view()),url('login/', user_login, name="user_login"),
  url('logout/', user_logout, name="user_logout"),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
