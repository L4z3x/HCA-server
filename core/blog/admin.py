from django.contrib import admin
from blog.models import Blog, Comment, Like

admin.site.register(Like)
admin.site.register(Blog)
admin.site.register(Comment)
