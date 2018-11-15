from django.db import models
from enum import Enum

class RiskFieldTypeEnum(Enum):
    NUMBER = 'number'
    TEXT = 'text'
    EMAIL = 'email'
    DATE = 'date'
    TEL = 'tel'
    URL = 'url'
    TIME = 'time'

# Create your models here.
class RiskType(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    # risk = models.ForeignKey(Risk, related_name='risk_type')

class  RiskFieldType(models.Model):
    name = models.CharField(max_length=255)
    field = models.CharField(max_length=255,
                choices=[(tag.name, tag.value) for tag in RiskFieldTypeEnum])
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    # risk_field = models.ForeignKey(RiskField, related_name='risk_field_type') 


class Risk(models.Model):
    client_name = models.CharField(max_length=255)
    risk_type = models.ForeignKey(RiskType, 
                related_name='risk_type', on_delete=models.SET_NULL,
                blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return f'{self.client_name} ({self.risk_type})'

class RiskField(models.Model):
    field_type = models.ForeignKey(RiskFieldType, 
                related_name='risk_field_type', on_delete=models.SET_NULL,
                blank=True, null=True)
    risk = models.ForeignKey(Risk, 
                related_name='field', on_delete=models.SET_NULL,
                blank=True, null=True)
    value = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.field_type}'
