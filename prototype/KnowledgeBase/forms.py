from django import forms
from .models import Asset


class assetDropdown(forms.Form):
    assets = forms.ModelChoiceField(
        queryset=Asset.objects.values_list("assetName").distinct(),

        empty_label=None
    )


class inputTextField(forms.Form):
    question = forms.CharField(label="Enter Question Here:", max_length=100)



