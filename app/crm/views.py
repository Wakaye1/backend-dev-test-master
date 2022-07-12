from django.shortcuts import get_object_or_404, render, redirect
from .forms import ClientForm, ClientWalletForm
from .models import Client, ClientWallet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import ClientWalletSerializer


# Create your views here.
def all_clients(request):
    active = True # Used to change the format of the navigation bar
    clients = Client.objects.all()
    context = {'all_clients': clients,
               'all_clients_active': active,}
    return render(request, 'crm/all_clients.html', context)
    

def create_client(request):
    active = True 
    context ={'create_client_active': active}
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_clients')
    context['form']= form
    return render(request, "crm/create_client.html", context)


def update_client(request, cid):
    context ={}
    client = get_object_or_404(Client, cid = cid)
    form = ClientForm(request.POST or None, instance = client)
    if form.is_valid():
        form.save()
        return redirect('all_clients')
    context["form"] = form
    return render(request, "crm/update_client.html", context)   


def delete_client(request, cid):
    context ={}
    client = get_object_or_404(Client, cid = cid)
    context['client'] = client
    if request.method =="POST":
        client.delete()
        return redirect('all_clients')
    return render(request, "crm/delete_client.html", context) 


def create_client_wallet(request, cid):
    # active = True 
    # context ={'create_client_active': active}
    client = get_object_or_404(Client, cid = cid)
    context = {}
    form = ClientWalletForm(request.POST or None)
    if form.is_valid():
        data = ClientWallet.objects.create(client_field = client, 
                                    available_balance = form.cleaned_data['available_balance'],
                                    lien_balance = form.cleaned_data['lien_balance'],
                                    total_balance = (form.cleaned_data['available_balance'] 
                                                     + form.cleaned_data['lien_balance']))
        data.save()
        return redirect('all_clients')
    context['form']= form
    return render(request, "crm/create_client_wallet.html", context)


def update_client_wallet(request, cid):
    context ={}
    client = get_object_or_404(ClientWallet, client_field = cid)
    form = ClientWalletForm(request.POST or None, instance = client)
    if form.is_valid():
        form.save()
        return redirect('all_clients')
    context["form"] = form
    return render(request, "crm/update_client_wallet.html", context)  


@api_view(['GET']) 
@permission_classes([IsAuthenticatedOrReadOnly])
def all_client_wallets(request): # endpoint
    client_wallets = ClientWallet.objects.all()
    serializer = ClientWalletSerializer(client_wallets, many = True)  
    json = JSONRenderer().render(serializer.data)
    return Response(json)

