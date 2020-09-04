from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
