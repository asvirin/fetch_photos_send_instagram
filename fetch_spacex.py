import requests
from dotenv import load_dotenv

def fetch_spacex():
    url = "https://api.spacexdata.com/v3/launches"
    r = requests.get(url)
    launches_data = r.json()

    for flight_number, flight_info in enumerate(launches_data):
        for images_number, images_url  in enumerate(flight_info['links']['flickr_images']):
            filename = 'spasex' + str(flight_number)+str(images_number) + '.jpg'
                get_images_spacex(images_url, filename)
                
def get_images_spacex(url, filename):
    r = requests.get(url)
    load_dotenv()
    dirfile = os.getenv("dirfile")
    fullpath = dirfile + filename
    with open(fullpath, 'wb') as f:  
        f.write(r.content)