from django.db import models
from django.contrib.auth.models import User

class note(models.Model):
  text = models.CharField(max_length=300,default="a note")
  created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
