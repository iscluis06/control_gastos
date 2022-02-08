from django.contrib.auth.models import User, Group
from rest_framework import serializers
from control_gastos.models import Cuenta, Categoria, Subcategoria, Transaccion, DetalleTransaccion


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class CuentasSerializer(serializers.ModelSerializer):
    #Primer forma de relacionar tablas
    #cuenta_usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    cuenta_usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    nombre_usuario = serializers.CharField(required=False, source='cuenta_usuario.username')
    class Meta:
        model = Cuenta
        fields = "__all__"

class CategoriaSerializer(serializers.ModelSerializer):
    categoria_usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    nombre_usuario = serializers.CharField(required=False, source='categoria_usuario.username')
    class Meta:
        model = Categoria
        fields = "__all__"

class SubcategoriaSerializer(serializers.ModelSerializer):
    subcategoria_usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    subcategoria_categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    nombre_usuario = serializers.CharField(required=False, source='subcategoria_usuario.username')
    nombre_categoria = serializers.CharField(required=False, source='subcategoria_categoria.categoria_nombre')
    class Meta:
        model = Subcategoria
        fields = "__all__"

class TransaccionSerializer(serializers.ModelSerializer):
    transaccion_usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    transaccion_subcategoria = serializers.PrimaryKeyRelatedField(queryset=Subcategoria.objects.all())
    transaccion_cuenta = serializers.PrimaryKeyRelatedField(queryset=Cuenta.objects.all())
    nombre_usuario = serializers.CharField(required=False, source='transaccion_usuario.username')
    nombre_cuenta = serializers.CharField(required=False, source='transaccion_cuenta.cuenta_nombre')
    nombre_subcategoria = serializers.CharField(required=False, source='transaccion_subcategoria.subcategoria_nombre')
    class Meta:
        model = Transaccion
        fields = "__all__"

class DetalleTransaccionSerializer(serializers.ModelSerializer):
    detalle_transaccion_usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())
    detalle_transaccion_transaccion = serializers.PrimaryKeyRelatedField(queryset=Transaccion.objects.all())
    nombre_usuario = serializers.CharField(required=False, source='detalle_transaccion_usuario.username')
    class Meta:
        model = DetalleTransaccion
        fields = "__all__"