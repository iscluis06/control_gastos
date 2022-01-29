# Generated by Django 4.0.1 on 2022-01-28 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_nombre', models.CharField(max_length=200)),
                ('categoria_creado', models.DateTimeField(auto_now_add=True)),
                ('categoria_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('cuenta_id', models.AutoField(primary_key=True, serialize=False)),
                ('cuenta_tipo', models.CharField(choices=[('A', 'Activo'), ('P', 'Pasivo')], max_length=1)),
                ('cuenta_debe', models.DecimalField(decimal_places=4, default=0.0, max_digits=25)),
                ('cuenta_haber', models.DecimalField(decimal_places=4, default=0.0, max_digits=25)),
                ('cuenta_nombre', models.CharField(max_length=200, unique=True)),
                ('cuenta_creada', models.DateTimeField(auto_now_add=True)),
                ('cuenta_modificada', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('subcategoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('subcategoria_nombre', models.CharField(max_length=200)),
                ('subcategoria_creado', models.DateTimeField(auto_now_add=True)),
                ('subcategoria_modificado', models.DateTimeField(auto_now=True)),
                ('subcategoria_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_gastos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('transaccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaccion_fecha', models.DateTimeField(auto_now_add=True)),
                ('transaccion_cantidad', models.DecimalField(decimal_places=4, max_digits=25)),
                ('transaccion_tipo_movimiento', models.CharField(choices=[('A', 'Abonar'), ('C', 'Cargar')], max_length=1)),
                ('transaccion_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_gastos.cuenta')),
                ('transaccion_subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_gastos.subcategoria')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleTransaccion',
            fields=[
                ('detalle_trasanccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('detalle_transaccion_nombre', models.CharField(max_length=200)),
                ('detalle_transaccion_descripcion', models.CharField(max_length=500, null=True)),
                ('detalle_transaccion_fecha', models.DateTimeField(auto_now_add=True)),
                ('detalle_transaccion_transaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_gastos.transaccion')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='categoria_cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_gastos.cuenta'),
        ),
    ]
