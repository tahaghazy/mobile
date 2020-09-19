from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St',
        'class': 'form-control'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or suite',
        'class': 'form-control'
    }))
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'

    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField
from django_countries.data import COUNTRIES
from django_countries.fields import *



class ContactForm(forms.Form):
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address1 = forms.CharField(required=True)
    address2 = forms.CharField(required=True)
    city = forms.CharField(required=True)
    country = forms.ChoiceField(choices=sorted(COUNTRIES.items()))
    zip = forms.CharField(required=True, max_length=10)
    phone = forms.CharField(required=True)
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UsercreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='', label='username')
    first_name = forms.CharField(max_length=30, required=False, help_text='', label='First name')
    last_name = forms.CharField(max_length=30, required=False, help_text='', label=' Last name')
    email = forms.EmailField(max_length=254, help_text='name@example.com',
                             label='Email')
    password1 = forms.CharField(max_length=30, required=False,label='password ', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(max_length=30, required=False,
                                label=' password confirm', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('error')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('unavailable')
        return cd['username']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='username ')
    password = forms.CharField(
        label='password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')