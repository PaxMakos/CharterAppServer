import requests
from PIL import Image
from io import BytesIO


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

                print(photo_url)

                if photo_response.status_code == 200:
                    image = Image.open(BytesIO(photo_response.content))
                    image.show()
                else:
                    print(f"Failed to retrieve photo. Status code: {photo_response.status_code}")
        else:
            print(f"Error: {data['message']}")
    else:
        print(f"Failed to retrieve photos. Status code: {response.status_code}")


show_photos('Mazury Cruiser 3')

