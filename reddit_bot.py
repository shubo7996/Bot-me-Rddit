import praw
import config
import time

def bot_login():
    print ("logging in!")
    r = praw.Reddit(username = config.username, 
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "what_a_mofo's testing lsd picture v0.1" )
    
    print("logged in")

    return r

def run_bot(r , comments_replied_to):
    print ("obtaining 25 comments!")

    for comment in r.subreddit('test').comments(limit = 25):
        if "lsd" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print ("string with \"lsd\" found in comments" + comment.id )
            comment.reply ("[here](https://www.etsy.com/listing/219095038/beatles-yellow-submarine-blotter-art?ref=shop_home_active_9) is what it looks like! go ahead and try. it will illuminate your mind!")
            print ("Replied to comment " + comment.id)

            comments_replied_to.append(comment.id)
    print ("sleeping for 10 seconds...")
    time.sleep(10)

def get_saved_comments():
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
while True:
    run_bot(r)