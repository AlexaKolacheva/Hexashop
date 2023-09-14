from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Cart, Order

#
# @receiver(post_save, sender=Cart)
# def create_order(sender, instance, created, **kwargs):
#     if created:
#         Order.objects.create(product=None, customer=instance.user)
#
#         print('Order created')
