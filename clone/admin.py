from django.contrib import admin
from .models import *
from clone.models import Profile, Comment, Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)