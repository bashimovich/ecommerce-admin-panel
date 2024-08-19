from django.utils.html import format_html, mark_safe, format_html_join
from mptt.admin import TreeRelatedFieldListFilter
from django.contrib import admin
from ecommerce.models import *
from mptt.admin import DraggableMPTTAdmin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline


class ImageInline(GenericStackedInline):
    model = Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ["img_preview"]


class AttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "weight", "get_images",)
    readonly_fields = ("slug",)
    search_fields = ('name', 'price')
    list_filter = ('category', 'brand',)
    list_editable = ("price", "weight",)
    inlines = (AttributeInline, ImageInline)

    def get_images(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images.all()))


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ("name",)
    list_display_links = ('name',)
    inlines = (ImageInline,)


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "get_images",)
    inlines = (ImageInline,)

    def get_images(self, obj):
        return format_html_join('\n', '<img src="/media/{}" width=60px height=60px>', ((i.src,) for i in obj.images.all()))


class AttributeAdmin(admin.ModelAdmin):
    inlines = (AttributeInline,)


# class CategoryDraggableMPTTAdmin(DraggableMPTTAdmin):
#     list_display = ('name',)
#     mptt_level_indent = 20

#     # list_display_links = ('indented_name',)

#     def name(self, instance):
#         return format_html(
#             '<div style="text-indent:{}px">{}</div>',
#             instance._mpttfield('level') * self.mptt_level_indent,
#             instance.name,  # Or whatever you want to put here
#         )
    # name.short_description = ('name nice')


admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(AttributeValue)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ProtoType)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Variant)
