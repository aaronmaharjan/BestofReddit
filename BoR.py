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

#creating result class that can be used to store data
class RedditResult:
  def __init__(self, title, id, score, selftext):
    self.title = title
    self.score = score
    self.link = link
    
wantedSubreddit = reddit.subreddit('default')

def getTopResultDay(selected_subreddit):
    wantedSubreddit = reddit.subreddit(selected_subreddit)
    for submission in wantedSubreddit.top(limit=1, time_filter='day'):
        print('Title: ' + submission.title)
        print('Score: ' + str(submission.score))
        print('Link: https://www.reddit.com' + submission.permalink)
getTopResultDay('askreddit')
    
    