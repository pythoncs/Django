from django.db import models
from django.utils.html import format_html

# Create your models here.
class Article(models.Model):
    atitle = models.CharField(max_length=100)
    acontent = models.TextField()
    aread = models.IntegerField(default=0)
    apub_datetime = models.DateTimeField(auto_now=True)
    aisDelete = models.BooleanField(default=False)
    def Acontent(self):
        return format_html(self.acontent)

