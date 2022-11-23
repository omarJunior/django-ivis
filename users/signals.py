from django.contrib.auth.models import User
from django.contrib.auth.signals import (
    user_login_failed,
    user_logged_in, 
    user_logged_out
    )
from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings

from .models import Profile

def do_login_failed(sender, credentials: dict, request=None, **kwargs):
    print("Logging failed")

def do_login(sender, user, request, **kwargs):
    print("logging succesfully", user)

def do_logout(sender, user, request, **kwargs):
    print('logout, bye', user)

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


user_login_failed.connect(do_login_failed)
user_logged_in.connect(do_login)
user_logged_out.connect(do_logout)
post_save.connect(createProfileUser, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deleteUser, sender = Profile)
