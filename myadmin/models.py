from os import access
from django.db import models
from accounts.models import Account
# Create your models here.


class StudentMark(models.Model):
    student=models.ForeignKey(Account, on_delete=models.CASCADE)
    marks=models.IntegerField(null=True)

    def __str__(self):
        return self.student.first_name
    