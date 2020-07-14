"""
This package does not define any custom models.

But in order to register signals based on Wagtail's page workflow, it made
sense to create models.py to define these.
"""
from wagtail.core.signals import page_published
from notifications.signals import notify


def notification(sender, instance, **kwargs):
    """
    In some cases, the page may not have any owner, for example the home page.
    For now we don't send any notification for these page as the logic behind finiding to who send
    a notification is not yet defined
    """
    if instance.owner:
        notify.send(instance, recipient=instance.owner, verb='published')


page_published.connect(notification)
