from django.contrib import admin
from blog.models import Post, BgRecord, BlogRoll, Category

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'created_time', 'change_time', 'views']


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(BgRecord)
admin.site.register(BlogRoll)

