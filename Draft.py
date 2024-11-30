
import csv
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import datetime, timedelta

class GUI: 
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("TOUT SUR COMMENCEMENT")
        self.screens = {}
        self.chosen_screen : str
        self.init_screens()
        self.update_dispaly("home")
        self.root.mainloop()
        
    def init_screens(self):
        self.screens["home"] = tk.Frame(self.root)
        self.init_home()
    
        self.screens["stats_read"] = tk.Frame(self.root)
        self.init_stats_read()
        
        self.screens["stats_prediction"] = tk.Frame(self.root)
        self.init_stats_prediction()
        
        self.screens["schemas"]= tk.Frame(self.root)
        self.init_schemas()
        
        self.screens["credits"] = tk.Frame(self.root)
        self.init_credits()
        
        self.screens["test data"] = tk.Frame(self.root)
        self.init_test_data()
        
    def init_home(self):
        tk.Label(self.screens["home"], text="Bienvenue! Prêt à parier?").pack()
        btngrid = tk.Frame(self.screens["home"])
        readBtn = tk.Button(btngrid, text="STATS READ", command=lambda:self.update_dispaly(screen_name="stats_prediction")).grid(row=0,column=0, padx=20, pady=20)
        predBtn = tk.Button(btngrid, text="PREDICTION", command=lambda:self.update_dispaly(screen_name="stats_prediction")).grid(row=0,column=1, padx=20, pady=20)
        SchBtn = tk.Button(btngrid, text="SCHEMAS", command=lambda:self.update_dispaly(screen_name="stats_prediction")).grid(row=1,column=0, padx=20, pady=20)
        CredBtn = tk.Button(btngrid, text="CREDITS", command=lambda:self.update_dispaly(screen_name="stats_prediction")).grid(row=1,column=1, padx=20, pady=20)
        TestBtn = tk.Button(btngrid, text="TEST DATA", command=lambda:self.update_dispaly(screen_name="stats_prediction")).grid(row=2,column=0, padx=20, pady=20)
        btngrid.pack()
        
        
    def init_stats_read(self):
        headerFrame = self.init_header("stats_read")
        headerFrame.pack()
     
        
    def init_stats_prediction(self):
        headerFrame = self.init_header("stats_prediction")
        headerFrame.pack()
     
        
    def init_schemas(self):
        headerFrame = self.init_header("schemas")
        headerFrame.pack()
     
    def init_credits(self):
        headerFrame = self.init_header("credits")
        headerFrame.pack()
     
        
    def init_test_data(self):
        headerFrame = self.init_header("test data")
        headerFrame.pack()
     
    def init_header(self, screen_name: str):
        headerFrame = tk.Frame(self.screens[screen_name])
        tk.Button(headerFrame, text="Home", command=lambda:self.update_dispaly("home"))
        tk.Label(headerFrame, text=screen_name)
        return headerFrame
        
       
    def update_dispaly(self, screen_name:str=None, screen: tk.Frame=None):
        print(f"Updating screen: {screen_name}")
        self.clear_frames()
        if screen and not screen_name :
            screen.pack()
        elif screen_name and not screen:
            self.chosen_screen = screen_name
            self.screens[screen_name].pack()
        
    def clear_frames(self):
        for screen in self.screens:
            self.screens[screen].pack_forget()
