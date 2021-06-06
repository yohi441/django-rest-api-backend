from django.contrib import admin
from django.contrib.auth import models
from blog import models



@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title', ), }


admin.site.register(models.Category)
