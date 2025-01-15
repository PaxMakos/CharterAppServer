import datetime

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ChartersDatabase.models import Port, Boat, Charter, Photo


class AuthURLTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_url_returns_200(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)

    def test_logout_url_returns_200(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 200)

    def test_register_url_returns_200(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 200)

    def test_login_url_on_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 405)

    def test_logout_url_on_get(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 405)

    def test_register_url_on_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 405)

    def test_login_url_fails_with_invalid_credentials(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'error')

    def test_register_url_fails_with_existing_user(self):
        response = self.client.post(reverse('register'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'error')


class BoatViewsTests(TestCase):
    def setUp(self):
        self.port = Port.objects.create(name="Test Port")
        self.company = "Test Company"
        self.boat = Boat.objects.create(
            name="Test Boat",
            boatModel="Model X",
            productionYear=2020,
            length=30.5,
            width=10.5,
            draft=5.0,
            company=self.company,
            contactEmail="test@example.com",
            contactPhone="1234567890",
            motherPort=self.port,
            beds=4,
            pricePerDay=1000.0,
            description="A test boat"
        )

    def test_get_all_boats(self):
        response = self.client.get(reverse('getAllBoats'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(len(response.json()['boats']), 1)

    def test_get_boats_by_port(self):
        response = self.client.get(reverse('getBoatsByPort'), {'portName': self.port.name})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(len(response.json()['boats']), 1)

    def test_get_boats_by_company(self):
        response = self.client.get(reverse('getBoatsByCompany'), {'companyName': self.company})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(len(response.json()['boats']), 1)

    def test_get_boat(self):
        response = self.client.get(reverse('getBoat'), {'boatName': self.boat.name})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(response.json()['boat']['name'], self.boat.name)


class CharterViewsTests(TestCase):
    def setUp(self):
        self.port = Port.objects.create(name="Test Port")
        self.company = "Test Company"
        self.boat = Boat.objects.create(
            name="Test Boat",
            boatModel="Model X",
            productionYear=2020,
            length=30.5,
            width=10.5,
            draft=5.0,
            company=self.company,
            contactEmail="test@example.com",
            contactPhone="1234567890",
            motherPort=self.port,
            beds=4,
            pricePerDay=1000.0,
            description="A test boat"
        )
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.charter = Charter.objects.create(
            boat=self.boat,
            startDate=datetime.date(2023, 1, 1),
            endDate=datetime.date(2023, 1, 10),
            price=9000.0,
            user=self.user
        )

    def test_get_charters_by_boat(self):
        response = self.client.get(reverse('getChartersByBoat'), {'boatName': self.boat.name})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(len(response.json()['charters']), 1)

    def test_get_charters_by_user(self):
        response = self.client.get(reverse('getChartersByUser'), {'userName': self.user.username})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(len(response.json()['charters']), 1)

    def test_add_charter(self):
        response = self.client.post(reverse('addCharter'), {
            'boatName': self.boat.name,
            'startDate': '2023-02-01',
            'endDate': '2023-02-10'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(Charter.objects.count(), 2)

    def test_add_charter_on_same_date(self):
        response = self.client.post(reverse('addCharter'), {
            'boatName': self.boat.name,
            'startDate': '2023-01-05',
            'endDate': '2023-01-15'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'error')
        self.assertEqual(response.json()['message'], 'This boat is already chartered in this period')
        self.assertEqual(Charter.objects.count(), 1)

class PortViewsTests(TestCase):
    def setUp(self):
        self.port = Port.objects.create(
            name="Test Port",
            country="Test Country",
            city="Test City",
            address="123 Test St",
            phone="1234567890",
            email="test@port.com",
            website="http://testport.com",
            places=100,
            description="A test port",
            longitude=10.0,
            latitude=20.0
        )

    def test_get_ports(self):
        response = self.client.get(reverse('getPorts'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(len(response.json()['ports']), 1)

    def test_get_port(self):
        response = self.client.get(reverse('getPort'), {'portName': self.port.name})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(response.json()['port']['name'], self.port.name)

class PhotoViewsTests(TestCase):
    def setUp(self):
        self.port = Port.objects.create(name="Test Port")
        self.company = "Test Company"
        self.boat = Boat.objects.create(
            name="Test Boat",
            boatModel="Model X",
            productionYear=2020,
            length=30.5,
            width=10.5,
            draft=5.0,
            company=self.company,
            contactEmail="test@example.com",
            contactPhone="1234567890",
            motherPort=self.port,
            beds=4,
            pricePerDay=1000.0,
            description="A test boat"
        )
        self.photo = Photo.objects.create(
            boat=self.boat,
            photo=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

    def test_get_boat_photos(self):
        response = self.client.get(reverse('getBoatPhotos'), {'boatName': self.boat.name})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
        self.assertEqual(len(response.json()['photos']), 1)

    def test_get_photo(self):
        response = self.client.get(reverse('getPhoto', args=[self.photo.photo.name.split('/')[-1]]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'image/jpg')