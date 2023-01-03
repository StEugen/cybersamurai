from django.db import models
from django.contrib.postgres.fields import ArrayField

class cabinets(models.Model):
    cabinet = models.TextField(unique=True, null=False)
    hard = ArrayField(
        models.TextField(unique=True, null=False)
    )

   