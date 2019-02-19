# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 15:36:03 2019

@author: Aaron Maharjan
LICENSE: MIT
"""
#! usr/bin/env python3

import praw
import pandas as pd
import datetime as dt
import configparser

#reading external config file

config = configparser.ConfigParser()
config.read('config.ini')

#loading config settings
reddit = praw.Reddit(client_id=config['DEFAULT']['CLIENT_ID'], \
                     client_secret=config['DEFAULT']['CLIENT_SECRET'], \
                     user_agent=config['DEFAULT']['USER_AGENT'], \
                     username=config['DEFAULT']['USERNAME'], \
                     password=config['DEFAULT']['PASSWORD'])


class RedditMain:
    results_dictionary = { "subreddit":[], \
                          "title":[], \
                          "score":[], \
                          "url":[]}
    
    def __init__(self):
        pass
    
    
    #print method for results
    def get_top_result(self, sub):
        for submission in reddit.subreddit(sub).top(limit=1):
        #for submission in wanted_subreddit.top(limit=1, time_filter='day'):
            print('Title: ' + submission.title)
            print('Score: ' + str(submission.score))
            print('url: ' + submission.url)
                
    #store method to keeping results in a dictionary
    def store_top_result(self, sub):
        for submission in reddit.subreddit(sub).top(limit=1):
            RedditMain.results_dictionary["subreddit"].append(sub)
            RedditMain.results_dictionary["title"].append(submission.title)
            RedditMain.results_dictionary["score"].append(submission.score)
            RedditMain.results_dictionary["url"].append(submission.url)
        data = pd.DataFrame(RedditMain.results_dictionary)
        data.to_csv('data/' + sub + '.csv' , index=False)

bestReddit = RedditMain()
bestReddit.store_top_result('all')




