# Generated by Django 3.2.7 on 2022-01-24 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('order_created_date', models.DateTimeField(auto_now_add=True)),
                ('order_qty', models.CharField(blank=True, max_length=50, null=True)),
                ('order_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('order_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('order_status', models.CharField(blank=True, max_length=50, null=True)),
                ('order_updated_date', models.DateTimeField(auto_now=True)),
                ('order_special_instruction', models.TextField(blank=True, null=True)),
                ('order_packed_by', models.CharField(blank=True, max_length=50, null=True)),
                ('order_packed_time', models.DateTimeField(auto_now_add=True)),
                ('customer_billing_id', models.CharField(blank=True, max_length=50, null=True)),
                ('createad_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('order_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_status_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderTracking',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_product_id', models.CharField(blank=True, max_length=50, null=True)),
                ('order_tracking_id', models.CharField(blank=True, max_length=50, null=True)),
                ('order_delivery_date', models.CharField(blank=True, max_length=50, null=True)),
                ('order_shipping_id', models.CharField(blank=True, max_length=50, null=True)),
                ('order_tracking_info', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingInfo',
            fields=[
                ('shipping_id', models.AutoField(primary_key=True, serialize=False)),
                ('shipping_name', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_type', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('warehouse_id', models.AutoField(primary_key=True, serialize=False)),
                ('warehouse_name', models.CharField(blank=True, max_length=50, null=True)),
                ('warehouse_position', models.CharField(blank=True, max_length=50, null=True)),
                ('warehouse_status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WareHouseLocation',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(blank=True, max_length=50, null=True)),
                ('warehouse_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_product_id', models.CharField(blank=True, max_length=50, null=True)),
                ('order_product_qty', models.CharField(blank=True, max_length=50, null=True)),
                ('order_product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('order_product_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('order_product_location_id', models.CharField(blank=True, max_length=50, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.orders')),
                ('order_product_status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.orderstatus')),
                ('order_product_warehouse_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.warehouselocation')),
            ],
        ),
    ]
