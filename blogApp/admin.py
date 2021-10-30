from django.contrib import admin
from .models import User, Post, Likes, Comments, PostViews

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(PostViews)

