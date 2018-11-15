from django.contrib import admin

from .models import Risk, RiskField, RiskFieldType, RiskType

# Register your models here.

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'risk_type',)

@admin.register(RiskType)
class RiskTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(RiskField)
class RiskFieldAdmin(admin.ModelAdmin):
    list_display = ('field_type','value')

    # inlines= [
    #     RiskValueInline,
    # ]

@admin.register(RiskFieldType)
class RiskFieldTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'field',)
