from django.db import models

# Create your models here.
class Member(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    country=models.CharField(max_length=100)