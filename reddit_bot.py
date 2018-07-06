import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username, 
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "what_a_mofo's testing lsd picture v0.1" )
    return r

def run_bot(r):
    for comment in r.subreddit('LSD').comments(limit = 50):
        if "lsd" in comment.body:
            print ("String Found!")


r = bot_login()
run_bot(r)