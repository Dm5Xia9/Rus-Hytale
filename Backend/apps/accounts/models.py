from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
     beginner = models.BooleanField(default=True)
     avatar = ProcessedImageField(upload_to='userimages/',processors=[ResizeToFill(500, 500)], verbose_name='Изображение', default="userimages/def.png", blank=True)
     identifier = models.CharField('Идентификатор', max_length = 15, null=True, blank=True)
     city = models.CharField('Город', max_length=30, null=True, blank=True)
     telephone = models.CharField('Телефон', max_length=13, null=True, blank=True)
     DateBirth = models.DateField('Дата рождения', null=True, blank=True)
     Points = models.IntegerField('Баллы', default=0)
     messages_count = models.IntegerField('Кол-во сообщений', default=0)
     Description = models.CharField("Описание", max_length=200, default=" ")
     subscribers = models.IntegerField("Подписчики", default=0)
     def __unicode__(self):
          return self.user
     class Meta:
          verbose_name = 'Профиль'
          verbose_name_plural = 'Профили'
from articles.models import tag_base
class tag_interest(models.Model):
     user = models.ForeignKey(User, on_delete = models.CASCADE)
     tag = models.ForeignKey(tag_base, on_delete = models.CASCADE)
class user_interest(models.Model):
     user = models.ForeignKey(User, on_delete = models.CASCADE)
     user_inter = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_i')
class user_post(models.Model):
     user_post = models.ForeignKey(User, on_delete = models.CASCADE)
     content = models.TextField("Пост", default=" ")


