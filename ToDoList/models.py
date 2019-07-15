# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.
# from django.contrib.auth.models import User


class ToDo(models.Model):
    # user = models.ForeignKey(User)
    todo_id = models.IntegerField(primary_key=True)
    owner = models.CharField(max_length=10)
    content = models.CharField(max_length=300)
    # flag = models.CharField()
    add_time = models.DateTimeField(auto_now_add=True)
    resolve_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=4, default='No')

    def __str__(self):
        # return '%d %s %s %s' % (self.todo_id, self.owner, self.content, self.status)
        return '%s %s %s' % (self.owner, self.content, self.status)

    class Meta:
        ordering = ['add_time', 'status']


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
