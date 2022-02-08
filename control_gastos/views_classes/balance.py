from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.views import APIView

from control_gastos.models import Cuenta


class Balance(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cuentas_activas = Cuenta.objects.filter(cuenta_tipo='A')
        cuentas_activas_cargo = 0
        cuentas_activas_abono = 0
        for cuenta in cuentas_activas:
            cuentas_activas_cargo += cuenta.cuenta_debe
            cuentas_activas_abono += cuenta.cuenta_haber
        cuentas_activas_total = cuentas_activas_abono + cuentas_activas_cargo
        cuentas_pasivo = Cuenta.objects.filter(cuenta_tipo='P')
        cuentas_pasivo_cargo = 0
        cuentas_pasivo_abono = 0
        for cuenta in cuentas_pasivo:
            cuentas_pasivo_cargo += cuenta.cuenta_debe
            cuentas_pasivo_abono += cuenta.cuenta_haber
        cuentas_pasivo_total = -cuentas_pasivo_abono + cuentas_pasivo_cargo
        total = cuentas_activas_total + cuentas_pasivo_total
        return JsonResponse({"capital": cuentas_activas_total, "deuda": cuentas_pasivo_total, "total":total}, status=status.HTTP_200_OK)