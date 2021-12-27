from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    text = models.TextField()

    def __str__(self):
        # получить название поста
        return f'{self.title}. ................ {self.text[:124]} ...'
    
    # date = models.DateField(auto_now_add=True)