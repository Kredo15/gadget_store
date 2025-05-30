from models import ItemPromotion


def get_promotion_items():
    promo_items = ItemPromotion.objects.filter(promotion__is_available=True)
    return promo_items