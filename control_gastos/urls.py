from django.urls import path, include
from rest_framework import routers
from control_gastos import views
from control_gastos.views_classes.cuentas import Cuentas

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"cuentas", Cuentas)

urlpatterns = [
    path('', include(router.urls))
]