from django import forms
from .models import Asset

class assetDropdown(forms.Form):
    assets = forms.ModelChoiceField(
        queryset=Asset.objects.values_list("assetName").distinct(),

        empty_label=None
    )

class questionInputTextField(forms.Form):
    question = forms.CharField(label="Enter Question Here:", max_length=100)

class threatInputTextField(forms.Form):
    threat = forms.CharField(label="Threat Name:", max_length=100)

class answerInputTextField(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(attrs={'style' : 'background-color: mistyrose; border: none', 'placeholder' : 'Have another answer? Type it here!'}))
