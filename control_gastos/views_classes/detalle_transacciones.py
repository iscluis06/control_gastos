from control_gastos.models import DetalleTransaccion
from control_gastos.serializer import DetalleTransaccionSerializer
from control_gastos.views_classes.base_view import BaseView, ParametroBusqueda, TipoComparasion


class DetalleTransacciones(BaseView):
    queryset = DetalleTransaccion.objects.all()
    serializer_class = DetalleTransaccionSerializer
    remplazo_de_parametros = [
        ParametroBusqueda(nombre_propiedad="detalleTransaccion",
                          nombre_columna="detalle_transaccion_transaccion__detalle_trasanccion_id",
                          tipo_comparacion=TipoComparasion.IGUAL),
        ParametroBusqueda(nombre_propiedad="detalleTransaccionNombre",
                          nombre_columna="detalle_transaccion_nombre",
                          tipo_comparacion=TipoComparasion.PARECIDO),
        ParametroBusqueda(nombre_propiedad="detalleTransaccionDescripcion",
                          nombre_columna="detalle_transaccion_descripcion",
                          tipo_comparacion=TipoComparasion.PARECIDO),
        ParametroBusqueda(nombre_propiedad="detalleTransaccionUsuario",
                          nombre_columna="detalle_transaccion_usuario__username",
                          tipo_comparacion=TipoComparasion.IGUAL)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(DetalleTransaccion, DetalleTransaccionSerializer, *args, **kwargs)