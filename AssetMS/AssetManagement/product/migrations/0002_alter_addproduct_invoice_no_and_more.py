# Generated by Django 4.1.3 on 2022-12-18 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='invoice_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]
