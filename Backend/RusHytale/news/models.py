from django.db import models
class New(models.Model):
     title = models.CharField('Название статьи', max_length = 50)
     text = models.TextField('Текст статьи')
     date = models.DateTimeField('Дата публикации')
     new_img = models.ImageField('Картинка новости 1200x552', upload_to='newimage/', default='1')
     class Meta:
          verbose_name = 'Новость'
          verbose_name_plural = 'Новости'

     def __str__(self):
          return f"{self.title}"