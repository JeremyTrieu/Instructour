# Generated by Django 4.0.dev20210612144642 on 2021-08-28 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.school'),
        ),
    ]
