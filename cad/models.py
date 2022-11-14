from django.db import models

class user_details(models.Model):
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    Firebase_id = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

class driver_detail(models.Model):
    driver_id = models.AutoField(primary_key=True)
    d_fname = models.CharField(max_length=50)
    d_lname = models.CharField(max_length=50)
    d_email = model.EmailField(max_length=50)
    d_phone = models.CharField(max_length=15)
    d_password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    d_photo=models.CharField(max_length=100)
    D_firebaseid = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

