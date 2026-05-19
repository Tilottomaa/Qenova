from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    profile_pic = models.ImageField(upload_to='photos/')
    role = models.CharField(max_length=20, default='user')
    status = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name



class OrganizationUser(models.Model):
    organization_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    logo = models.ImageField(upload_to='logos/')
    working_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.organization_name


class Admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.name



