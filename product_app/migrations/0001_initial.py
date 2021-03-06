# Generated by Django 3.2.7 on 2022-01-24 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('attribute_id', models.AutoField(primary_key=True, serialize=False)),
                ('attribute_name', models.CharField(blank=True, max_length=50, null=True)),
                ('attribute_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attribute_value', models.CharField(blank=True, max_length=50, null=True)),
                ('attribute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(blank=True, max_length=50, null=True)),
                ('parent_category_id', models.CharField(blank=True, max_length=50, null=True)),
                ('category_level', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('nr_items', models.CharField(blank=True, max_length=50, null=True)),
                ('temprelationship', models.CharField(blank=True, max_length=50, null=True)),
                ('dept_name', models.CharField(blank=True, max_length=50, null=True)),
                ('key', models.CharField(blank=True, max_length=50, null=True)),
                ('nefault_group_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_code', models.CharField(blank=True, max_length=150, null=True)),
                ('dept_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_short_description', models.TextField(blank=True, null=True)),
                ('product_long_description', models.TextField(blank=True, null=True)),
                ('product_retail_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_wholesale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_dealer_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_tax', models.CharField(blank=True, max_length=50, null=True)),
                ('group_id', models.CharField(blank=True, max_length=50, null=True)),
                ('product_notes', models.TextField(blank=True, null=True)),
                ('product_info', models.TextField(blank=True, null=True)),
                ('product_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('product_unite', models.CharField(blank=True, max_length=50, null=True)),
                ('product_qty_hold', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_order_limit', models.CharField(blank=True, max_length=50, null=True)),
                ('product_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.categories')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_location_id', models.CharField(blank=True, max_length=50, null=True)),
                ('product_id', models.CharField(blank=True, max_length=50, null=True)),
                ('location_id', models.CharField(blank=True, max_length=50, null=True)),
                ('product_quantity', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('images_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.CharField(blank=True, max_length=500, null=True)),
                ('image_name', models.CharField(blank=True, max_length=50, null=True)),
                ('image_caption', models.CharField(blank=True, max_length=150, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('product_attribute_id', models.AutoField(primary_key=True, serialize=False)),
                ('prodict_attribute_value_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.attributevalue')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.productstatus'),
        ),
        migrations.CreateModel(
            name='OrderProductAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_product_id', models.CharField(blank=True, max_length=50, null=True)),
                ('product_attribute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.productattribute')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='dept_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.department'),
        ),
    ]
