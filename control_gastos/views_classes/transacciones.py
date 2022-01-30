from control_gastos.models import Transaccion
from control_gastos.serializer import TransaccionSerializer
from control_gastos.views_classes.base_view import BaseView


class Transacciones(BaseView):

    def __init__(self):
        super().__init__(Transaccion, TransaccionSerializer)