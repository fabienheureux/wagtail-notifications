import notifications.urls
from django.urls import path, include

urlpatterns = [
    path('inbox/notifications/',
         include(notifications.urls, namespace='notifications')),
]
