from instabot import Bot

my_bot = Bot()
#login
my_bot.login(username="siyamahmed23a", password="PythonBOT")

#follow a user
my_bot.follow("sharifuddin471")

#follow multiple useres
my_bot.follow_users(["coding_.master","coding_for_beginners_","coders.learning"])

#unfollow the non followers
my_bot.unfollow_non_followers()

#uplod an image
my_bot.upload_photo("mee.jpg", caption="Pyhon")

#send message to user
my_bot.send_message("Helle", "coding_.master")

#like a post
my_bot.like_user("coding_.master", amount=2)

my_bot.logout()