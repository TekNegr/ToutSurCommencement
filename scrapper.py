########################################################|DEFINITION|########################################################

import csv
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import datetime, timedelta

###########################################################|CODE|############################################################

class Scrapper:
    def __init__(self) -> None:
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        self.urlbase = "https://www.drf.com/"
        # self.page : requests
        self.quotes = []
        # self.soup : BeautifulSoup
        #Liste des ID des tracks
        self.track_list_ID_US = {
            "Churchill Downs": "CD",
            "Delta Downs":"DED",
            "Evangeline Downs": "EVD",
            "Finger Lakes":"FL",
            "Hollywood Casino Charles Town race":"CT",
            "Mahoning Valley Race Course":"MVR",
            "Mountaineer Casino Race & Resort":"MNR",
            "Parx Race":"PRX",
            "Penn National":"PEN",
            "Tampa Bay Downs":"TAM",
            "Turf Paradise":"TUP"}

