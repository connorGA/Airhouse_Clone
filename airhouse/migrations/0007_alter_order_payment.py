# Generated by Django 5.0.1 on 2024-02-25 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airhouse', '0006_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('paid', 'Paid'), ('not_paid', 'Not Paid')], default='not_paid', max_length=20),
        ),
    ]
