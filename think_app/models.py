from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class Enrollment(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)