# Generated by Django 5.0.1 on 2024-02-17 04:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airhouse', '0005_order_alter_category_options_orderitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='airhouse.order'),
        ),
    ]
