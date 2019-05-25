from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class College(models.Model):
    name = models.CharField(max_length=40)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length = 50)
    colleges = models.ManyToManyField(College)

    def __str__(self):
        return self.name
