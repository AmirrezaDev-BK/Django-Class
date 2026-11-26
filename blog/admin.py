from django.contrib import admin

from .models import Post, Comment, Post_Image

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content')
    search_fields = ('author',)


class Post_ImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'author', 'created_at')
    search_fields = ('author',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post_Image, Post_ImageAdmin)
