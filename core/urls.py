from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('locode', views.LocodeView, basename='locode')
urlpatterns = router.urls
