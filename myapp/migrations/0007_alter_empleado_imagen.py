# Generated by Django 5.1.1 on 2024-09-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_empleado_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='imagen',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='empleados/'),
        ),
    ]
