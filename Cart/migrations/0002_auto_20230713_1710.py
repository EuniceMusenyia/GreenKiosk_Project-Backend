# Generated by Django 3.2.12 on 2023-07-13 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('Order', '0003_order_customer'),
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Order.order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='inventory.Product'),
        ),
    ]