# Generated by Django 2.2.7 on 2019-11-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupaccess', '0005_auto_20191117_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fortiparameters',
            name='fortiCipheredData',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='fortiparameters',
            name='fortiCipheredIV',
            field=models.CharField(default='', max_length=128),
        ),
    ]
