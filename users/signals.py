from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance #user
        profile = Profile()
        profile.user = user
        profile.name = user.first_name
        profile.email = user.email
        profile.username = user.username
        profile.save()
    else:
        #si se actualizara
        profile = Profile.objects.get(user = instance)
        if instance.first_name:
            profile.name = instance.first_name
        if instance.email:
            profile.email = instance.email
        profile.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('Deleting user...')

#post_save.connect(createProfile, sender=User)
#post_delete.connect(deleteUser, sender = Profile)
