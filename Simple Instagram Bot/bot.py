from instabot import Bot
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


bot = Bot()
bot.login(username=username, password=password)
bot.follow('wscubetechindia')

bot.upload_photo("E:/STUDY THINGS/WEB DEVELOPMENT/image.png",caption="hahahehe")

bot.unfollow('wscubetechindia')

# Sent message to multiple users

users=["user1","user2","user3","user4","user5","user6"]
bot.send_message("Hello guyz!!!",users)

followers=bot.get_user_followers(username)
for follower in followers:
    print(bot.get_user_info(follower))