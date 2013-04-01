from django.db import models
from hashlib import md5

class Course(models.Model):
    hash = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=128)
    source = models.CharField(max_length=255)
    url = models.URLField()

    def save(self, *args, **kwargs):
        if not self.hash:
            # We identify each remote course with hash.
            hash_calc = md5()
            hash_calc.update(self.url.encode('utf-8'))
            self.hash = hash_calc.hexdigest()

        super(Course, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.source + " - " + self.title


