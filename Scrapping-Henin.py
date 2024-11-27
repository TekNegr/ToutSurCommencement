######################DEFINITION#######################################

import csv
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import datetime, timedelta

######################CODE#######################################

class Scrapper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        self.url = "https://www.drf.com/"
        self.page = requests.get(self.url, headers=self.headers)
        self.quotes = []
        
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
      
###########################GETTERS#####################################
    #fonction pour récuperer l'URL d'une course  
    def get_track_url(self, Track_ID:str, Date, Finished:bool):
        if Finished:
            track_url = self.url + "race-results/"
        else : 
            track_url = self.url + "race-entries/"
        track_url += f"tracks/{Track_ID}/country/USA/date/{Date}"
        return track_url
        
        
###########################SETTERS#####################################
    
    #Fonction pour traverser les dates 
    def scroll_through_dates(self, date_start, date_finish, Track_ID:str, Finished:bool):
        if date_start > date_finish:
            raise ValueError("date_start must be less than or equal to date_finish")
        current_date = date_start
        while current_date <= date_finish:
            url = self.get_track_url(Track_ID, current_date.strftime('%m-%d-%Y'), Finished)
            
            if url:
                if Finished:
                    self.scrap_race_results(url)
                else : 
                    self.scrap_future_races(url)
            else:
                print(f"No URL found for {current_date.strftime('%m-%d-%Y')}")
            
            current_date += timedelta(days=1)
    
    def scrap_race_results(self, url):
        #Function to fecth races results data on a specific url track
        
        #For BlackBox : Each Track Has multiple races. I want this function to be able to fetch for each race the 3 winning horses.
#        Races are stored in a div with the class "entriesRaceDtls"
#        each race div has a class "raceHeader" with an (e.g:id="Race7")
#        each race has an ul with the class dataTable with the data of interest, with 3 li of the class "horseDetails"
#        
        
        pass
    
    def scrap_future_races(self, url):
        #Function to fecth races data
        
        
        
        pass


###########################MANIPULATORS#####################################
    
    def save_csv(self):
        #Function to save data as a csv
        pass




class GUI:
    #For BlackBox : Let's create a simple GUI with 2 windows interchangeable (and a home to access both): Teams_Stats and Pronostics 
    def __init__(self, root:tk.Tk) -> None:
        self.root = root
        self.root.title("BET ON COMMENCEMENT")
        
        self.teams_stats_frame = tk.Frame(self.root)
        self.pronostics_frame = tk.Frame(self.root)
        self.home_frame = tk.Frame(self.root)
        
        self.init_home()
        
    def init_home(self):
        
        self.clear_frames()
        
        # Create buttons for navigation
        if not hasattr(self, 'teams_stats_button') or not hasattr(self, 'pronostics_button') :
            self.teams_stats_button = tk.Button(self.home_frame, text="Teams Stats", command=self.show_teams_stats)
            self.pronostics_button = tk.Button(self.home_frame, text="Pronostics", command=self.show_pronostics)
            self.teams_stats_button.pack(pady=10)
            self.pronostics_button.pack(pady=10)

        
        self.home_frame.pack(fill="both", expand=True)
      
    def show_teams_stats(self):
        # Clear all frames and show Teams Stats
        self.clear_frames()
        self.teams_stats_frame.pack(fill="both", expand=True)
        
        
        
        # Example content for Teams Stats
        if not hasattr(self, 'stats_label'):
            self.stats_label = tk.Label(self.teams_stats_frame, text="Teams Stats")
            self.stats_label.pack(pady=20)

        if not hasattr(self, 'sback_button'):
            self.sback_button = tk.Button(self.teams_stats_frame, text="Back to Home", command=self.init_home)
            self.sback_button.pack(pady=10)

    def show_pronostics(self):
        # Clear all frames and show Pronostics
        self.clear_frames()
        self.pronostics_frame.pack(fill="both", expand=True)
        
        # Example content for Pronostics
        if not hasattr(self, 'prono_label'):
            self.prono_label = tk.Label(self.pronostics_frame, text="Pronostics. Work in Progress")
            self.prono_label.pack(pady=20)

        if not hasattr(self, 'pback_button'):
            self.pback_button = tk.Button(self.pronostics_frame, text="Back to Home", command=self.init_home)
            self.pback_button.pack(pady=10)  
        
    def clear_frames(self):
        self.teams_stats_frame.pack_forget()
        self.pronostics_frame.pack_forget()
        self.home_frame.pack_forget()
        
######################LAUNCHER#######################################
      
        
def main():
    root = tk.Tk()
    # GUI = GUI(root)
    start_date = datetime(2024,1,1)
    end_date = datetime(2024,2,1)
    Scr_App = Scrapper()
    Scr_App.scroll_through_dates(start_date, end_date)
    # root.mainloop()
    
if __name__ == "__main__":
    main()