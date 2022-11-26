from django.db import models

# Create your models here.
class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    # Firebase_id = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

class driver_detail(models.Model):
    driver_id = models.AutoField(primary_key=True)
    d_fname = models.CharField(max_length=200)
    d_lname = models.CharField(max_length=200)
    d_email = models.EmailField(max_length=200)
    d_phone = models.BigIntegerField()
    d_password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    d_photo=models.ImageField(upload_to='images')
    # D_firebaseid = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)    

# no editing needed