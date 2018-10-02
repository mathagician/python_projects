import urllib.request
import json
import webbrowser
import os
import time
from random import randint

URL = "https://api.vk.com/method/wall.get?owner_id=-120734334&offset=20&count=100" \
      "&access_token=3049c2d53049c2d53049c2d5683016bbd5330493049c2d56a4140962333381555430fb8&v=V"
FILE_NAME = "tmp_picture.jpg"

try:
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    try:
        photo = data['response'][randint(1, 100)]['attachment']['photo']['src_xbig']
        urllib.request.urlretrieve(photo, FILE_NAME)
    except Exception:
        photo = data['response'][randint(1, 100)]['attachment']['photo']['src_xbig']
        urllib.request.urlretrieve(photo, FILE_NAME)
    webbrowser.open(FILE_NAME)
    time.sleep(10)
    os.remove(FILE_NAME)
except Exception:
    print("Something went wrong :(")
    print("Try again, plz")
