from django.contrib import admin

# Register your models here.
from delano_bar.core.models import Product, ProductCategory, Event, PromoEvent, Photos


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(PromoEvent)
class PromoEventAdmin(admin.ModelAdmin):
    pass


@admin.register(Photos)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'cover_image', 'created_on')





