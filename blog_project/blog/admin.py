# blog/admin.py

from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)} # Auto-fills slug from title

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)