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

config = configparser.ConfigParser()
config.read('config.ini')

reddit = praw.Reddit(client_id=config['DEFAULT']['CLIENT_ID'], \
                     client_secret=config['DEFAULT']['CLIENT_SECRET'], \
                     user_agent=config['DEFAULT']['USER_AGENT'], \
                     username=config['DEFAULT']['USERNAME'], \
                     password=config['DEFAULT']['PASSWORD'])