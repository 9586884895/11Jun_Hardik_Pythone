from django.db import models

# Create your models here.
class signup(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    