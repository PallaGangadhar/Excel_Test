from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Test_Excel(models.Model):
    name = models.CharField(max_length=128,null=True,blank=True)
    address = models.CharField(max_length=128,null=True,blank=True)
    visit = models.IntegerField(blank=True)
    status = models.IntegerField(blank=True)

    class Meta:
        verbose_name_plural = 'Test_Excel'
    
    def __str__(self):
        return self.name

