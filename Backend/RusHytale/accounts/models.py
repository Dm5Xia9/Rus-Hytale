from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     avatar = models.ImageField(upload_to='userimages/', verbose_name='Изображение')
     identifier = models.CharField('Идентификатор', max_length = 15, null=True, blank=True)
     city = models.CharField('Город', max_length=30, null=True, blank=True)
     telephone = models.CharField('Телефон', max_length=13, null=True, blank=True)
     DateBirth = models.DateField('Дата рождения', null=True, blank=True)
     def __unicode__(self):
          return self.user

     class Meta:
          verbose_name = 'Профиль'
          verbose_name_plural = 'Профили'