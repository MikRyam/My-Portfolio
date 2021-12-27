from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from django.views.decorators.cache import cache_page # импортируем декоратор для кэширования отдельного представления
 
@cache_page(100) # в аргументы к декоратору передаём количество секунд, которые хотим, чтобы страница держалась в кэше. Внимание! Пока страница находится в кэше, изменения, происходящие на ней, учитываться не будут!
def all_blogs(request):
    blogs_count = Blog.objects.count()  # подсчитывает кол-во постов
    # blogs = Blog.objects.order_by('-date')[:5]  # импортируем все записи о проектах из БД, сортируая их по дате и выводит первые 5 постов
    blogs = Blog.objects.order_by('-date')    
    # paginate_by = 5
    p = Paginator(Blog.objects.order_by('-date'), 5)
    page = request.GET.get('page')
    blogs_list = p.get_page(page)
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'blogs_count':blogs_count, 'blogs_list': blogs_list})

@cache_page(100)
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
