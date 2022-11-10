from django.db import models

# Create your models here.
class user_details(models.Model):
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
