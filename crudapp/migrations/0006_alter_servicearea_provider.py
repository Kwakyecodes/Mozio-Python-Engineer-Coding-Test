# Generated by Django 4.0.5 on 2022-06-14 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_alter_servicearea_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapp.provider'),
        ),
    ]
