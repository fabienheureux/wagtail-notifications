"""
This package does not define any custom models.

But in order to register signals based on Wagtail's page workflow, it made
sense to create models.py to define these.
"""
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from wagtail.admin.auth import users_with_page_permission
from wagtail.core.models import PageRevision
from wagtail.core.signals import page_published
from .signals import notify
from notifications.models import Notification


def notify_after_page_published(sender, instance, **kwargs):
    """
    In some cases, the page may not have any owner, for example the home page.
    For now we don't send any notification for these page as the logic behind finiding to who send
    a notification is not yet defined
    """
    if instance.owner:
        notify.send(instance, recipient=instance.owner, verb='published')


@receiver(post_save, sender=PageRevision)
def notify_after_revision_save(sender, instance, **kwargs):
    if not instance.submitted_for_moderation:
        return

    # Get list of publishers
    include_superusers = getattr(
        settings, 'WAGTAILADMIN_NOTIFICATION_INCLUDE_SUPERUSERS', True)
    recipients = users_with_page_permission(
        instance.page, 'publish', include_superusers)

    for recipient in recipients:
        notify.send(instance.page, recipient=recipient, verb='submitted')


page_published.connect(notify_after_page_published)
