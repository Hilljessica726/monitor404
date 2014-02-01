from django.db import models
from django.contrib.auth.models import User


class UserSite(models.Model):
    user = models.ForeignKey(User)
    host = models.CharField(max_length=253) # max length of a domain name
    slug = models.SlugField(max_length=253)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.host)
        super(UserSite, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s: %s" % (self.user, self.host)


class LogEntry(models.Model):
    site = models.ForeignKey(UserSite)
    source_url = models.URLField()
    destination_url = models.URLField()
    time_first = models.DateTimeField(auto_now_add=True)
    time_last = models.DateTimeField(auto_now=True)
    times = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return "%s > %s" % (self.source_url, self.destination_url)
