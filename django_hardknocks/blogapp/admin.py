from django.contrib import admin
from .models import BlogPage,Tags,Post,Comment,Pcategory
# Register your models here.
admin.site.register(BlogPage)
admin.site.register(Tags)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Pcategory)