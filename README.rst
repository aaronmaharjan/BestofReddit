Best of Reddit
==============

USAGE
=====

https://www.reddit.com/prefs/apps In here you can create an app or
create another app,

1) Get the keys required after creating your app and put them into a
   file called config.ini Note that there is no config.ini file in this
   repo as it has been ignored, edit the config\_example.ini file with
   the correct details and either change the name in the BoR.py file to
   read config\_example.ini instead of config.ini or rename
   config\_example.ini to config.ini
   
Make sure you have the libraries listed below

virtualenv venv

bash: source venv/bin/activate      Windows: venv\Scripts\activate

pip install -r requirements.txt

Run the BoR.py file from command line or within Spyder,etc

Libraries Used
==============

praw
pandas
configparser
source
virtualenv


Dataframe pictured below, WIP will improve visualisation later.

.. image:: images/dataframe_default.png
  :alt: DataframePicture
  :align: left
  

.. meta::
   :description: BestofReddit project
   :author: Aaron Maharjan
   :keywords: python, reddit
   
USING PEP 8 -- Style Guide for Python Code 
USING PRAW : https://github.com/praw-dev/praw 
Special thanks to : Felippe Rodrigues for this helpful guide to help get me started
http://www.storybench.org/how-to-scrape-reddit-with-python/

