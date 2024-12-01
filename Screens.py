#############################################################################################
#                                                                                           #
#                                     DEFINITION                                            #
#                                                                                           #
#############################################################################################
import tkinter as tk
from tkinter import ttk, messagebox
#from API_v2.FRONT import API_GUI

#############################################################################################
#                                                                                           #
#                                         CODE                                              #
#                                                                                           #
#############################################################################################

class ScreenManager:
    def __init__(self, gui):
        from API_v2.FRONT import API_GUI

        self.gui : API_GUI  = gui # Reference to the main GUI
        self.current_screen = None
        self.screens = {
            "HomeScreen": HomeScreen,
            "ScrapingScreen": ScrapingScreen,
            "TestScreen": TestingScreen,
            "StatsScreen": StatsReaderScreen
        }

    def show_screen(self, screen_name:str):
        """Transition to a specific screen."""
        print(f"showing screen:{screen_name}")
        if self.current_screen:
            self.current_screen.destroy()  # Remove current screen
        screen_class = self.screens.get(screen_name)
         
        if screen_class:
            print(f"{screen_name} selected")
            self.current_screen = screen_class(self)  # Instantiate the screen class
            self.current_screen.pack()  # Pack the new screen
            print(f"Packing {self.current_screen}...")
        else:
            print(f"Screen {screen_name} not found.")

        
class BaseScreen(tk.Frame):
    """A base class for all screens."""
    def __init__(self, manager: ScreenManager):
        
        super().__init__(manager.gui.root)
        
        self.manager = manager
        
    def getScreenHeader(self, Screen_title:str):
        """Create a header for the screen."""
        self.header = tk.Frame(self)
        homeBtn = tk.Button(self.header, text="Home", command=self.goHome)
        headerTitle = tk.Label(self.header, text = Screen_title)
        homeBtn.pack(side=tk.LEFT, padx=10)
        headerTitle.pack(side=tk.RIGHT, padx=10)
        return self.header
        
    def goHome(self):
        self.manager.show_screen("HomeScreen")
   
    def setup_widgets(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def refresh_screen(self):
        print("Refreshing page...")
        for widget in self.winfo_children():  # Destroy all existing widgets
            widget.destroy()
        self.setup_widgets()
        
class HomeScreen(BaseScreen):
    def __init__(self, manager):
        super().__init__(manager)
        self.setup_widgets()
        
        
    def setup_widgets(self):
        label = tk.Label(self, text="Welcome to the Home Screen")
        label.pack(pady=10)
        
        btn_test = tk.Button(self, text="Go to testing screen", command=lambda: self.manager.show_screen("TestScreen"))
        btn_test.pack(pady=10)

        # Button to navigate to another screen
        btn_scraping = tk.Button(self, text="Go to Scraping Screen",
                                 command=lambda: self.manager.show_screen("ScrapingScreen"))
        btn_scraping.pack(pady=10)
        
        btn_read = tk.Button(self, text="Go to Stats Reader screen", command=lambda: self.manager.show_screen("StatsScreen"))
        btn_read.pack(pady=10)
     
class ScrapingScreen(BaseScreen):
    def __init__(self, manager):
        super().__init__(manager)
        self.setup_widgets()
        
    def setup_widgets(self):
        self.getScreenHeader("Scraping Screen").pack(pady=10)

        self.text_display = tk.Text(self, wrap="word", height=20, width=80)
        self.text_display.pack(pady=10)

        # Button to trigger scraping
        btn_scrape = tk.Button(self, text="Start Scraping",
                               command=self.start_scraping)
        btn_scrape.pack()


    def start_scraping(self):
        """Trigger the scraping process via the GUI."""
        try:
            data = self.manager.gui.scrapper.scrape_data("https://example.com")
            self.manager.gui.db_manager.save_data(data)
            messagebox.showinfo("Success", "Data scraped and saved!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
class StatsReaderScreen(BaseScreen):
    def __init__(self, manager):
        super().__init__(manager)
        self.setup_widgets()
        
    def setup_widgets(self):
        self.getScreenHeader("Stats reader Screen").pack(pady=10)

        self.table_frame = tk.Frame(self)
        self.table_frame.pack(pady=10)
       
        self.columns = ("Track", "Date", "Horse", "Jockey","Win", "Place", "Show")
        self.tree = ttk.Treeview(self.table_frame, columns=self.columns, show="headings")
        
        for col in self.columns:
            self.tree.heading(col, text =col)
            self.tree.column(col, anchor="center")
            
        self.scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        
        self.tree.pack(side=tk.LEFT)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def populate_table(self, data):
        pass
            
class TestingScreen(BaseScreen):
    def __init__(self, manager):
        super().__init__(manager)
        self.setup_widgets()
        
    def setup_widgets(self):
        """Set up the screen's widgets."""
        # Title label
        self.getScreenHeader("Testing Screen").pack(pady=10)
        
        
        # Text area to display data
        self.text_display = tk.Text(self, wrap="word", height=20, width=80)
        self.text_display.pack(pady=10)

        btnFrame = tk.Frame(self)

        # Scraping button
        test_button = tk.Button(btnFrame, text="Fetch Data", command=self.start_test)
        test_button.grid(row=0, column=0, padx=10, pady=10)
        
        refresh_button = tk.Button(btnFrame, text="Refresh", command=self.refresh_screen)
        refresh_button.grid(row=0, column=1, padx=10, pady=10)
        
        btnFrame.pack(pady=10)
    def start_test(self):
        # Test the scraping process
        try:
            response = self.manager.gui.scrapper.testscrape_data("Churchill Downs", "11-28-2024", True)
            # response = self.manager.gui.scrapper.get_track_url(self.manager.gui.scrapper.track_list_ID_US["Churchill Downs"], "11-28-2024", True)
            self.text_display.delete("1.0", tk.END)
            self.text_display.insert(tk.END, response)
            messagebox.showinfo("Success", "Data scraped and displayed!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # def refresh_screen(self):super