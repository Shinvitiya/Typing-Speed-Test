import requests
import random

URL = "https://baconator-bacon-ipsum.p.rapidapi.com/"
API_KEY = "xxxxxxxxxxxxxxxxxxxxxx"  # Enter you API key here

API_HOST = "baconator-bacon-ipsum.p.rapidapi.com"

parameters = {"type": "all-meat",
              "paras": "6"}

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

response = requests.get(url=URL, headers=headers, params=parameters)


class TextGenerator:
    def __init__(self):
        word_list = response.json()
        random.shuffle(word_list)
        words = "".join(word_list)
        self.text = words
