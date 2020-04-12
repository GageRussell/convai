#from django.db import models
from djongo import models
# Create your models here.

class Convai(models.Model):
    email = models.CharField(max_length=255)
    submit_time = models.DateTimeField()

    class Meta:
        db_table = "userEmails"

