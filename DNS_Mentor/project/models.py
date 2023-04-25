import mysql

from django.db import models
from mysql.connector import connect


class Mentor(models.Model):
    objects = models.Manager()
    mentor_name = models.CharField(max_length=50)
    mentor_surname = models.CharField(max_length=50)
    mentor_telegram = models.CharField(max_length=30)
    experience = models.IntegerField()
    sphere = models.TextField()
    price = models.CharField(max_length=50)
    number_of_rescued = models.FloatField()

    class Meta:
        db_table = 'mentors'

