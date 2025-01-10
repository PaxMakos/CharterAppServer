from django.contrib.auth.models import User
from django.test import TestCase
import requests
from PIL import Image
from io import BytesIO
import datetime
from django.urls import reverse

from ChartersDatabase.models import Boat, Port


# Create your tests here.
def show_photos(boat_name):
    url = 'http://127.0.0.1:8000/db/boatPhotos/'
    params = {'boatName': boat_name}
    response = requests.get(url, params=params, verify=False)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            for photo_url in data['photos']:
                photo_url = 'http://127.0.0.1:8000/db' + photo_url
                photo_response = requests.get(photo_url)

                if photo_response.status_code == 200:
                    image = Image.open(BytesIO(photo_response.content))
                    image.show()
                else:
                    print(f"Failed to retrieve photo. Status code: {photo_response.status_code}")
        else:
            print(f"Error: {data['message']}")
    else:
        print(f"Failed to retrieve photos. Status code: {response.status_code}")


#show_photos('Mazury Cruiser 3')

class CharterOverlapTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.port = Port.objects.create(
            name='Test Port',
            country='Test Country',
            city='Test City',
            address='Test Address',
            phone='123456789',

        )
        self.boat = Boat.objects.create(
            name='Test Boat',
            boatModel='Cruiser 34',
            productionYear=2020,
            length=34,
            width=12,
            draft=6,
            company='Test Company',
            motherPort=self.port,
            beds=8,
            pricePerDay=590,
            description='A comfortable cruiser for family trips.'
        )
