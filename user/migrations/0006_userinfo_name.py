# Generated by Django 3.0.3 on 2020-03-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200328_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='name',
            field=models.CharField(default='default', max_length=20),
            preserve_default=False,
        ),
    ]
