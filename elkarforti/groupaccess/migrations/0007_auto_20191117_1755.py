# Generated by Django 2.2.7 on 2019-11-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupaccess', '0006_auto_20191117_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fortiparameters',
            name='fortiCipheredData',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='fortiparameters',
            name='fortiCipheredIV',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
