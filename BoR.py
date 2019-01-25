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

#creating result dictionary that can be used to store data
resultsDictionary = { "subreddit":[], \
                      "title":[], \
                      "score":[], \
                      "url":[]}
#instantiating wantedSubreddit to select a subreddit to target and targettedSubreddit a list of targetted subreddits
wantedSubreddit = reddit.subreddit('default')
targettedSubreddit = ["all", "worldnews", "jokes", "quotes"]

#print method for results
def getTopResultDay(selected_subreddit):
    for sub in selected_subreddit:
        wantedSubreddit = reddit.subreddit(sub)
        for submission in wantedSubreddit.top(limit=1, time_filter='day'):
            print('Title: ' + submission.title)
            print('Score: ' + str(submission.score))
            print('url: ' + submission.url)
            
#store method to keeping results in a dictionary
def storeTopResultDay(selected_subreddit):
    for sub in selected_subreddit:
        wantedSubreddit = reddit.subreddit(sub)
        for submission in wantedSubreddit.top(limit=1, time_filter='day'):
            resultsDictionary["subreddit"].append(sub)
            resultsDictionary["title"].append(submission.title)
            resultsDictionary["score"].append(submission.score)
            resultsDictionary["url"].append(submission.url)

#User interaction

userInteract = input("Would you like to change the default queried subreddits?\n type 'y' and hit enter if yes or any other action and/or enter if no \n")
if userInteract.lower() == "y":
    targettedSubreddit = []
    addMore = 1
    while addMore > 0:
        addSub = input("Please enter the name of the subreddit you wish to add \n")
        targettedSubreddit.append(addSub)
        done = input("would you like to add another, type 'y' and hit enter for yes or any action and/or enter for no \n")
        if done != "y":
            addMore = 0
    getTopResultDay(targettedSubreddit)
    storeTopResultDay(targettedSubreddit)
else:
    getTopResultDay(targettedSubreddit)
    storeTopResultDay(targettedSubreddit)
    