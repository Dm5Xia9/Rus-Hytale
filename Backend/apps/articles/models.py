from django.db import models
from accounts.models import User
# Create your models here.
from tinymce.models import HTMLField
from PIL import Image
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
class article(models.Model):
     user = models.ForeignKey(User, on_delete= models.PROTECT)
     title = models.CharField("Название", max_length=100, default=" ")
     cover = models.TextField("Обложка", default=" ")
     content = HTMLField("Контент")
     views = models.IntegerField("Просмотры", default=0)
     likes = models.IntegerField("Лайки", default=0)
     dilikes = models.IntegerField("Дизлайки", default=0)
     DateCreate = models.DateTimeField('Дата публикации',auto_now_add=True, blank=True)
     hidden = models.BooleanField("Скрыто", default=0)
     deleted = models.BooleanField("Удалено", default=0)
     limited = models.BooleanField("Ограничено", default=0)
class tag_base(models.Model):
     title = models.CharField("тег", max_length=40)
     img = ProcessedImageField(upload_to='tagimages/',processors=[ResizeToFill(500, 500)], verbose_name='Изображение', default="tagimages/def.png", blank=True)
     description = models.CharField("Описание", max_length=200, default=" ")
     def __str__(self):
          return f"{self.title}"
class articles_tag(models.Model):
     article = models.ForeignKey(article, on_delete= models.CASCADE)
     tag = models.ForeignKey(tag_base, on_delete= models.CASCADE)
class Like(models.Model):
     user = models.ForeignKey(User, on_delete= models.PROTECT)
     article = models.ForeignKey(article, on_delete= models.CASCADE)
class Delike(models.Model):
     user = models.ForeignKey(User, on_delete= models.PROTECT)
     article = models.ForeignKey(article, on_delete= models.CASCADE)
class article_image(models.Model):
     image = models.ImageField(upload_to='images_articles/')
     def save(self):
          super().save()
          img = Image.open(self.image.path)
          if img.height > 920 or img.width > 920:
               img.thumbnail((920, 920))
               img.save(self.image.path)

class views_article(models.Model):
     user = models.ForeignKey(User, on_delete=models.PROTECT)
     article = models.ForeignKey(article, on_delete=models.CASCADE)
class article_top(models.Model):
     article = models.ForeignKey(article, on_delete=models.CASCADE)
class article_comment(models.Model):
     user = models.ForeignKey(User, on_delete=models.PROTECT)
     article = models.ForeignKey(article, on_delete=models.CASCADE)
     content = models.TextField("Контент", default=" ")
     deleted = models.BooleanField("Удалено", default=0)
