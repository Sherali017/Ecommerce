# Generated by Django 3.2.7 on 2021-09-10 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.brandmodel'),
            preserve_default=False,
        ),
    ]
