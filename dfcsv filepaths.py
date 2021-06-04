# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:03:37 2021

@author: u
"""

import os
if os.path.exists("test.db"):
    print ( " File is there " )
else:
    print ( " File is not there " )
CURR_DIR = os.path.dirname(os.path.realpath(__name__))
print(CURR_DIR)
print(CURR_DIR+"\\test.db") # escape character is \

# create a database at specific location and open only that one
