# Write a background task that populates the Client model
# with users from this [endpoint](https://62c2c06cff594c656764970a.mockapi.io/users).
from background_task import background
import json
from .models import Client
from urllib.request import urlopen


@background(schedule = 60)
def create_client():
    response = urlopen("https://raw.githubusercontent.com/01kazu/connect-four/master/users.json")
    data_json = json.loads(response.read())
    print(data_json)
    for data in data_json['data']:
        try:
            client = Client.objects.get(cid = data['cid'])
        except Client.DoesNotExist:
            client = Client.objects.create(cid = data['cid'], first_name = data['first_name'],
                                          last_name = data['last_name'],
                                          country_code = data['country_code'],
                                          email = data['email'], address = data['address'],
                                          phone = data['phone'])
            client.save()
