# Generated by Django 2.1.3 on 2018-11-13 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_risk_client_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='risk',
            name='field',
        ),
        migrations.AddField(
            model_name='riskfield',
            name='risk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='field', to='management.Risk'),
        ),
    ]