from control_gastos.models import Cuenta
from control_gastos.serializer import CuentasSerializer
from control_gastos.views_classes.base_view import BaseView, ParametroBusqueda, TipoComparasion


class Cuentas(BaseView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentasSerializer
    remplazo_de_parametros = [
        ParametroBusqueda(nombre_propiedad="cuentaNombre",
                          nombre_columna="cuenta_nombre",
                          tipo_comparacion=TipoComparasion.PARECIDO),
        ParametroBusqueda(nombre_propiedad="cuentaMonto",
                          nombre_columna="cuenta_monto",
                          tipo_comparacion=TipoComparasion.IGUAL),
        ParametroBusqueda(nombre_propiedad="cuentaDeuda",
                          nombre_columna="cuenta_deuda",
                          tipo_comparacion=TipoComparasion.IGUAL),
        ParametroBusqueda(nombre_propiedad="cuentaUsuario",
                          nombre_columna="cuenta_usuario__username",
                          tipo_comparacion=TipoComparasion.IGUAL),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(Cuenta, CuentasSerializer, *args, **kwargs)
