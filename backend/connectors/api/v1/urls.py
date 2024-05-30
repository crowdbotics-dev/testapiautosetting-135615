from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135615ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135615", Testconnectors135615ViewSet, basename="testconnectors135615"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
