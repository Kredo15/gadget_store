from django.shortcuts import render
from django.views.generic import DetailView, ListView
from models import ItemPromotion, Items
from services import get_promotion_items, get_items_details

# Create your views here.
class StoreView(ListView):
    model = Items
    # queryset = Products.objects.all().order_by("-id")
    template_name = "store/index.html"
    context_object_name = "items"

    def get_queryset(self):
        return get_promotion_items()


def item_details(request, item_slug):
    return render(request, 'store/item_details.html', get_items_details(item_slug))
