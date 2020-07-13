from django.shortcuts import render


def dashboard(request):
    """Display the wagtail notifications list
    """
    return render(request, 'wagtail_notifications/dashboard.html', {
        "notifications": request.user.notifications.unread()
    })
