from django import forms
from .models import RiskValue

class RiskValueForm(forms.ModelForm):
    class Meta:
        model = RiskValue
        fields = ('text',)

RiskValueFormSet=forms.modelformset_factory(
    RiskValue,
    fields = ('text',),
    min_num = 1, 
)
