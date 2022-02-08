from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cuenta(models.Model):
    TIPO_CUENTA = (
        ('A', 'Activo'),
        ('P', 'Pasivo')
    )
    cuenta_id = models.AutoField(primary_key=True,)
    cuenta_tipo = models.CharField(max_length=1, choices=TIPO_CUENTA, null=False)
    cuenta_debe = models.DecimalField(max_digits=25, decimal_places=4, default=0.0)
    cuenta_haber = models.DecimalField(max_digits=25, decimal_places=4, default=0.0)
    cuenta_nombre = models.CharField(max_length=200, null=False, blank=False, unique=True)
    cuenta_creada = models.DateTimeField(auto_now_add=True)
    cuenta_modificada = models.DateTimeField(auto_now=True)
    cuenta_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nombre = models.CharField(max_length=200, null=False)
    categoria_creado = models.DateTimeField(auto_now_add=True)
    categoria_modificado = models.DateTimeField(auto_now=True)
    categoria_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Subcategoria(models.Model):
    subcategoria_id = models.AutoField(primary_key=True)
    subcategoria_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria_nombre = models.CharField(max_length=200, null=False)
    subcategoria_creado = models.DateTimeField(auto_now_add=True)
    subcategoria_modificado = models.DateTimeField(auto_now=True)
    subcategoria_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Transaccion(models.Model):
    transaccion_id = models.AutoField(primary_key=True)
    transaccion_subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    transaccion_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    transaccion_fecha = models.DateTimeField(auto_now_add=True)
    transaccion_cantidad = models.DecimalField(max_digits=25, decimal_places=4)
    transaccion_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Transaccion, self).save(*args, **kwargs)
        cuenta = Cuenta.objects.get(pk=self.transaccion_cuenta.cuenta_id)
        if cuenta.cuenta_tipo == 'A' and self.transaccion_cantidad > 0:
            cuenta.cuenta_debe += self.transaccion_cantidad
        elif cuenta.cuenta_tipo == 'A' and self.transaccion_cantidad < 0:
            cuenta.cuenta_haber += self.transaccion_cantidad
        elif cuenta.cuenta_tipo == 'P' and self.transaccion_cantidad > 0:
            cuenta.cuenta_haber += self.transaccion_cantidad
        elif cuenta.cuenta_tipo == 'P' and self.transaccion_cantidad < 0:
            cuenta.cuenta_debe += self.transaccion_cantidad
        cuenta.save()

class DetalleTransaccion(models.Model):
    detalle_trasanccion_id = models.AutoField(primary_key=True)
    detalle_transaccion_transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    detalle_transaccion_nombre = models.CharField(null=False, max_length=200)
    detalle_transaccion_descripcion = models.CharField(null=True, max_length=500)
    detalle_transaccion_fecha = models.DateTimeField(auto_now_add=True)
    detalle_transaccion_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
