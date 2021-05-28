from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class TablesNews(models.Model):
    photo = models.ImageField(upload_to='Photo', default='')
    title = models.CharField(max_length=1000)
    detail = RichTextField()
    date = models.DateTimeField(auto_now_add=True, blank=False)
    date_updated = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.title