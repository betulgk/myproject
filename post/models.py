from django.db import models

class post(models.Model):
    author = models.CharField(max_length=200)
    post_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


