# Generated by Django 3.0.3 on 2020-04-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200409_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
