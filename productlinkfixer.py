# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 07:01:25 2023

@author: siton
"""

import pyperclip
import re

recent_value = None;
print("""Welcome to Product Link Fixer 
v1.1, by JJG
Enjoy uncluttered, untracked linking for Amazon, eBay, and Etsy! 
(Exit at any time by hitting ctr-c)""")

while True:
    recent_value = pyperclip.waitForNewPaste()
    print(f"\nNew clipboard contents:\n{recent_value}")
    
    # Is it an Amazon product link? If so, cut off the faf
    match_object = re.search('https://www.amazon.com/?[\w-]*/dp/\w*/' , recent_value)
    if match_object:
        print("Amazon product URL detected, reformatting")
        recent_value = match_object.group()
        
        # Check for a name in the middle and remove it if present
        if re.search('https://www.amazon.com/[\w-]*/dp/\w*/' , recent_value):
            recent_value = re.sub('/[\w-]*/dp/', '/dp/', recent_value, 1) 
            
        pyperclip.copy(recent_value)
        
    # Is it an eBay product link? If so, cut off the faf
    match_object = re.search('https://www.ebay.com/itm/\d+' , recent_value)
    if match_object:
        print("eBay product URL detected, reformatting")
        recent_value = match_object.group()
        
        pyperclip.copy(recent_value)
    
    # Is it an Etsy product link? If so, cut off the faf
    match_object = re.search('https://www.etsy.com/listing/\d+/' , recent_value)
    if match_object:
        print("Etsy product URL detected, reformatting")
        recent_value = match_object.group()
        
        pyperclip.copy(recent_value)    
    