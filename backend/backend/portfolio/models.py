from django.db import models


class Introduction(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


class AccountLinks(models.Model):
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='account')
    icon = models.ImageField(upload_to='icon')


class Projects(models.Model):
    link = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='projects')


class Timeline(models.Model):
    date = models.DateField()
    text = models.TextField()