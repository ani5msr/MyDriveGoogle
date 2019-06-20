from django.db import models
from django.contrib.auth.models import User
class File(models.Model):
  file_name = models.CharField(max_length=200)
  remark = models.TextField(max_length=200)
  created_by = models.ForeignKey(User,on_delete=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return "%s" % (self.file_name)