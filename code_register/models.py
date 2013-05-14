from django.db import models

class Gender(models.Model):
    title = models.CharField(max_length=40)
    machine_readable_title = models.SlugField(max_length=12, unique=True)

    def __unicode__(self):
        return self.title


class Language(models.Model):
    code = models.CharField(max_length=5)
    title = models.CharField(max_length=40)

    def __unicode__(self):
        return self.title

class AgeRange(models.Model):
    min = models.PositiveIntegerField()
    max = models.PositiveIntegerField()

    def __unicode__(self):
        return "%d-%d" % (self.min, self.max)

class Occupation(models.Model):
    title = models.CharField(max_length=40)

    def __unicode__(self):
        return self.title

class AreasOfStudy(models.Model):
    title = models.CharField(max_length=40)

    def __unicode__(self):
        return self.title
