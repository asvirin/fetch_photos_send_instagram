import requests

def fetch_spacex():
    url = "https://api.spacexdata.com/v3/launches"
    r = requests.get(url)
    launches_data = r.json()

    for flight_number, flight_info in enumerate(launches_data):
        for image_number, image_url  in enumerate(flight_info['links']['flickr_images']):
            filename =  'spacex{}{}.jpg'.format(flight_number, image_number)
            get_images_spacex(image_url, filename)
                
def get_images_spacex(url, filename):
    r = requests.get(url)
    folder_with_pics = os.getenv("folder_with_pics")
    fullpath = '{}{}'.format(folder_with_pics, filename)
    with open(fullpath, 'wb') as f:  
        f.write(r.content)
