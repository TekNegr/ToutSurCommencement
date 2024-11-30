######################DEFINITION#######################################

import csv
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import datetime, timedelta

######################CODE#######################################

class Scrapper:
    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        self.url = "https://www.drf.com/"
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
      
###########################GETTERS#####################################
    #fonction pour récuperer l'URL d'une course  
    def get_track_url(self, Track_ID:str, Date, Finished:bool):
        print("Getting URL...")
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
    
    def scrap_race_results(self, url, race_id, track_id):
        #Function to fecth races results data on a specific url track
        try:
            page = requests.get(url, headers=self.header)
            page.raise_for_status()
            soup = BeautifulSoup(page.text, 'html.parser')
            
            race_elements = soup.find("div", class_="entriesDtlsbody")
            if not race_elements:
                raise ValueError("No race details found on the page.")
            
            race_header = soup.find("div", class_="entriesRaceHeader", id=race_id)
            if not race_header:
                raise ValueError(f"Race header with ID {race_id} not found.")

            Race_data = {
            "track_id": track_id,
            "race_id": race_id,
            "Winning_horses": []
            }
            
            horse_elements = race_elements.find_all("li", class_="horseDetails")
            for index, horse in enumerate(horse_elements[:3]):
                number = int(horse.find("span", class_="valResDtlsNum").text.strip())
                name = horse.find("span", class_="valResDtlsHorse").text.strip()
                jockey = horse.find("span", class_="valResDtlsJockey").text.strip()
                win = int(horse.find("span", class_="valResDtlsWin").text.strip())
                place = int(horse.find("span", class_="valResDtlsPlace").text.strip())
                show = int(horse.find("span", class_="valResDtlsShow").text.strip())
                
                Race_data["Winning_horses"].append({
                    "horse_spot": index + 1,
                    "number": number,
                    "name": name,
                    "jockey": jockey,
                    "win": win,
                    "place": place,
                    "show": show
                })
            
            return Race_data
        except requests.RequestException as e:
            print(f"HTTP Request failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    #Fonction pour récuperer la data de toutes les courses d'une seule journée
    def scrap_day_races(self, url, track_id, date):
        print(f"Scrapping races from {date}...")
        try : 
            print("Url valid, scrapping...")
            print(url)
            page = requests.get(url, headers=self.header)
            page.raise_for_status()
            print("Status code:", page.status_code)
            soup = BeautifulSoup(page.text, 'html.parser')
            all_race_elements = soup.find_all("div", class_="entriesRaceDtls")
            races_data_list = []
            print("All races:",all_race_elements)
            for index, race in enumerate(all_race_elements):
                race_id = f"Race{index + 1}"
                Race_data = {
                "date": date,
                "track_id": track_id,
                "race_id": race_id,
                "Winning_horses": []
                }
                race_elmt = race.find("div", class_="entriesDtlsbody")
                print("Race:",race_elmt)
                horse_elements = race_elmt.find_all("li", class_="horseDetails")
                for index, horse in enumerate(horse_elements):
                    print("horse:",horse_elements)
                    number = int(horse.find("span", class_="valResDtlsNum").text.strip())
                    name = horse.find("span", class_="valResDtlsHorse").text.strip()
                    jockey = horse.find("span", class_="valResDtlsJockey").text.strip()
                    win = int(horse.find("span", class_="valResDtlsWin").text.strip())
                    place = int(horse.find("span", class_="valResDtlsPlace").text.strip())
                    show = int(horse.find("span", class_="valResDtlsShow").text.strip())
                    
                    Race_data["Winning_horses"].append({
                        "horse_spot": index + 1,
                        "number": number,
                        "name": name,
                        "jockey": jockey,
                        "win": win,
                        "place": place,
                        "show": show
                    })
                    print(f"Horse : {number} {name} / {jockey} / win : {win}/ place : {place} / show : {show}")
                if Race_data:
                    print("data fetching successful, appending...")
                    races_data_list.append(Race_data)
            print("Returning data") 
            return races_data_list
        except requests.RequestException as e:
            print(f"HTTP Request failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def scrap_future_races(self, url):
        #Function to fecth races data
        
        
        
        pass


###########################MANIPULATORS#####################################
    
    def save_csv(self, data, date, track_id):
        print("Saving As CSV...")
        race_name = f"{track_id}_{date}.csv"
        with open(race_name, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['track_id','date','race_id', 'winner1_spot', 'winner1_hname', 'winner1_hnum','winner1_hjockey','winner1_win','winner1_place','winner1_show',  'winner2_spot', 'winner2_hname', 'winner2_hnum','winner2_hjockey','winner2_win','winner2_place','winner2_show',  'winner3_spot', 'winner3_hname', 'winner3_hnum','winner3_hjockey','winner3_win','winner3_place','winner3_show'])
            for race in data:
                writer.writerow([track_id, date, race["race_id"], race["Winning_horses"][0]["horse_spot"],race["Winning_horses"][0]["name"],race["Winning_horses"][0]["number"],race["Winning_horses"][0]["jockey"],race["Winning_horses"][0]["win"],race["Winning_horses"][0]["place"],race["Winning_horses"][0]["show"], race["Winning_horses"][1]["horse_spot"],race["Winning_horses"][1]["name"],race["Winning_horses"][1]["number"],race["Winning_horses"][1]["jockey"],race["Winning_horses"][1]["win"],race["Winning_horses"][1]["place"],race["Winning_horses"][1]["show"], race["Winning_horses"][2]["horse_spot"],race["Winning_horses"][2]["name"],race["Winning_horses"][2]["number"],race["Winning_horses"][2]["jockey"],race["Winning_horses"][2]["win"],race["Winning_horses"][2]["place"],race["Winning_horses"][2]["show"]])
        csvfile.close()




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
      
def test_scrap_day_races(scraper_instance: Scrapper, track_id, date):
    print("Testing scrap_day_races...")
    try:
        url = scraper_instance.get_track_url(track_id, date, True)
        print(url)
        race_data = scraper_instance.scrap_day_races(url, track_id, date)
        if race_data:
            print("Success! Here’s the data:")
            for race in race_data:
                print(f"Race ID: {race['race_id']}, Date: {race['date']}, Track ID: {race['track_id']}")
                for horse in race["Winning_horses"]:
                    print(f"  Horse Name: {horse['name']}, Jockey: {horse['jockey']}, Win: {horse['win']}")
        else:
            print("No races found or data is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def main():
    # root = tk.Tk()
    # GUI = GUI(root)
    # start_date = datetime(2024,1,1)
    # end_date = datetime(2024,2,1)
    Scr_App = Scrapper()
    test_scrap_day_races(Scr_App, "CD", "11-25-2024")
    # root.mainloop()
    
if __name__ == "__main__":
    main()