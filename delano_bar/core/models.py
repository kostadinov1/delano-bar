from django.core.validators import MinLengthValidator
from django.db import models


class Event(models.Model):
    TITLE_MAX_LEN = 100
    GUEST_MAX_LEN = 100

    title = models.CharField(max_length=TITLE_MAX_LEN, null=False, blank=False,
                             validators=(MinLengthValidator,))
    guest = models.CharField(max_length=GUEST_MAX_LEN, null=True, blank=True)
    description = models.TextField(null=False, blank=False,
                                   validators=(MinLengthValidator,))
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    image_url = models.URLField()


class PromoEvent(models.Model):
    NAME_MAX_LEN = 50

    name = models.CharField(max_length=NAME_MAX_LEN, blank=False, null=False,
                            validators=(MinLengthValidator,))
    description = models.TextField(null=False, blank=False,
                                   validators=(MinLengthValidator,))
    start_date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    image_url = models.URLField()


class ProductCategory(models.Model):
    NAME_MAX_LEN = 50

    name = models.CharField(max_length=NAME_MAX_LEN, null=False, blank=False,
                            validators=(MinLengthValidator,))
    description = models.TextField(null=False, blank=False,
                                   validators=(MinLengthValidator,))

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    NAME_MAX_LEN = 100

    name = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=False,
                            validators=(MinLengthValidator,))
    price = models.IntegerField(null=False, blank=False,)
    description = models.TextField(null=False, blank=False,
                                   validators=(MinLengthValidator,))
    image_url = models.URLField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=False, blank=False)


class PhotoGallery(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(max_length=TITLE_MAX_LEN, null=False, blank=False,
                             validators=(MinLengthValidator,))
    image_local = models.ImageField(null=True, blank=True, upload_to='photo_images_gallery')
    image_url = models.URLField(null=True, blank=True,)



