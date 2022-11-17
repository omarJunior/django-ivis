from django.contrib import admin

# Register your models here.
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'title',
        'featured_image',
        'get_tags',
        'vote_total',
        'vote_ratio',
        'created',
    )
    list_filter = ('owner', 'title',)

    def get_tags(self, request):
        if request.tags:
            tag = ""
            for t in request.tags.all():
                tag += t.name + ","
            return tag[:-1]
        return ""
    get_tags.short_description = "Tags"


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'get_owner',
        'project',
        'get_body',
        'value',
        'created',
    )
    list_filter = ('project',)

    def get_owner(self, request):
        if request.owner:
            return f"{request.owner.name}"
        return ""
        
    def get_body(self, request):
        if request.body:
            return f"{request.body.upper()}"
        return ""

    get_owner.short_description = "Full Name"
    get_body.short_description = "Body"

class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
    )
    list_filter = ('name', )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)