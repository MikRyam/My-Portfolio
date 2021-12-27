from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        # получить название поста
        return f'{self.title}. ................ {self.description[:124]} ...'

# Модель Message
class Message(models.Model):
    name = models.CharField(max_length=128, verbose_name="")
    email = models.EmailField(max_length=128, verbose_name="")
    subject = models.CharField(max_length=128, verbose_name="")
    message = models.TextField(max_length=2800, verbose_name="")
    date = models.DateTimeField(auto_now_add=True)
    
    # Метод preview() модели Message, который возвращает начало статьи (предварительный просмотр)
    # длиной 124 символа и добавляет многоточие в конце.
    def preview(self):
        return f'{self.postText[:124]} ...'

    def __str__(self):
        # получить название поста
        return f'{self.name}..... {self.subject}..... {self.date}..... {self.message[:80]} .....'

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000'
    #     # return f'/news/{self.id}'

    
