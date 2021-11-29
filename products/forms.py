from django import forms

from products.models import ColorModel


class ColorModelForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = ColorModel
        widgets = {
            'code':forms.TextInput(attrs={
                'type': 'color'
            })
        }