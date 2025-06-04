from models import ItemPromotion, Items
from django.shortcuts import get_object_or_404


def get_promotion_items():
    promo_items = ItemPromotion.objects.filter(promotion__is_available=True)
    return promo_items


def get_items_details(item_slug: str) -> dict:
    item = get_object_or_404(Items, slug=item_slug)
    context = {
        'item': item,
    }
    return context