from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    short_intro =  models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to = 'uploads/users/', null=True, blank=True, default="uploads/users/user-default.png")
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ['created']

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['created']

    def __str__(self):
        return str(self.name)

