# Generated by Django 4.1.3 on 2022-12-13 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'manufacturer',
            },
        ),
    ]
