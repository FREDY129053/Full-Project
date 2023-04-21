from django.db import models


class Mentor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    telegram = models.CharField(max_length=30)
    profession = models.TextField()
    about = models.TextField()

