# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Category, Size, Price


@receiver(post_save, sender=Category)
def create_price_for_new_category(sender, instance, created, **kwargs):
    if created:
        sizes = Size.objects.all()
        for size in sizes:
            Price.objects.create(category=instance, size=size, price=0.0)


@receiver(post_save, sender=Size)
def create_price_for_new_size(sender, instance, created, **kwargs):
    if created:
        categories = Category.objects.all()
        for category in categories:
            Price.objects.create(category=category, size=instance, price=0.0)
