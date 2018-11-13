from django.db import models

# Create your models here.

class Risk(models.Model):
    # name = models.CharField(max_length=255)
    risk_type = models.ForeignKey(RiskType, related_name='risk_type')
    field = models.ForeignKey(RiskField, related_name='risk_field')
    value = models.CharField(max_length=255)

class RiskField(models.Model):
    risk_field = models.ForeignKey(RiskField, related_name='risk_field_type')
    # field_type = models.CharField(max_length=255)
    # risk = models.ForeignKey(Risk, related_name='risk_field')

class RiskType(models.Model):
    name = models.CharField(max_length=255)
    # risk = models.ForeignKey(Risk, related_name='risk_type')

class  RiskFieldType(models.Model):
    name = models.CharField(max_length=255)
    field = models.CharField(choices=())
    # risk_field = models.ForeignKey(RiskField, related_name='risk_field_type') 

class RiskValue(models.Model):
    text = models.CharField(max_length=255)
    risk = models.ForeignKey(Risk, related_name='risk_value')