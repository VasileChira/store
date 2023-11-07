from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	division_CHOICES = (
		('Romania', 'Romania'),
		('Germany', 'Germany'),
		('Italy', 'Italy '),
	)

	DISCRICT_CHOICES = (
		('Bucharest', 'Bucharest'),
		('Berlin', 'Berlin'),
		('Rome', 'Rome'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Pay in cash on arrival', 'Pay in cash on arrival'),
		('Pay with cash on arrival','Pay with cash on arrival')
	)

	division = forms.ChoiceField(choices=division_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
