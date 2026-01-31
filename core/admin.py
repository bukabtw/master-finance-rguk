from django.contrib import admin
from .models import Application, PageContent

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at', 'user')
    list_filter = ('created_at', 'user')
    search_fields = ('name', 'phone', 'email', 'message')

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'title')
    search_fields = ('key', 'title', 'content')
