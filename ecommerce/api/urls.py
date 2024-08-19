from rest_framework import routers
from .views import AllProductsViewSet, AllBrandsViewSet, AllCategoriesViewSet
router = routers.SimpleRouter()
router.register('products', AllProductsViewSet)
router.register('categories', AllCategoriesViewSet)
router.register('brands', AllBrandsViewSet)
urlpatterns = [

]
urlpatterns += router.urls
