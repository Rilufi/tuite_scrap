from twikit import Client, TooManyRequests
from configparser import ConfigParser
import os


#* login credentials
username = os.getenv("TWITTER_USERNAME")
email = os.getenv("TWITTER_EMAIL")
password = os.getenv("TWITTER_PASSWORD")

#* authenticate to X.com
#! 1) use the login credentials. 2) use cookies.
client = Client(language='en-US')
client.login(auth_info_1=username, auth_info_2=email, password=password)
client.save_cookies('cookies.json')
