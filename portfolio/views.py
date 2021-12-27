from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Project, Message
from blog.models import Blog
from .forms import MessageForm 
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
from decouple import config


# def home(request):
#     projects = Project.objects.all()  # импортируем все записи о проектах из БД
#     return render(request, 'portfolio/home.html', {'projects': projects})

# Обе модели работают в одном представлении:
def home(request):
    blog_1 = Blog.objects.order_by('-date')[0]
    blog_2 = Blog.objects.order_by('-date')[1]
    blog_3 = Blog.objects.order_by('-date')[2]
    projects = Project.objects.all()  # импортируем все записи о проектах из БД
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            message.save()
            name = message.name[:30]
            messages.add_message(request, messages.SUCCESS, f'Thanks {name}! I received your message and will respond shortly...')

            #  отправляем на почту HTML-шаблон:

            # получаем наш html
            html_content = render_to_string('portfolio/message_created.html', {'message': message})
            
            msg = EmailMultiAlternatives(
                subject=f'Message from: {message.name}. - {message.subject} -',
                body=f'Subject: {message.subject}\n \n{message.message}\n \nContact email: {message.email}\nName: {message.name}',  #  это то же, что и message
                from_email=config('from_email'),
                to=[config('recipient_1'), config('recipient_2')], 
            )
            msg.attach_alternative(html_content, "text/html")  # добавляем html

            msg.send()  # отсылаем
            
            return redirect('home')
    else:
        form = MessageForm()

    context_dict = {'projects': projects, 'form': form, 'blog_1': blog_1, 'blog_2': blog_2, 'blog_3': blog_3} 
    return render(request, 'portfolio/home.html', context_dict)


