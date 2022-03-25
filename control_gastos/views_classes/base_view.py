from typing import List
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions, status
from django.db.models import Model
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from enum import Enum

class TipoComparasion(Enum):
    IGUAL = ""
    PARECIDO = "__contains",
    EN = "__in",
    MAYOR = "__gt",
    MENOR = "__lt",
    MAYORI = "__gte",
    MENORI = "__lte",
    RANGO_FECHAS = '__range'


class ParametroBusqueda():
    def __init__(self, nombre_propiedad: str, nombre_columna: str, tipo_comparacion: TipoComparasion = TipoComparasion.IGUAL):
        self.nombre_propiedad = nombre_propiedad
        self.nombre_columna = nombre_columna
        self.tipo_comparacion = tipo_comparacion


class BaseView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    page_size_query_param = 'page'
    """ Variable usada para remplazar parametros, debe ser sobreescrita en herencia """
    remplazo_de_parametros: List[ParametroBusqueda] = []

    def __init__(self, modelo, serializer, *args, **kwargs):
        self.modelo_actual: Model = modelo
        self.serializer_actual: ModelSerializer = serializer
        super().__init__(*args, **kwargs)

    def create(self, request):
        data = JSONParser().parse(request)
        context = {"request": request}
        serializer = self.serializer_actual(data=data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = self.modelo_actual.objects.all()
        params = self.request.query_params
        if params and self.remplazo_de_parametros:
            llaves = params.keys()
            try:
                for parametro in self.remplazo_de_parametros:
                    if parametro.nombre_propiedad in llaves:
                        queryset = queryset.filter(**{self.construir_filtro(parametro.nombre_columna, parametro.tipo_comparacion): params.get(parametro.nombre_propiedad)})
            except Exception as err:
                print(err)
        return queryset

    def construir_filtro(self, nombre_columna: str, tipo_comparasion: TipoComparasion) -> str:
        filtro = nombre_columna
        if(tipo_comparasion.value is tuple):
            filtro += tipo_comparasion.value[0]
        print(filtro)
        return filtro

    # def post(self, request, format=None):
    #     data = JSONParser().parse(request)
    #     context = {"request": request}
    #     serializer = self.serializer_actual(data=data, context=context)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def put(self, request, pk, format=None):
    #     instance = self.modelo_actual.objects.get(pk=pk)
    #     data = JSONParser().parse(request)
    #     propiedad_usuario = self._obtenerPropiedadUsuario()
    #     serializer = self.serializer_actual(instance, data=data)
    #     if serializer.is_valid() and propiedad_usuario:
    #         serializer.save(propiedad_usuario=request.user)
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    #
    # def delete(self, request, pk, format=None):
    #     try:
    #         instance = self.modelo_actual.objects.get(pk=pk)
    #         is_deleted = instance.delete()
    #         is_deleted = {"is_deleted": bool(is_deleted[0])}
    #         return JsonResponse(is_deleted, status=status.HTTP_200_OK)
    #     except Exception as err:
    #         return JsonResponse({"error": "error {error}".format(error=err)}, status=status.HTTP_400_BAD_REQUEST)

    def _filterFunction(self, variable):
        buscar = 'usuario'
        if (buscar in variable):
            substr = variable[variable.index(buscar):]
            if (substr == buscar):
                return True
            else:
                return False
        else:
            return False

    def _obtenerPropiedadUsuario(self):
        try:
            propeidadesFiltradas = filter(self._filterFunction, dir(self.modelo_actual))
            propeidadesFiltradas = list(propeidadesFiltradas)
            if (len(propeidadesFiltradas) > 0):
                return propeidadesFiltradas[0]
            else:
                return None
        except Exception as exception:
            print(exception)
            return None
