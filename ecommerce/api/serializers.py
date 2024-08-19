from rest_framework import serializers
from ecommerce.models import Product, Attribute, Category, Brand, ProtoType, Image, ProductAttribute


class ImageSerializer(serializers.Serializer):
    src = serializers.ImageField()

    # class Meta:
    #     model = Image
    #     fields = ('src',)


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Brand
        fields = ('name', 'images',)


class CategorySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class ProtoTypeSerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True)
    attributes = AttributeSerializer(many=True)

    class Meta:
        model = ProtoType
        fields = '__all__'


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='attribute.name')

    class Meta:
        model = ProductAttribute
        fields = ('name', 'value',)


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    brand = BrandSerializer()
    # attributes = ProductAttributeValueSerializer(
    #     source='product_attributes', many=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'description', 'images', 'brand', 'weight', 'price',)
