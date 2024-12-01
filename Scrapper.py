#############################################################################################
#                                                                                           #
#                                     DEFINITION                                            #
#                                                                                           #
#############################################################################################

import requests
import pandas as pd
from bs4 import BeautifulSoup


#############################################################################################
#                                                                                           #
#                                         CODE                                              #
#                                                                                           #
#############################################################################################

class Scrapper:
    def __init__(self, db_manager):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        self.urlbase = "https://www.drf.com/"
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
        self.timeout = 0
        self.db_manager = db_manager


    def get_track_url(self, Track_ID:str, Date, Finished:bool):
        print("Getting URL...")
        if Finished:
            track_url = self.urlbase + "race-results/"
        else : 
            track_url = self.urlbase + "race-entries/"
        track_url += f"tracks/{Track_ID}/country/USA/date/{Date}"
        return track_url
    #For BlackBox : Let's create a function     
    def get_race_info(self, track_url: str, track:str, date:str, Finished:bool):
        index=0
        all_races_data={
            "Track":track,
            "Date":date,
            "Finished": Finished,
            "Race_Id": f"{self.track_list_ID_US[track]}{date}{index}",
            "RaceElmt": []
        }
        try:
            print(f"Getting Race Results of {track} the {date}...")
            page = requests.get(track_url, headers=self.header)
            page.raise_for_status()
            soup = BeautifulSoup(page.text, 'html.parser')
            race_info = soup.find_all('div', class_='entriesRaceDtlsBody')
            for race in race_info:
                horses = race.find_all('li', class_="horseDetail")
                race_data = []
                cursor = self.database_manager.connection.cursor()
                cursor.execute('''
                    INSERT INTO courses (id_course, date, track_id, status)
                    VALUES (?, ?, ?, ?)
                ''', (all_races_data["Race_Id"], date, track, 'completed' if Finished else 'scheduled'))
                for horse in horses:
                    horse_data = {
                        "Horse Num": horse.find('span', class_='valResDtlsNum').text.strip(),
                        "Horse Name": horse.find('span', class_='valResDtlsHorse').text.strip(),
                        "Horse Jockey": horse.find('span', class_='valResDtlsJockey').text.strip(),
                        "Horse Win": horse.find('span', class_='valResDtlsWin').text.strip(),
                        "Horse Place": horse.find('span', class_='valResDtlsPlace').text.strip(),
                        "Horse Show": horse.find('span', class_='valResDtlsShow').text.strip(),
                    }
                    race_data.append(horse_data)
                all_races_data["RaceElmt"].append(race_data)
            
        except requests.RequestException as e:
            print(f"HTTP Request failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        pass

    def testscrape_data(self, track:str, date:str, Finished:bool):
        url = self.get_track_url(Track_ID=self.track_list_ID_US[track], Date=date, Finished=Finished)
        page = requests.get(url, headers=self.header)
        page.raise_for_status()
        soup = BeautifulSoup(page.text, 'html.parser')
        
        return soup.prettify()