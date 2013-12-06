from django.contrib import admin
from .models import UserProfile

# class UserAdmin(admin.ModelAdmin):
    # list_display = ('title', 'views', 'category', 'url')

admin.site.register(UserProfile)
