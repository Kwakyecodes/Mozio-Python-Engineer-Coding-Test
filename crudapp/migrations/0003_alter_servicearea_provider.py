# Generated by Django 4.0.5 on 2022-06-14 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_provider_email_provider_langauge_provider_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='something', to='crudapp.provider'),
        ),
    ]
