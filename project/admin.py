from django.contrib import admin
from .models import *



admin.site.register(Category)
admin.site.register(Updateimage)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'create_at')
    search_fields = ('title', )
    readonly_fields = (
        'create_at', 'update_at'
    )

