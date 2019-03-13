# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:47:21 2018

@author: lenovo
"""
from bs4 import BeautifulSoup
import time
import sys
import requests
from pprint import pprint
import json


# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)


# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)




