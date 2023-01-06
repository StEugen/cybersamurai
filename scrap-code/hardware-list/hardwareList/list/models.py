from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

class cabinets(models.Model):
    cabinet = models.TextField(unique=True, null=False)
    hard = ArrayField(
        models.TextField(unique=True, null=False)
    )
    hardware_number = ArrayField(
        models.TextField(unique=True, null=False)
    )

    def __str__(self):
        return self.cabinet
    

   