from rest_framework import permissions
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.db.models import Model
from rest_framework.serializers import ModelSerializer


class BaseView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self, modelo, serializer, *args, **kwargs):
        self.modelo_actual: Model = modelo
        self.serializer_actual: ModelSerializer = serializer
        super().__init__(**kwargs)

    def get(self, request, pk=None, count=False, limit=None, format=None):
        try:
            if count:
                instancias = self.modelo_actual.objects.all()
                counting = {"count": len(instancias)}
                return JsonResponse(counting, status=status.HTTP_200_OK)
            elif (limit != None):
                instancia = None
                if(limit==0):
                    instancia = self.modelo_actual.objects.all()
                else:
                    instancia = self.modelo_actual.objects.all().order_by('-pk')[:limit]
                serializer = self.serializer_actual(instancia, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif (pk != None):
                instancia = self.modelo_actual.objects.get(pk=pk)
                serializer = self.serializer_actual(instancia)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                instancia = self.modelo_actual.objects.all()
                serializer = self.serializer_actual(instancia, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return JsonResponse({"error": "error {error}".format(error=err)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        context = {"request": request}
        serializer = self.serializer_actual(data=data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        instance = self.modelo_actual.objects.get(pk=pk)
        data = JSONParser().parse(request)
        propiedad_usuario = self._obtenerPropiedadUsuario()
        serializer = self.serializer_actual(instance, data=data)
        if serializer.is_valid() and propiedad_usuario:
            serializer.save(propiedad_usuario=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        try:
            instance = self.modelo_actual.objects.get(pk=pk)
            is_deleted = instance.delete()
            is_deleted = {"is_deleted": bool(is_deleted[0])}
            return JsonResponse(is_deleted, status=status.HTTP_200_OK)
        except Exception as err:
            return JsonResponse({"error": "error {error}".format(error=err)}, status=status.HTTP_400_BAD_REQUEST)

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
            if(len(propeidadesFiltradas)>0):
                return propeidadesFiltradas[0]
            else:
                return None
        except Exception as exception:
            print(exception)
            return None