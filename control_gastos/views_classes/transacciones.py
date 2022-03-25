from control_gastos.models import Transaccion
from control_gastos.serializer import TransaccionSerializer
from control_gastos.views_classes.base_view import BaseView, ParametroBusqueda, TipoComparasion


class Transacciones(BaseView):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer
    remplazo_de_parametros = [
        ParametroBusqueda(nombre_propiedad="transaccionSubcategoria",
                          nombre_columna="transaccion_subcategoria__subcategoria_nombre",
                          tipo_comparacion=TipoComparasion.IGUAL),
        ParametroBusqueda(nombre_propiedad="transaccionCuenta",
                          nombre_columna="transaccion_cuenta__cuenta_nombre",
                          tipo_comparacion=TipoComparasion.IGUAL),
        ParametroBusqueda(nombre_propiedad="transaccionCantidad",
                          nombre_columna="transaccion_cantidad",
                          tipo_comparacion=TipoComparasion.IGUAL),
        ParametroBusqueda(nombre_propiedad="transaccionUsuario",
                          nombre_columna="transaccion_usuario__username",
                          tipo_comparacion=TipoComparasion.IGUAL)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(Transaccion, TransaccionSerializer, *args, **kwargs)