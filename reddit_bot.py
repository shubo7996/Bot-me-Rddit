import praw
import config

praw.Reddit(username = config.username, 
            password = config.password
            client_id = config.client_id
            client_secret_id = config.client_secret_id
            user_agent = "sassysalmnder's drug test")


