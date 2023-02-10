from django.shortcuts import get_object_or_404, render
from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
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


def group_posts(request, slug):
    # return HttpResponse(f'Посты, отфильтрованные по группам: {slug}')
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    # title = f'Yatube {group.title} posts'
    title = 'Записи сообщества'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }

    return render(request, template, context)
