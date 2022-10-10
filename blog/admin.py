from django.contrib import admin
from .models import Post

#adminに表示されるようにする
admin.site.register(Post)