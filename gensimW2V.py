# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:47:39 2019

@author: Aaron Maharjan
"""

import gzip
import gensim 
import logging
input_file = 'reviews_data.txt.gz'
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



with gzip.open (input_file, 'rb') as f:
        for i,line in enumerate (f):
            print(line)
            break