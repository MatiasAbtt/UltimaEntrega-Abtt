from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    content = CKEditor5Field(config_name='default')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pages/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title