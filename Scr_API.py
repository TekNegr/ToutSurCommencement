#############################################################################################
#                                                                                           #
#                                     DEFINITION                                            #
#                                                                                           #
#############################################################################################



#############################################################################################
#                                                                                           #
#                                         CODE                                              #
#                                                                                           #
#############################################################################################

class ScrAPI:
    def __init__(self):
        print("Launching API...")
        from API_v2.FRONT import API_GUI, Screens
        from API_v2.BACK import Scrapper, DatabaseManager
        
        self.db_manager = DatabaseManager()
        self.scrapper = Scrapper(self.db_manager)
        screens = Screens
        GUI = API_GUI(scrapper=self.scrapper, db_manager=self.db_manager)
        GUI.run()
       
