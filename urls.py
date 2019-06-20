from django.conf.urls import url
from MyDrive.views import file_delete,post
urlpatterns = [url('add/', post, name="post"),
    url('<int:id>/delete/', file_delete, name="file_delete"),]