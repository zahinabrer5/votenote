import uuid
from django.db import models

# Create your models here.

class PollItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    yes = models.IntegerField(default=0, editable=False)
    no = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PollIdAndUserIp(models.Model):
    ref_id = models.CharField(max_length=200, editable=False)
    ip = models.CharField(max_length=200, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ref_id
