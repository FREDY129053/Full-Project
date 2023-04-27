import mysql

from django.db import models
from mysql.connector import connect


class Anketa(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mail = models.EmailField()
    tg = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    exp = models.IntegerField()
    sphere = models.TextField()
    about = models.TextField()


class Mentor(models.Model):
    objects = models.Manager()
    id = models.IntegerField(primary_key=True)
    mentor_name = models.CharField(max_length=50)
    mentor_surname = models.CharField(max_length=50)
    mentor_telegram = models.CharField(max_length=30)
    experience = models.IntegerField()
    sphere = models.TextField()
    price = models.CharField(max_length=50)
    number_of_rescued = models.FloatField()
    about = models.TextField()

    def get_formate_about(self):
        return self.about.replace('*', '\n')

    class Meta:
        db_table = 'mentors'

