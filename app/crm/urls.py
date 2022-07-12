from django.urls import path, include
from .views import (create_client, update_client, delete_client, 
                    all_client_wallets, create_client_wallet, update_client_wallet) 


urlpatterns = [
    # path('clients/all', all_clients, name='all_clients'),
    # path('clients/all', all_clients, name='all_clients'),
    path('client/create', create_client, name='create_client'),
    path('client/update/<str:cid>', update_client, name='update_client'),
    path('client/delete/<str:cid>', delete_client, name='delete_client'),
    path('client-wallet/create/<str:cid>', create_client_wallet, name='create_client_wallet'),
    path('client-wallet/update/<str:cid>', update_client_wallet, name='update_client_wallet'),
    path('client-wallet/api/all', all_client_wallets, name='all_client_wallets'),
]