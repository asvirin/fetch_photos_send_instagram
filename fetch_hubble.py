import requests

def fetch_hubble(collection_name):
    params = {page: 'all', 
              collection_name: collection_name}
    url = 'http://hubblesite.org/api/v3/images'
    r = requests.get(url, params=params)
    photos_info = r.json()
    for photo_number, photo_info in enumerate(photos):
        get_images_hubble(photo_info['id'])
        
def get_file_extension(url):
    url_parts = url.split('.')
    return url_parts[-1]

def get_images_hubble(filename):
    url = 'http://hubblesite.org/api/v3/image/{}'.format(filename)
    r = requests.get(url)
    photos_info = r.json()
    
    for images_url in photos_info['image_files']:
        continue
    
    folder_with_pics = os.getenv("folder_with_pics")
    fullpath = '{}{}.{}'.format(folder_with_pics, filename, get_file_extension(images_url['file_url']))
    
    r = requests.get(images_url['file_url'])
    with open(fullpath, 'wb') as f:  
        f.write(r.content)
