from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_welcome_email(sender, instance, created, **kwargs):
    if not created:
        return

    send_mail(
        subject="Welcome!",
        message=f"Welcome, {instance.email}!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[instance.email],
    )
