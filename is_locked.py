import os
import twitter_bot

if os.path.exists("/var/www/html/twitter-bot/isConnected"):
    twitter_bot.send_good_tweet()
    print("good tweet sent.")
else:
    twitter_bot.send_pute_tweet()
    print("pute tweet sent.")