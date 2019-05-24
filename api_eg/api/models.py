from django.db import models

class College(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Job(models.Model):
    position = models.CharField(max_length = 50)
    salary = models.IntegerField()

    def __str__(self):
        return self.position
