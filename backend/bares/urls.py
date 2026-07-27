from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import BarViewSet


router = DefaultRouter()

router.register(
    r'bares',
    BarViewSet,
    basename='bares'
)


urlpatterns = [
    path('', include(router.urls)),
]