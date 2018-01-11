from django.db import models

# Create your models here.
class Repo(models.Model):

    STATUS_ACTIVE = 'active'
    STATUS_ERROR = 'error'

    path = models.CharField(max_length=256)
    details = models.TextField()
    status = models.CharField(max_length=128, default=STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
