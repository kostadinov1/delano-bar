from django.contrib import admin

# Register your models here.
from delano_bar.core.models import Product, ProductCategory, Event, PromoEvent, PhotoGallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(PromoEvent)
class PromoEventAdmin(admin.ModelAdmin):
    pass


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    pass




