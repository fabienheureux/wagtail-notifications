from django.db import models
from wagtail.core.models import Page
from wagtail.core.signals import page_published
from wagtail_notifications.signals import notify

def notification(sender, instance, **kwargs):
    if instance.owner:
        notify.send(instance, recipient=instance.owner,verb='published')



class HomePage(Page):
    pass


# Register a receiver
page_published.connect(notification)
