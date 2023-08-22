from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, Group, Permission


from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    start_date = models.DateField()  # Добавьте это поле для даты начала
    end_date = models.DateField()  # Добавьте это поле для даты завершения
    status = models.CharField(max_length=100)  # Добавьте это поле для статуса
    responsible = models.CharField(max_length=100)  # Добавьте это поле для ответственного
    customer = models.CharField(max_length=100)  # Добавьте это поле для заказчика

    def __str__(self):
        return self.title

from django.db import models
from .models import Task

class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='task_files/', default = None, null=True)

    def __str__(self):
        return self.file.name  # Вернуть имя файла как строковое представление
