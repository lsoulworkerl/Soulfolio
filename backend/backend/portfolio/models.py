from django.db import models


class Introduction(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        verbose_name = 'Introduction'
        verbose_name_plural = 'Introductions'


class AccountLinks(models.Model):
    social = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='account')
    icon = models.ImageField(upload_to='icon')

    class Meta:
        verbose_name = 'Account Link'
        verbose_name_plural = 'Account Links'


class Projects(models.Model):
    link = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='projects')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Timeline(models.Model):
    date = models.DateField()
    text = models.TextField()

    class Meta:
        verbose_name = 'Timeline'
        verbose_name_plural = 'Timelines'