# Generated by Django 5.0.6 on 2024-06-27 05:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Footwears',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('sandals', 'sandals'), ('slipperandflipflops', 'slipperandflipflops'), ('casualshoes', 'casualshoes'), ('specialcollections', 'specialcollections'), ('flatshoes', 'flatshoes'), ('schooledition', 'schooledition')], max_length=100)),
                ('product_types', models.CharField(choices=[('ladies', 'ladies'), ('gents', 'gents'), ('boys', 'boys'), ('girls', 'girls'), ('kids', 'kids')], max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('product_description', models.TextField()),
                ('product_color', models.CharField(choices=[('Black', 'Black'), ('Blue', 'Blue'), ('Brown', 'Brown'), ('Camel', 'Camel'), ('Cherry', 'Cherry'), ('Gold', 'Gold'), ('Grape', 'Grape'), ('Green', 'Green'), ('Grey', 'Grey'), ('Maroon', 'Maroon'), ('Mehandi', 'Mehandi'), ('Navy', 'Navy'), ('Olive', 'Olive'), ('Peach', 'Peach'), ('Peacock', 'Peacock'), ('Pink', 'Pink'), ('Purple', 'Purple'), ('Tan', 'Tan'), ('Violet', 'Violet'), ('White', 'White'), ('Wine', 'Wine'), ('Yellow', 'Yellow')], max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Footwearimages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_color', models.CharField(choices=[('Black', 'Black'), ('Blue', 'Blue'), ('Brown', 'Brown'), ('Camel', 'Camel'), ('Cherry', 'Cherry'), ('Gold', 'Gold'), ('Grape', 'Grape'), ('Green', 'Green'), ('Grey', 'Grey'), ('Maroon', 'Maroon'), ('Mehandi', 'Mehandi'), ('Navy', 'Navy'), ('Olive', 'Olive'), ('Peach', 'Peach'), ('Peacock', 'Peacock'), ('Pink', 'Pink'), ('Purple', 'Purple'), ('Tan', 'Tan'), ('Violet', 'Violet'), ('White', 'White'), ('Wine', 'Wine'), ('Yellow', 'Yellow')], max_length=100)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='imagesall/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VolantApp.footwears')),
            ],
        ),
        migrations.CreateModel(
            name='Footwearsize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13')], max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VolantApp.footwears')),
            ],
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('in_cart', 'in_cart'), ('order_placed', 'order_placed'), ('cancelled', 'cancelled')], default='in_cart', max_length=100)),
                ('total', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VolantApp.footwearimages')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VolantApp.footwears')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VolantApp.footwearsize')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('cancelled', 'cancelled'), ('order-placed', 'order-placed'), ('dispatched', 'dispatched'), ('shipped', 'shipped'), ('delivered', 'delivered')], default='order-placed', max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('total', models.FloatField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VolantApp.footwearimages')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VolantApp.footwears')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VolantApp.footwearsize')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
