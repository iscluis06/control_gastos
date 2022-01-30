from control_gastos.models import Subcategoria
from control_gastos.serializer import SubcategoriaSerializer
from control_gastos.views_classes.base_view import BaseView


class Subcategorias(BaseView):

    def __init__(self):
        super().__init__(Subcategoria, SubcategoriaSerializer)