from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Q
from django.utils import timezone

from blog.models import Post, Category


def time_pub():
    """Функция возвращает проверку времени и флага публикации"""
    return Q(pub_date__date__lt=timezone.now()) & Q(is_published=True)


def index(request):
    """Функция возвращает все посты на главной странице"""
    templates = 'blog/index.html'
    posts = Post.objects.select_related('author').all().filter(
        Q(time_pub()) & Q(category__is_published=True))[:5]
    context = {'posts': posts}
    return render(request, templates, context)


def post_detail(request, id):
    """Функция возвращает детализированную информацию поста"""
    templates = 'blog/detail.html'
    post = get_object_or_404(Post, time_pub(), category__is_published=True,
                             pk=id)
    context = {'post': post}
    return render(request, templates, context)


def category_posts(request, category_slug):
    """Функция возвращает страницу категории публикации"""
    templates = 'blog/category.html'
    post_list = get_list_or_404(Post, time_pub()
                                & Q(category__slug=category_slug))
    category = get_object_or_404(Category, Q(slug=category_slug)
                                 & Q(is_published=True))
    context = {'category': category, 'post_list': post_list}
    return render(request, templates, context)
