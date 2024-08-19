from rest_framework import routers
from .views import UsersViewset
router = routers.SimpleRouter()
router.register('users', UsersViewset)
urlpatterns = [

]
urlpatterns += router.urls
