from django.contrib import admin
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin
from .models import Comment,    Blog,likes

class LikesInline(SuperInlineModelAdmin,admin.TabularInline):
    model =likes
    extra = 1

class CommentInline(SuperInlineModelAdmin,admin.StackedInline):
    model = Comment
    extra = 1
    

class BlogAdmin(SuperModelAdmin):
    model = Blog
    inlines = (CommentInline,LikesInline)
admin.site.register(Comment)
admin.site.register(Blog,BlogAdmin)
admin.site.register(likes)
