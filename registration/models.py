from django.contrib.auth.models import User
from django.db.models.signals import post_save
from user_profile.models import Profile


def create_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return
    Profile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)
