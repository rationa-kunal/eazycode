from django.db import models


class Department(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.department.name + " | " + self.name


class Practicle(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    aim = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    code = models.TextField(blank=True)
    contributor = models.CharField(max_length=100, blank=True)
    contributor_url = models.URLField(default='www.google.co.in')

    def __str__(self):
        return self.subject.name + " | " + self.aim
