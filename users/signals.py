from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile

#@receiver(post_save, sender=User)
def createProfileUser(sender, instance, created, **kwargs):
    if created:
        user = instance #user
        profile = Profile()
        profile.user = user
        profile.name = user.first_name
        profile.email = user.email
        profile.username = user.username
        profile.save()

def updateProfile(sender, instance, created, **kwargs):
    if not created:
        profile = instance
        user = profile.user
        user.first_name = profile.name
        user.email = profile.email
        user.username = profile.username
        user.save()

#@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfileUser, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deleteUser, sender = Profile)
