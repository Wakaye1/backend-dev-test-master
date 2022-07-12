from rest_framework import serializers
from .models import ClientWallet


class ClientWalletSerializer(serializers.ModelSerializer):
    cid = serializers.CharField(source = "client_field.cid")
    first_name = serializers.CharField(source = "client_field.first_name")
    last_name = serializers.CharField(source = "client_field.last_name")
    country_code = serializers.CharField(source = "client_field.country_code")
    email = serializers.EmailField(source = "client_field.email")
    address = serializers.CharField(source = "client_field.address")
    phone = serializers.CharField(source = "client_field.phone")
    class Meta:
        model = ClientWallet
        fields = ('cid', 'first_name', 'last_name', 'country_code', 'email',
                  'address', 'phone', 'total_balance', 'available_balance', 'lien_balance')