from django.db import models

class Post(models.Model):
    #Данные о посте
    title = models.CharField( 'Заголовок записи', max_length=44)
    descriptions = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=40)
    date = models.DateField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='image/%Y', default='image/pass.jpg')
    
    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'