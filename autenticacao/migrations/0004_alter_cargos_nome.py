# Generated by Django 4.2.5 on 2023-09-10 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0003_cargos_nome_alter_usuarios_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargos',
            name='nome',
            field=models.CharField(default='Visualizador', max_length=20, null=True, unique=True),
        ),
    ]
