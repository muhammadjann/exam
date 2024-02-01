from django.contrib import admin

from muhammad.models import Post, UserProfile


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProfile)
class UserPofileAdmin(admin.ModelAdmin):
    pass
