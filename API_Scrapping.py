########################################################|DEFINITION|########################################################
import csv
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import datetime, timedelta
from GUI import GUI
from scrapper import Scrapper
###########################################################|CODE|############################################################


########################################################|LAUNCHER|########################################################
class Api_Launcher : 
    def __init__(self) -> None:
        self.scrapper = Scrapper()
        self.GUI_root = tk.Tk()
        self.GUI = GUI(self.GUI_root)
