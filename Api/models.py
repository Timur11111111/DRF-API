from django.db import models

class people(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)

    def __str__(self):
        return self.firstname