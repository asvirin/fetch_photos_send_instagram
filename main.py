from instabot import Bot
from dotenv import load_dotenv
from os import listdir
load_dotenv()

def send_photos(dirfile, filename):
    username = os.getenv("username")
    password = os.getenv("password")
    example_caption = os.getenv("caption")

    bot = Bot()
    bot.login(username, password)

    pic = dirfile + filename
    bot.upload_photo(pic, example_caption)
    
if __name__ == '__main__':
    dirfile = os.getenv("dirfile")
    photos_list = listdir(dirfile)
    for filename in photos_list:
        send_photos(dirfile, filename)
