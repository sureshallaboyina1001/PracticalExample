from django.db import models


class LoginSystem(models.Model):
    username         = models.CharField(max_length=60,blank=True,null=True)
    user_location    = models.CharField(max_length=60,blank=True,null=True)
    email            = models.CharField(max_length=60,blank=True,null=True)
    confirm_email    = models.CharField(max_length=60,blank=True,null=True)
    password         = models.CharField(max_length=60,blank=True,null=True)
    confirm_password = models.CharField(max_length=60,blank=True,null=True)


class LoginTime(models.Model):
    login_id= models.CharField(max_length=60,blank=True,null=True)
    login_time = models.DateTimeField(auto_now_add=True)
