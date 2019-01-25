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
results_dictionary = { "subreddit":[], \
                      "title":[], \
                      "score":[], \
                      "url":[]}
#instantiating wanted_subreddit to select a subreddit to target and targetted_subreddit a list of targetted subreddits
wanted_subreddit = reddit.subreddit('default')
targetted_subreddit = ["all", "worldnews", "jokes", "quotes"]

#print method for results
def get_top_result(selected_subreddit):
    for sub in selected_subreddit:
        wanted_subreddit = reddit.subreddit(sub)
        for submission in wanted_subreddit.top(limit=1, time_filter='day'):
            print('Title: ' + submission.title)
            print('Score: ' + str(submission.score))
            print('url: ' + submission.url)
            
#store method to keeping results in a dictionary
def store_top_result(selected_subreddit):
    for sub in selected_subreddit:
        wanted_subreddit = reddit.subreddit(sub)
        for submission in wanted_subreddit.top(limit=1, time_filter='day'):
            results_dictionary["subreddit"].append(sub)
            results_dictionary["title"].append(submission.title)
            results_dictionary["score"].append(submission.score)
            results_dictionary["url"].append(submission.url)

#User interaction

userInteract = input("Would you like to change the default queried subreddits?\n type 'y' and hit enter if yes or any other action and/or enter if no \n")
if userInteract.lower() == "y":
    targetted_subreddit = []
    add_more = 1
    while add_more > 0:
        add_sub = input("Please enter the name of the subreddit you wish to add \n")
        targetted_subreddit.append(add_sub)
        done = input("would you like to add another, type 'y' and hit enter for yes or any action and/or enter for no \n")
        if done != "y":
            add_more = 0
    get_top_result(targetted_subreddit)
    store_top_result(targetted_subreddit)
else:
    get_top_result(targetted_subreddit)
    store_top_result(targetted_subreddit)