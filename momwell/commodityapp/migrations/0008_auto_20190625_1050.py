# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-25 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodityapp', '0007_auto_20190625_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='cart_commoditys_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='commodityapp.ShopCart', verbose_name='购物车商品id'),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='commodity_nums',
            field=models.IntegerField(default=1, verbose_name='商品数量'),
        ),
    ]