from .models import Razorpay
from django import forms
from django.forms import ModelForm


class RazorpayForm(ModelForm):
    class Meta:
        model = Razorpay
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RazorpayForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['amount'].widget.attrs['class'] = 'form-control'
            self.fields['services'].widget.attrs['class'] = 'form-control'
