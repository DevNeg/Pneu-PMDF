# Generated by Django 4.2.5 on 2023-09-10 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0006_cargos_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='cargo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.cargos'),
        ),
    ]
