from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import Post, Category
from django.db.models import Q
import datetime as dt


def index(request):
    """Функция возвращает все посты на главной странице"""
    templates = 'blog/index.html'
    posts = Post.objects.filter(
        Q(pub_date__date__lt=dt.datetime.now())
        & Q(is_published=True)
        & Q(category__is_published=True)
    ).order_by('-pub_date')[:5]
    context = {'posts': posts}
    return render(request, templates, context)


def post_detail(request, id):
    """Функция возвращает детализированную информацию поста"""
    templates = 'blog/detail.html'
    post = get_object_or_404(Post, Q(pub_date__date__lt=dt.datetime.now())
                             & (Q(is_published=True)
                             & Q(category__is_published=True)),
                             pk=id)
    context = {'post': post}
    return render(request, templates, context)


def category_posts(request, category_slug):
    """Функция возвращает страницу категории публикации"""
    templates = 'blog/category.html'
    post_list = get_list_or_404(Post.objects.all().filter(
        Q(pub_date__date__lt=dt.datetime.now())
        & Q(is_published=True)
        & Q(category__slug=category_slug)
    ).order_by('-pub_date'))
    category = get_object_or_404(Category, Q(slug=category_slug)
                                 & Q(is_published=True))
    context = {'category': category, 'post_list': post_list}
    return render(request, templates, context)
