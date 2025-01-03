from django.contrib import admin
from .models import Post,Comment,Contact

# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Contact)
class AdminComment(admin.ModelAdmin):
    list_display = ['name','email','subject']
    list_filter = ['name']
    search_fields = ['name','email']

