import notifications.urls
from django.urls import path, include
from .views import dashboard

urlpatterns = [
    path('inbox/notifications/',
         include(notifications.urls, namespace='notifications')),
    path('notifications/', dashboard, name="wagtail_notifications"),
]
