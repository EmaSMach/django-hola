# Generated by Django 3.1 on 2020-08-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienvenido', '0002_departamento_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='foto',
            field=models.ImageField(null=True, upload_to='empleados/'),
        ),
    ]
