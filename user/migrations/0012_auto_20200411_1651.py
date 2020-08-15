# Generated by Django 3.0.3 on 2020-04-11 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_searchapp', '0005_auto_20200331_1541'),
        ('user', '0011_auto_20200410_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='smart_searchapp.Product'),
            preserve_default=False,
        ),
    ]