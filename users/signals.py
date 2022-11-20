from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings

from .models import Profile

#@receiver(post_save, sender=User)
def createProfileUser(sender, instance, created, **kwargs):
    if created:
        user = instance #user
        profile = Profile()
        profile.user = user
        profile.name = user.first_name
        profile.last_name = user.last_name
        profile.email = user.email
        profile.username = user.username
        profile.save()  
        subject = "Profile created succesfully!"
        message = f"Hello, welcome {profile.user}"
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [f'{profile.email}'],
                fail_silently = False,
            )
        except:
            print("No tiene email")
            pass


#@receiver(post_save, sender=Profile)
def updateProfile(sender, instance, created, **kwargs):
    if not created:
        profile = instance
        user = profile.user
        user.first_name = profile.name
        user.last_name = profile.last_name
        user.email = profile.email
        user.username = profile.username
        user.save()

#@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    if user is not None:
        user.delete()

post_save.connect(createProfileUser, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deleteUser, sender = Profile)
