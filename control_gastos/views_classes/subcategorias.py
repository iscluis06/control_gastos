from control_gastos.models import Subcategoria
from control_gastos.serializer import SubcategoriaSerializer
from control_gastos.views_classes.base_view import BaseView, ParametroBusqueda, TipoComparasion


class Subcategorias(BaseView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer
    remplazo_de_parametros = [
        ParametroBusqueda(nombre_propiedad="subcategoriaCategoria",
                          nombre_columna="subcategoria_categoria__categoria_nombre",
                          tipo_comparacion=TipoComparasion.PARECIDO),
        ParametroBusqueda(nombre_propiedad="subcategoriaNombre",
                          nombre_columna="subcategoria_nombre",
                          tipo_comparacion=TipoComparasion.PARECIDO),
        ParametroBusqueda(nombre_propiedad="subcategoriaUsuario",
                          nombre_columna="subcategoria_usuario__username",
                          tipo_comparacion=TipoComparasion.IGUAL)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(Subcategoria, SubcategoriaSerializer, *args, **kwargs)