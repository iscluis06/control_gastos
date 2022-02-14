from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.views import APIView

from control_gastos.models import Cuenta


class Balance(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cuentas_deuda = Cuenta.objects.filter(cuenta_deuda=True)
        cuentas_deuda_monto = 0
        for cuenta in cuentas_deuda:
            cuentas_deuda_monto += cuenta.cuenta_monto
        cuentas_capital = Cuenta.objects.filter(cuenta_deuda=False)
        cuentas_capital_monto = 0
        for cuenta in cuentas_capital:
            cuentas_capital_monto += cuenta.cuenta_monto
        total = cuentas_capital_monto - cuentas_deuda_monto
        return JsonResponse({"capital": cuentas_capital_monto, "deuda": cuentas_deuda_monto, "total":total}, status=status.HTTP_200_OK)