
from django.db import models

from accounts.models import Account

class StudentProfile(models.Model):
    student=models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    address=models.TextField(max_length=300, null=True)
    dob=models.DateField(null=True)
    image=models.ImageField(max_length=2500,null=True)
    phone=models.IntegerField(null=True)

    def __str__(self):
        return  self.student.first_name
    
