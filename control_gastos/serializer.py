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
    class Meta:
        model = Cuenta
        fields = "__all__"

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = "__all__"

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = "__all__"

class DetalleTransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleTransaccion
        fields = "__all__"