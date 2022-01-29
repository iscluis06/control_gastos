from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from control_gastos.models import Cuenta
from control_gastos.serializer import CuentasSerializer
import datetime

class Cuentas(viewsets.ModelViewSet):
    permission_classes =  [permissions.IsAuthenticated]
    serializer_class = CuentasSerializer
    queryset = Cuenta.objects.all()