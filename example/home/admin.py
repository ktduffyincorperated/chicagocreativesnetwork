from django.contrib import admin
from .models import Post, Comment, Image

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    list_filter = ('title', 'created_on')
    search_fields = ('title',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'body', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('author', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'post')


    def approve_comment(self, request, queryset):
        queryset.update(active=True)

