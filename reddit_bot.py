import praw
import config

def bot_login():
    praw.Reddit(username = config.username, 
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "sassysalmnder testing lsd picture v0.1" )

bot_login()
