from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.first_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
