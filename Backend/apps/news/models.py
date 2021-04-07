from django.db import models
from communities.models import communiti
from tinymce.models import HTMLField
from accounts.models import User
from PIL import Image
class New(models.Model):
     communiti = models.ForeignKey(communiti, on_delete=models.CASCADE)
     title = models.CharField('Название статьи', max_length=100)
     text_mini = models.TextField('Краткий текст статьи', default=' ')
     text = HTMLField("Контент")
     views = models.IntegerField("Просмотры", default=0)
     likes = models.IntegerField("Лайки", default=0)
     dilikes = models.IntegerField("Дизлайки", default=0)
     DateCreate = models.DateTimeField('Дата публикации', blank=True,auto_now_add=True)

     class Meta:
          verbose_name = 'Новость'
          verbose_name_plural = 'Новости'

     def __str__(self):
          return f"{self.title}"
class Like_new(models.Model):
     user = models.ForeignKey(User, on_delete= models.PROTECT)
     new = models.ForeignKey(New, on_delete= models.CASCADE)
class Delike_new(models.Model):
     user = models.ForeignKey(User, on_delete= models.PROTECT)
     new = models.ForeignKey(New, on_delete= models.CASCADE)
class views_new(models.Model):
     user = models.ForeignKey(User, on_delete=models.PROTECT)
     new = models.ForeignKey(New, on_delete=models.CASCADE)
class new_image(models.Model):
     image = models.ImageField(upload_to='images_news/')
     def save(self):
          super().save()
          img = Image.open(self.image.path)
          if img.height > 920 or img.width > 920:
               img.thumbnail((920, 920))
               img.save(self.image.path)
