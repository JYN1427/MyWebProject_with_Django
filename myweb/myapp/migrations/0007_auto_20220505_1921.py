# Generated by Django 2.2.24 on 2022-05-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20220505_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prettynum',
            name='price',
            field=models.IntegerField(default=0, verbose_name='价格'),
        ),
    ]
