from django.contrib import admin
from .models import Category, Post, Location


class PostModel(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at',
    )

    list_editable = (
        'is_published',
        'category',
        'pub_date',
        'location',
        'author'
    )

    search_fields = ('title',)
    list_filter = ('author', 'category', 'is_published')
    list_display_links = ('title',)


class CategoryModel(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at',
    )
    list_editable = (
        'is_published',
        'slug',
        'description',
    )

    search_fields = ('title',)


class LocationModel(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at',
    )


admin.site.register(Category, CategoryModel)
admin.site.register(Post, PostModel)
admin.site.register(Location, LocationModel)
