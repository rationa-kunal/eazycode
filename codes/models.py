from django.db import models


class Department(models.Model):

    name = models.CharField(max_length=100)


class Subject(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Practicle(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    aim = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    code = models.TextField(blank=True)
