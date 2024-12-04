from django.contrib import admin

from homepage.models import Service, Ideas, ProcessStep


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions')
    search_fields = ('title',)


@admin.register(Ideas)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')
    search_fields = ('name',)


@admin.register(ProcessStep)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions')
    search_fields = ('title',)
