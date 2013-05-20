from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from opencollea.settings import ETHERPAD_HOST

import code_register.models


class Course(models.Model):
    title = models.CharField(max_length=50)
    machine_readable_title = models.SlugField(max_length=50, unique=True,
                                              blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.machine_readable_title:
            # Title to machine readable format
            self.machine_readable_title = slugify(self.title)

        super(Course, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class UserProfile(User):
    timezone = models.CharField(max_length=40, default='Europe/Ljubljana')
    language_code = models.ForeignKey(
        code_register.models.Language, blank=True, null=True)
    is_language_code_public = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='user_profile/avatar', blank=True)
    courses_enrolled = models.ManyToManyField(Course, blank=True)
    website = models.URLField(blank=True)
    lives_in = models.CharField(max_length=128)
    is_lives_in_public = models.BooleanField(default=False)
    biography = models.TextField()
    is_biography_public = models.BooleanField(default=False)
    age_range = models.ForeignKey(
        code_register.models.AgeRange, blank=True, null=True)
    is_age_range_public = models.BooleanField(default=False)
    gender = models.ForeignKey(
        code_register.models.Gender, blank=True, null=True)
    is_gender_public = models.BooleanField(default=False)
    occupation = models.ForeignKey(
        code_register.models.Occupation, blank=True, null=True)
    is_occupation_public = models.BooleanField(default=False)
    area_of_study = models.ForeignKey(
        code_register.models.AreaOfStudy, blank=True, null=True)
    is_area_of_study_public = models.BooleanField(default=False)


class Tag(models.Model):
    title = models.CharField(max_length=20)
    machine_readable_title = models.SlugField(max_length=50, unique=True,
                                              blank=True)

    def save(self, *args, **kwargs):
        if not self.id and self.title and not self.machine_readable_title:
            # Title to machine readable format
            self.machine_readable_title = slugify(self.title)

        super(Tag, self).save(args, kwargs)

    def __unicode__(self):
        return self.title


class Attachment(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(UserProfile)
    file = models.FileField(upload_to='attachment')
    mime_type = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title


class ReferenceType(models.Model):
    title = models.CharField(max_length=20)
    machine_readable_title = models.CharField(max_length=50, unique=True,
                                              blank=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.machine_readable_title:
            # Title to machine readable format
            self.machine_readable_title = slugify(self.title)

        super(ReferenceType, self).save(args, kwargs)

    def __unicode__(self):
        return self.title


class Reference(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course)
    user = models.ForeignKey(UserProfile)
    author = models.CharField(max_length=50)
    type = models.ForeignKey(ReferenceType)
    attachments = models.ManyToManyField(Attachment)
    tags = models.ManyToManyField(Tag)
    abstract = models.TextField()
    note = models.TextField()
    published = models.DateField()
    link = models.URLField()


class Question(models.Model):
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=20)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    course = models.ForeignKey('Course', related_name='questions')
    published = models.DateField()

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey('Question', related_name='answers')
    user = models.ForeignKey(UserProfile)
    content = models.TextField()

    def save(self, *args, **kwargs):
        super(Answer, self).save(*args, **kwargs)

class EtherpadNote(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=48, blank=False, null=False)
    machine_readable_title = models.SlugField(max_length=48, unique=True,
                                              blank=True, null=False)
    host_url = models.URLField(blank=True, null=False)
    pad_id = models.CharField(max_length=256, blank=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.machine_readable_title:
            # Title to machine readable format
            self.machine_readable_title = slugify(self.title)

        if not self.id:
            # Etherpad info
            self.host_url = 'http://%s/' % ETHERPAD_HOST
            self.pad_id = 'oc-%d-%s' \
                          % (self.course.id,
                          self.machine_readable_title)
        super(EtherpadNote, self).save(*args, **kwargs)
