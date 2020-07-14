from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Notification


class NotificationAdmin(ModelAdmin):
    model = Notification
    menu_label = "Notifications"
    menu_icon = "radio-empty"


modeladmin_register(NotificationAdmin)
