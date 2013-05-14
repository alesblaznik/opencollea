from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


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
    language_code = models.CharField(max_length=5, default='en-us')
    is_language_code_public = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='user_profile/avatar')
    courses_enrolled = models.ManyToManyField(Course)
    website = models.URLField(blank=True)
    lives_in = models.CharField(max_length=128)
    is_lives_in_public = models.BooleanField(default=False)
    biography = models.TextField()
    is_biography_public = models.BooleanField(default=False)
    age_range = models.PositiveIntegerField()
    is_age_range_public = models.BooleanField(default=False)
    gender = models.CharField(max_length=40)
    is_gender_public = models.BooleanField(default=False)


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

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(UserProfile)
    content = models.TextField()
