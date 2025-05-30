from django.shortcuts import render

from services import get_promotion_items

# Create your views here.
def store(request):
    return render(request, 'store/main_page.html', get_promotion_items())
