# from django.contrib.auth.models import User, Group
from .models import Risk, RiskField, RiskFieldType, RiskType, RiskValue
from rest_framework import serializers

class RiskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskType
        fields = ('name', 'id')

class RiskFieldTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFieldType
        fields = ('id', 'name', 'field')

class RiskValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskValue
        fields = ('text', 'risk_field')

class RiskFieldSerializer(serializers.ModelSerializer):
    field_type = RiskFieldTypeSerializer(read_only=True)
    risk_field_value = RiskValueSerializer(read_only=True, many=True)
    class Meta:
        model = RiskField
        fields = ('field_type', 'risk', 'risk_field_value')

class RiskSerializer(serializers.ModelSerializer):
    risk_type = RiskTypeSerializer(read_only=True)
    field = RiskFieldSerializer(read_only=True, many=True)
    class Meta:
        model = Risk
        fields = ('id', 'risk_type', 'client_name', 'field')