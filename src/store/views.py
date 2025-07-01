from django.shortcuts import render
from django.views.generic import DetailView, ListView
from store.models import ItemPromotion, Items
from store.services import get_promotion_items, get_items_details


def main_page(request):
    context = {
        'page_obj': get_promotion_items()
    }
    return render(request, 'store/index.html', context)


def item_details(request, item_slug):
    return render(request, 'store/item_details.html', get_items_details(item_slug))
