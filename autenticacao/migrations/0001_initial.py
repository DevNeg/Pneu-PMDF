# Generated by Django 4.2.5 on 2023-09-08 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=64)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacao.cargos')),
            ],
        ),
    ]
