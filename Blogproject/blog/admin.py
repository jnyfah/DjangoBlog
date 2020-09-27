from django.contrib import admin

from.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'published',)
    list_filter = ('created', 'published', 'author',)
    search_fields = ('title', 'body',)
    raw_id_fields = ('author',)
    date_hierarchy='published'
    ordering = ('published',)

