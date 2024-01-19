# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from incident.models import Incident


# @receiver(post_save, sender=TransactionDetail, dispatch_uid="update_stock_count")
# def update_stock(sender, instance, **kwargs):
#     instance.product.stock -= instance.amount
#     instance.product.save()