from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Status)
def create_status(sender, instance, created, **kwargs):
    if created:
        TheStatus.objects.create(status=instance)

@receiver(post_save, sender=Status)
def save_status(sender, instance, **kwargs):
    instance.theStatus.save()

@receiver(post_save, sender=Role)
def create_role(sender, instance, created, **kwargs):
    if created:
        TheRole.objects.create(role=instance)

@receiver(post_save, sender=Role)
def save_role(sender, instance, **kwargs):
    instance.theRole.save()