from django.contrib.auth.models import User, Group
from rest_framework import serializers
from control_gastos.models import Cuenta

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class CuentasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'