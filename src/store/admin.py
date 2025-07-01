from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from store.models import Items, Categories, Characteristics, \
    Brands, Models, Review, ItemCharacteristics, Promotion, \
    ItemPromotion


@admin.register(Categories)
class CategoriesAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Items)
admin.site.register(Characteristics)
admin.site.register(Brands)
admin.site.register(Models)
admin.site.register(Review)
admin.site.register(ItemCharacteristics)
admin.site.register(Promotion)
admin.site.register(ItemPromotion)
