from control_gastos.models import Cuenta
from control_gastos.serializer import CuentasSerializer
from control_gastos.views_classes.base_view import BaseView


class Cuentas(BaseView):
    def __init__(self):
        super().__init__(Cuenta, CuentasSerializer)
