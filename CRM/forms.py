from django.forms import ModelForm

from CRM.models import Payments


class Payment_form(ModelForm):
    class Meta:
        model = Payments
        fields = ('pay', 'student')
