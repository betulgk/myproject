
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=200)
    post_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    post_content = models.CharField(max_length=280)

    def __str__(self):
        return self.post_name

