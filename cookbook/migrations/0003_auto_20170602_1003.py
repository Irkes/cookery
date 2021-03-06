# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_auto_20170528_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Get_Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_recipe', models.IntegerField()),
                ('recipe_name', models.CharField(max_length=45)),
                ('recipe_calories', models.IntegerField()),
                ('recipe_discription', models.CharField(max_length=500)),
                ('cooking_time', models.IntegerField()),
                ('number_of_servings', models.IntegerField()),
                ('Rating', models.IntegerField()),
                ('Creation_date', models.DateTimeField()),
                ('number_of_steps', models.IntegerField()),
                ('steps_discription', models.CharField(max_length=2000)),
                ('product_name', models.CharField(max_length=45)),
                ('product_calories', models.IntegerField()),
                ('product_weight', models.IntegerField()),
                ('product_weight_type', models.CharField(max_length=45)),
                ('product_category_name', models.CharField(max_length=45)),
                ('recipe_category_name', models.CharField(max_length=45)),
                ('main_picture', models.CharField(max_length=500)),
                ('picture', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='pictures_has_recipe',
            name='id_picture',
        ),
        migrations.RemoveField(
            model_name='pictures_has_recipe',
            name='id_recipe',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id_category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id_discription',
        ),
        migrations.DeleteModel(
            name='Product_category',
        ),
        migrations.RemoveField(
            model_name='product_has_pictures',
            name='id_picture',
        ),
        migrations.RemoveField(
            model_name='product_has_pictures',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='product_has_recipe',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='product_has_recipe',
            name='id_recipe',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='id_discription',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='id_feed_type',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='id_recipe_category',
        ),
        migrations.AlterField(
            model_name='menu',
            name='id_recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Get_Recipe'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Discriptions',
        ),
        migrations.DeleteModel(
            name='Feed_type',
        ),
        migrations.DeleteModel(
            name='Pictures',
        ),
        migrations.DeleteModel(
            name='Pictures_has_Recipe',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Product_has_Pictures',
        ),
        migrations.DeleteModel(
            name='Product_has_Recipe',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.DeleteModel(
            name='Recipe_category',
        ),
    ]
