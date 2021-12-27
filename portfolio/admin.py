from django.contrib import admin
from .models import Project, Message

# создаём новый класс для представления сообщений в админке
class MessageAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # list_display = [field.name for field in Message._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    list_display = ('id','name', 'email', 'subject', 'message', 'date') # оставляем только имя и цену товара
    list_filter = ('name', 'email', 'subject', 'message', 'date') # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'email', 'subject') # тут всё очень похоже на фильтры из запросов в базу

# Register your models here.
admin.site.register(Project)
admin.site.register(Message, MessageAdmin)

