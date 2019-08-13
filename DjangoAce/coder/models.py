from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Code(models.Model):
    title = models.CharField(max_length=250)
    program = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
