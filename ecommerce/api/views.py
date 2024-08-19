from rest_framework import viewsets
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer
from ecommerce.models import Product, Brand, Category
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, BaseFilterBackend
from slugify import slugify


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    brand = filters.BaseInFilter(field_name='brand', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['category']

# custom search
# class ProductSearchFilter(BaseFilterBackend):
#     def filter_queryset(self, request, queryset, view):
#         if request.query_params.get('search', False):
#             q = slugify(request.query_params.get('search', False))
#             return Product.objects.filter(slug__trigram_similar=q)


class AllProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = (filters.DjangoFilterBackend, ProductSearchFilter) #Custom Search
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = ProductFilter
    search_fields = ['slug']


class AllBrandsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class AllCategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
