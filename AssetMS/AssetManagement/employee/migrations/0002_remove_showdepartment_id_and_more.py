# Generated by Django 4.1.3 on 2022-12-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showdepartment',
            name='id',
        ),
        migrations.AlterField(
            model_name='showdepartment',
            name='department_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='showdepartment',
            table='department',
        ),
    ]
