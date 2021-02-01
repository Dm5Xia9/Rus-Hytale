from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
class New(models.Model):
     title = models.CharField('Название статьи', max_length = 50)
     text = RichTextUploadingField('Текст статьи')
     date = models.DateTimeField('Дата публикации')