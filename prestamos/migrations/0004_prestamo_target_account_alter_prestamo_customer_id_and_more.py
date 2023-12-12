# Generated by Django 4.2.7 on 2023-11-30 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0005_delete_tiposdecuenta_alter_cuenta_account_type'),
        ('clientes', '0007_remove_cliente_id_cliente_customer_id'),
        ('prestamos', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='target_account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cuentas.cuenta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='loan_date',
            field=models.DateField(),
        ),
    ]