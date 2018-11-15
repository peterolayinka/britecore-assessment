from django.contrib import admin

from .forms import RiskValueFormSet, RiskValueForm
from .models import Risk, RiskField, RiskFieldType, RiskType, RiskValue

# Register your models here.

class RiskValueInline(admin.TabularInline):
    model = RiskValue
    max_num = 1

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

@admin.register(RiskValue)
class RiskValueAdmin(admin.ModelAdmin):
    list_display = ('text',)