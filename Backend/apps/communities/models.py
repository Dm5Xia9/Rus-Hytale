from django.db import models
from accounts.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
class communiti(models.Model):
     owner = models.ForeignKey(User, on_delete = models.PROTECT)
     ava = ProcessedImageField(upload_to='communitiimages/',processors=[ResizeToFill(500, 500)], verbose_name='Изображение', default="communitiimages/def.png", blank=True)
     title = models.CharField("Название", max_length=100, default=" ")
     Description = models.CharField("Описание", max_length=200, default=" ")
     subscribers = models.IntegerField("Подписчики", default=0)
     rating = models.IntegerField("Рейтинг", default=0)
     identifier = models.CharField('Идентификатор', max_length=15, null=True, blank=True)
     def __str__(self):
          return f"{self.title}"
class tag(models.Model):
     communiti = models.ForeignKey(communiti, on_delete = models.CASCADE)
     title = models.CharField("Название", max_length=50)
     def __str__(self):
          return f"{self.communiti.title}"
class team(models.Model):
     communiti = models.ForeignKey(communiti, on_delete=models.CASCADE)
     User = models.ForeignKey(User, on_delete = models.CASCADE)
     job_title = models.CharField("Название", max_length=80)
class communiti_interest(models.Model):
     user = models.ForeignKey(User, on_delete = models.CASCADE)
     communiti = models.ForeignKey(communiti, on_delete = models.CASCADE)