# Generated by Django 2.1.3 on 2018-11-13 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20181113_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='client_name',
            field=models.CharField(default='Peter Olayinka', max_length=255),
            preserve_default=False,
        ),
    ]
