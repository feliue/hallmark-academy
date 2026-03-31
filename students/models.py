from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class StudentResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    grade = models.CharField(max_length=5)
    semester = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student.username} - {self.subject}"
