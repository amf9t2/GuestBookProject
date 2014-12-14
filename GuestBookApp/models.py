from django.db import models

# Create your models here.
from django.db import models

class Guests(models.Model):
    last_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name