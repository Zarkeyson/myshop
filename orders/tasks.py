from email.mime import message
from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Zadatak da posalje email notifikaciju kada je narudzbina uspesno kreirana
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order_id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'You have successfull placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'djurdjev.zarko@gmail.com', [order.mail])
    return mail_sent