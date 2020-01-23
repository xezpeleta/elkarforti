# Generated by Django 2.2.7 on 2019-11-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groupaccess', '0002_fortiparameters'),
    ]

    operations = [
        migrations.AddField(
            model_name='fortiparameters',
            name='automaticCloseTime',
            field=models.TimeField(default='22:00'),
        ),
        migrations.AddField(
            model_name='fortiparameters',
            name='automaticOpenClose',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fortiparameters',
            name='automaticOpenTime',
            field=models.TimeField(default='15:00'),
        ),
    ]
