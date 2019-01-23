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


# setting subreddit to target
subreddit = reddit.subreddit('worldnews')

# finding top subreddit posts, also usable are .hot, .new, .controversial, .gilded and .search("keywords")
#this defaults to return top 100 submissions, you can set an amount with .top(limit=500) etc and note reddit's request limit is 1000
top_subreddit = subreddit.top()

# currently retrieving top result of all time and sdome elements of the submission
for submission in subreddit.top(limit=1):
    print(submission.title)
    print(submission.id)
    print(submission.selftext)
    
# want to grab top result for certain time frame such as the date of 23-jan-19 only.