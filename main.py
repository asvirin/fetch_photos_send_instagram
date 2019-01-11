from instabot import Bot
from dotenv import load_dotenv
from os import listdir

def main():
    load_dotenv()
    folder_with_pics = os.getenv("folder_with_pics")
    photos_list = listdir(folder_with_pics)
    username = os.getenv("username")
    password = os.getenv("password")
    example_caption = os.getenv("caption")
    bot = Bot()
    bot.login(username, password)
    
    for filename in photos_list:
        pic = folder_with_pics + filename
        bot.upload_photo(pic, example_caption)
    
if __name__ == '__main__':
    main()
