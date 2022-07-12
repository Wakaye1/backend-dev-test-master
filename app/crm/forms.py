
from django import forms
from .models import Client, ClientWallet
 
 
# creating a form
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
        
class ClientWalletForm(forms.ModelForm):
    class Meta:
        model = ClientWallet
        exclude = ['client_field', 'total_balance']