# Generated by Django 2.1.3 on 2018-11-15 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20181114_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riskvalue',
            name='risk_field',
        ),
        migrations.AddField(
            model_name='riskfield',
            name='value',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
