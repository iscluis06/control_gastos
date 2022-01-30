from control_gastos.models import DetalleTransaccion
from control_gastos.serializer import DetalleTransaccionSerializer
from control_gastos.views_classes.base_view import BaseView


class DetalleTransacciones(BaseView):

    def __init__(self):
        super().__init__(DetalleTransaccion, DetalleTransaccionSerializer)