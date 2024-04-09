from django.http import HttpResponse
from django.core.mail import send_mail


def home(request):
    try:
        send_mail(
            "Subject here",
            "Here is the message.",
            "mailpit_sender@localhost",
            ["mailpit_receiver@localhost"],
            fail_silently=False,
        )
    except Exception as e:
        return HttpResponse("error", e)
    return HttpResponse("Mail sent")
