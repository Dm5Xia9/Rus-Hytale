from django.db import models

class New(models.Model):
     title = models.CharField('Название статьи', max_length = 50)
     text = models.TextField('Текст статьи')
     date = models.DateTimeField('Дата публикации')