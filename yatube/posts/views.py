from django.shortcuts import render
from .models import Post


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к
    # меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request):
    # return HttpResponse(f'Посты, отфильтрованные по группам: {slug}')
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {'title': title, }
    return render(request, template, context)
