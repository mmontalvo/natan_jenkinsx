from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'client', views.ClientViewSet)
router.register(r'trade', views.TradeViewSet)

urlpatterns = [
    path('', include(router.urls))
]