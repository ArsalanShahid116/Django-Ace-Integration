from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

class Code(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='coder_code')
   
    def get_absolute_url(self):
        return reverse('coder:code_detail', kwargs={"id": self.id})
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
