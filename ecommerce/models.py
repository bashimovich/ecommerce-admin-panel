from django.db import models
from django.utils.html import mark_safe
# from django.utils.text import slugify
from slugify import slugify
# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import Func


class Image(models.Model):
    src = models.ImageField(upload_to="images")
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def img_preview(self):
        return mark_safe(f'<img src="{self.src.url}" width=70 height=70>')


class Attribute(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name='values')

    def __str__(self):
        return self.value


class Brand(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    images = GenericRelation('Image', blank=True, null=True)

    def __str__(self):
        return self.name


class ProtoType(models.Model):
    name = models.CharField(max_length=255, blank=True, default='Null')
    attributes = models.ManyToManyField(
        Attribute, related_name='prototypes')
    brands = models.ManyToManyField(
        Brand, related_name='prototypes')

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=255, blank=True, default='Null')
    images = GenericRelation('Image', blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(default='true')
    description = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, default='Null')
    images = GenericRelation('Image', blank=True, null=True)
    prototype = models.ForeignKey(
        ProtoType, on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    attributes = models.ManyToManyField(
        Attribute, through='ProductAttribute',  related_name='products')

    requires_shipping = models.BooleanField(default=False)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductAttribute(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_attributes')
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name='product_attributes')
    value = models.CharField(max_length=255, blank=True)


class Variant(models.Model):
    images = models.ManyToManyField(
        Image, related_name='variants')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='variants')
