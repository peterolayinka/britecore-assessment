# Generated by Django 2.1.3 on 2018-11-14 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20181113_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskfieldtype',
            name='field',
            field=models.CharField(choices=[('NUMBER', 'number'), ('TEXT', 'text'), ('EMAIL', 'email'), ('DATE', 'date'), ('TEL', 'tel'), ('URL', 'url'), ('TIME', 'time')], max_length=255),
        ),
    ]
