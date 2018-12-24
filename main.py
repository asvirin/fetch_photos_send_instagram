from instabot import Bot
from dotenv import load_dotenv
from os import listdir

def send_photos(dirfile, filename):
    load_dotenv()
    username = os.getenv("username")
    password = os.getenv("password")
    example_caption = os.getenv("caption")

    bot = Bot()
    bot.login(username, password)

    pic = dirfile + filename
    bot.upload_photo(pic, example_caption)
    
if __name__ == '__main__':
    load_dotenv()
    dirfile = os.getenv("dirfile")
    photos_list = listdir(dirfile)
    for images_number, filename in enumerate(photos_list):
        send_photos(dirfile, filename)