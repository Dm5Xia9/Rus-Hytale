from django.db import models

class new(models.Model):
    new_title = models.CharField('Название новости', max_length=200)
    new_text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата побликации')
    new_img = models.ImageField('Картинка новости 1200x552', upload_to='newimage/')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    def __str__(self):
        return f"{self.new_title}"