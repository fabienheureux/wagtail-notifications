from django.utils.translation import ugettext_lazy as _

try:
    from wagtail.core import hooks
    from wagtail.admin.menu import MenuItem
except ImportError:  # fallback for Wagtail <2.0
    from wagtail.wagtailcore import hooks
    from wagtail.wagtailadmin.menu import MenuItem

try:
    from django.urls import re_path, include
except ImportError:  # fallback for Django <2.0
    from django.conf.urls import url as re_path
    from django.conf.urls import include

try:
    from django.urls import reverse
except ImportError:  # fallback for Django <1.9
    from django.core.urlresolvers import reverse

from . import urls
from . import views


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^notifications/', include(urls)),
    ]


class NotificationsAwareAdminMenuItem(MenuItem):
    def get_context(self, request):
        """
        Override get_context function in order to get unread status for the current user
        """
        context = super().get_context(request)
        icon = "icon icon-radio-empty"
        if (request.user.notifications.unread()):
            icon = "icon icon-radio-full"

        context["classnames"] = "{} {}".format(context["classnames"], icon)
        return context


@hooks.register('register_admin_menu_item')
def register_wagtail_notifications_menu_items():
    return NotificationsAwareAdminMenuItem(_('Notifications'), reverse('wagtail_notifications'), order=10000)
