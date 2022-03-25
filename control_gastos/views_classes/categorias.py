from control_gastos.models import Categoria
from control_gastos.serializer import CategoriaSerializer
from control_gastos.views_classes.base_view import BaseView, ParametroBusqueda, TipoComparasion


class Categorias(BaseView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    remplazo_de_parametros = [
        ParametroBusqueda(nombre_propiedad="categoriaNombre", nombre_columna="categoria_nombre",
                          tipo_comparacion=TipoComparasion.PARECIDO),
        ParametroBusqueda(nombre_propiedad="categoriaUsuario", nombre_columna="categoria_usuario__username",
                          tipo_comparacion=TipoComparasion.IGUAL)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(Categoria, CategoriaSerializer, *args, **kwargs)
