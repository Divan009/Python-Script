# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 00:09:43 2018

@author: lenovo
"""


from urllib.request import urlopen 
from bs4 import BeautifulSoup 
from urllib.error import HTTPError
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read()) 
print(bsObj.nonExistentTag) 
# =============================================================================
# try:
#    html = urlopen("http://www.pythonscraping.com/pages/page1.html") 
# except HTTPError as e:
#     print(e)
# else:    
#     bsObj = BeautifulSoup(html.read()) 
#     print(bsObj.nonExistentTag) 
# =============================================================================
print(bsObj.h1) 