from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(mail, text):
    send_mail('Reminder', text, 'admin_email@somecompany.com', [mail])
