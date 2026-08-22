from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Product


@receiver(pre_save, sender=Product)
def auto_generate_product_slug(sender, instance, **kwargs):
    """
    სიგნალი: პროდუქტის შენახვამდე (pre_save) ავტომატურად
    აგენერირებს უნიკალურ slug-ს პროდუქტის სახელიდან.
    """
    if not instance.slug:
        base_slug = slugify(instance.name)
        if not base_slug:
            base_slug = f"product-{instance.pk or 'item'}"

        slug = base_slug
        counter = 1
        # შევამოწმოთ უნიკალურობა
        while Product.objects.filter(slug=slug).exclude(pk=instance.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        instance.slug = slug
