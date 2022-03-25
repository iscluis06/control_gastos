from django.urls import path
from rest_framework import routers

from control_gastos.views_classes.balance import Balance
from control_gastos.views_classes.categorias import Categorias
from control_gastos.views_classes.cuentas import Cuentas
from control_gastos.views_classes.detalle_transacciones import DetalleTransacciones
from control_gastos.views_classes.subcategorias import Subcategorias
from control_gastos.views_classes.transacciones import Transacciones

urlpatterns = []

views = [Categorias, Cuentas, DetalleTransacciones, Subcategorias, Transacciones]
router = routers.DefaultRouter(trailing_slash=False)

for view in views:
    class_name = view.__name__.lower()
    router.register(class_name, view)

urlpatterns.append(path("balance", Balance.as_view()))
urlpatterns += router.urls
