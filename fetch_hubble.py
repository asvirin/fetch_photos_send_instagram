import requests
from dotenv import load_dotenv

def fetch_hubble(collection_name):
    params = {page: 'all', 
              collection_name: collection_name}
    url = 'http://hubblesite.org/api/v3/images'
    r = requests.get(url, params=params)
    simple = r.json()
    for photo_number, photo_info in enumerate(simple):
        get_images_hubble(photo_info['id'])
        
def get_file_extension(url):
    url_parts = url.split('.')
    return url_parts[-1]

def get_images_hubble(filename):
    url = 'http://hubblesite.org/api/v3/image/' + str(filename)
    r = requests.get(url)
    simple = r.json()
    
    for images_url in simple['image_files']:
        continue
    extension = '.' + get_file_extension(images_url['file_url'])
    
    r = requests.get(images_url['file_url'])
    
    load_dotenv()
    dirfile = os.getenv("dirfile")
    fullpath = dirfile + str(filename) + extension
    with open(fullpath, 'wb') as f:  
        f.write(r.content)
