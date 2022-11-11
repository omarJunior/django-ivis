from django.contrib import admin

# Register your models here.
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'title',
        'description',
        'featured_image',
        'demo_link',
        'source_link',
        'get_titles',
        'vote_total',
        'vote_ratio',
        'created',
    )
    list_filter = ('owner', 'title',)

    def get_titles(self, request):
        if request.tags:
            tag = ""
            for t in request.tags.all():
                tag += t.name + ","
            return tag[:-1]
        return ""
    get_titles.short_description = "Tags"


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'project',
        'body',
        'value',
        'created',
    )
    list_filter = ('project',)

class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
    )
    list_filter = ('name', )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)