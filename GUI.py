#############################################################################################
#                                                                                           #
#                                     DEFINITION                                            #
#                                                                                           #
#############################################################################################

import tkinter as tk
from tkinter import ttk, messagebox
from API_v2.FRONT import Screens
from API_v2.BACK import Scrapper, DatabaseManager
#############################################################################################
#                                                                                           #
#                                         CODE                                              #
#                                                                                           #
#############################################################################################

class API_GUI:
    def __init__(self, scrapper : Scrapper, db_manager = DatabaseManager) :
        self.root = tk.Tk()
        self.root.title("TOUT SUR COMMENCEMENT")
        self.root.minsize(400, 300)
        
        self.scrapper = scrapper
        self.db_manager = db_manager
        
        self.screen_manager = Screens.ScreenManager(self)
        self.screen_manager.show_screen("HomeScreen")
        
    
    def run(self):
        print("running API...")
        self.root.mainloop()