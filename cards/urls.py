from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter() 
router.register('cards', CardViewSet, basename='cards')



urlpatterns = router.urls