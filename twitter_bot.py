from datetime import datetime
import tweepy
from config import consumer_key, consumer_secret, access_token_key, access_token_secret

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token_key,
    access_token_secret=access_token_secret
)

def send_pute_tweet():
    french_days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    french_months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

    current_date_time = datetime.now()

    formatted_date = "{} {} {} {}".format(
    french_days[current_date_time.weekday()],  # Get the day name in French
    current_date_time.day,                     # Get the day of the month
    french_months[current_date_time.month - 1],# Get the month name in French
    current_date_time.year                     # Get the year
    )

    current_time = current_date_time.strftime('%H:%M')
    tweet_text = "On est le "+ formatted_date+ "\nil est "+ current_time+ "\nJe suis une énorme pute car je dors encore au lieu de travailler.\nDM ce tweet avec ton 06 pour recevoir un Lydia de 10€. Bonne journée."
    client.create_tweet(text=tweet_text)

def send_good_tweet():
    french_days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    french_months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

    current_date_time = datetime.now()

    formatted_date = "{} {} {} {}".format(
    french_days[current_date_time.weekday()],  # Get the day name in French
    current_date_time.day,                     # Get the day of the month
    french_months[current_date_time.month - 1],# Get the month name in French
    current_date_time.year                     # Get the year
    )
    current_time = current_date_time.strftime('%H:%M')
    tweet_text = "On est le "+ formatted_date+ "\nil est "+ current_time+ "\n Bonne journée."
    client.create_tweet(text=tweet_text)