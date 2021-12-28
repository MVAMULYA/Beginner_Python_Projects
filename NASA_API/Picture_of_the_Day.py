#!usr/bin/env Python

from datetime import date
import requests
import cv2 as cv
import numpy as np

API_KEY = "Y8Z3Z03xXoR0qrAHCNbX8DJEpn7AJDiGuI1r6TLI"
endpoint = "https://api.nasa.gov/planetary/apod"
year, month, dt = map(int, input("enter year, month, and date seperated by spaces for the day of picture \n").split())
date = date(year,month,dt)
thumbs = True
params = {"api_key" : API_KEY, "date" : date, "thumbs" : thumbs}
response = requests.get(endpoint, params= params)

if response.json()['media_type'] == 'image':
    url = response.json()['url']
else:
    url = response.json()['thumbnail_url']

request_url = requests.get(url)
image = np.asarray(bytearray(request_url.content))
image = cv.imdecode(image,cv.IMREAD_COLOR)
title = response.json()['title']
cv.imshow(title, image)
k = cv.waitKey(0)
if k:
    cv.destroyAllWindows()






