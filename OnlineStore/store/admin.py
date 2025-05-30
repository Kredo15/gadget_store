from django.contrib import admin
from models import Item, Categories, Characteristics, \
    Brands, Models, Review, ItemCharacteristics, Promotion, \
    ItemPromotion

# Register your models here.
admin.site.register(Item)
admin.site.register(Categories)
admin.site.register(Characteristics)
admin.site.register(Brands)
admin.site.register(Models)
admin.site.register(Review)
admin.site.register(ItemCharacteristics)
admin.site.register(Promotion)
admin.site.register(ItemPromotion)
