from django.contrib import admin
from .models import *


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'last_name',
        'email',
        'username',
        'location',
        'short_intro',
        'profile_image',
        'created',
    )
    list_filter = ('user', 'last_name',)

class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'name',
        'created',
    )
    search_fields = ('name',)
    list_filter = ('owner', 'name',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
