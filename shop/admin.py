from django.contrib import admin
from shop.models import Address, Cart, Order, OrderProducts
# Register your models here.
# class Ord(admin.ModelAdmin):
#     list_display = ("name", "price", "weight", "get_images",)
#     readonly_fields = ("slug",)
#     search_fields = ('name', 'price')
#     list_filter = ('category', 'brand',)
#     list_editable = ("price", "weight",)
#     inlines = (AttributeInline, ImageInline)


class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "add",)

    def user(self, obj):
        return obj.user_id.username


class CategoryAdmin(admin.ModelAdmin):
    pass


class OrderProductsAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ("number",)
    list_display = ("user", "number", "status",)
    list_editable = ("status",)

    def user(self, obj):
        return obj.user_id.username

    # def user
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "":
    #         kwargs["queryset"] = Car.objects.filter(owner=request.user)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Address, AddressAdmin)
admin.site.register(Cart)
admin.site.register(OrderProducts)
admin.site.register(Order, OrderAdmin)
