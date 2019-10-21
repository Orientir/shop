from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import pgettext_lazy

class LIQPAYPaymentForm(forms.Form):
    amount = forms.DecimalField()
    payment_method_nonce = forms.CharField()

    def get_payment_token(self):
        return self.cleaned_data["payment_method_nonce"]

    
