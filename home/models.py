from tabnanny import verbose
from django.db import models
from datetime import datetime
# Create your models here.



class Data(models.Model):
    name = models.CharField("نام و نام خانوادگی", max_length=100)
    title = models.CharField('عنوان', max_length=100)
    phone_number = models.CharField('شماره تماس', max_length=200 , unique=True)
    created_at = models.FloatField(default=datetime.now().timestamp())
    email = models.CharField('ایمیل', null=True, max_length=200, blank=False)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        