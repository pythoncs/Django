from django.db import models

# Create your models here.

class AreaInfo(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self',null=True,blank=True)



    class Meta:
        db_table = 'AreaInfo'

class UploadImage(models.Model):
    utitle = models.CharField(max_length=20)
    uhead = models.ImageField(upload_to='areaapp/')

    def __str__(self):
        return self.utitle

