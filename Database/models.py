# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)  
    password = models.CharField(max_length = 100)  
    def __str__(self):
        return self.name


class Group(models.Model):
    ADMINISTRATOR = 'Admin'
    WEBUSER = 'WebUser'
    DEVELOPER = 'Developer'
    GEST = 'Gest'
    
    GROUP_NAMES = (
        (ADMINISTRATOR, 'Admin'),
        (WEBUSER, 'WebUser'),
        (DEVELOPER, 'Developer'),
        (GEST, 'Gest'),
    )

    name = models.CharField(max_length = 10, choices = GROUP_NAMES )
    permissions = models.BooleanField()
   
    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Layer(models.Model):

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
