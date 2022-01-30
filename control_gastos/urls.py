from django.urls import path
from control_gastos.views_classes.categorias import Categorias
from control_gastos.views_classes.cuentas import Cuentas
from control_gastos.views_classes.detalle_transacciones import DetalleTransacciones
from control_gastos.views_classes.subcategorias import Subcategorias
from control_gastos.views_classes.transacciones import Transacciones

urlpatterns = []

views = [Categorias, Cuentas, DetalleTransacciones, Subcategorias, Transacciones]

for view in views:
    class_name = view.__name__.lower()
    urlpatterns.append(path("{}".format(class_name), view.as_view()))
    urlpatterns.append(path("{}/<int:pk>".format(class_name), view.as_view()))
    urlpatterns.append(path("{}/count/<int:count>".format(class_name), view.as_view()))
