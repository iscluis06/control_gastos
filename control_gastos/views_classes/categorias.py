from control_gastos.models import Categoria
from control_gastos.serializer import CategoriaSerializer
from control_gastos.views_classes.base_view import BaseView


class Categorias(BaseView):

    def __init__(self):
        super().__init__(Categoria, CategoriaSerializer)
