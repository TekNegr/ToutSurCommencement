########################################################|DEFINITION|########################################################

import csv
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from datetime import datetime, timedelta

###########################################################|CODE|############################################################

class Screen(tk.Frame):
    def __init__(self, parent, title="", **kwargs):
        super().__init__(parent.root, **kwargs)
        self.parent = parent
        self.frame = tk.Frame(parent.root)
        self.title = title
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the screen. To be overridden by subclasses."""
        raise NotImplementedError("Subclasses should implement this method.")

    def create_header(self, header_title):
        print("creating header")
        headerframe = tk.Frame(self.frame)
        tk.Button(headerframe, text="Home", command=lambda: self.parent.show_screen(HomeScreen)).pack()
        tk.Label(headerframe, text=header_title, font=("Arial", 24)).pack()
        return headerframe
        

    def show(self):
        """Show the screen."""
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        """Hide the screen."""
        self.frame.pack_forget()
        
class HomeScreen(Screen):
    """Home screen."""
    def create_widgets(self):
        tk.Label(self.frame, text="Bienvenue! Prêt à parier?").pack()
        btngrid = tk.Frame(self.frame)
        readBtn = tk.Button(btngrid, text="STATS READ", command=lambda:self.parent.show_screen(StatsReadScreen)).grid(row=0,column=0, padx=20, pady=20)
        predBtn = tk.Button(btngrid, text="PREDICTION", command=lambda:self.parent.show_screen(StatsPredictionScreen)).grid(row=0,column=1, padx=20, pady=20)
        SchBtn = tk.Button(btngrid, text="SCHEMAS", command=lambda:self.parent.show_screen(SchemasScreen)).grid(row=1,column=0, padx=20, pady=20)
        CredBtn = tk.Button(btngrid, text="CREDITS", command=lambda:self.parent.show_screen(CreditsScreen)).grid(row=1,column=1, padx=20, pady=20)
        TestBtn = tk.Button(btngrid, text="TEST DATA", command=lambda:self.parent.show_screen(TestScreen)).grid(row=2,column=0, padx=20, pady=20)
        btngrid.pack()

class StatsReadScreen(Screen):
    """Stats Read screen."""
    def create_widgets(self):
        headerFrame = self.create_header("Stats Read")
        
        tk.Button(headerFrame, text="Home", command=lambda: self.parent.show_screen(HomeScreen)).pack()
        tk.Label(headerFrame, text="STATS READER").pack()
        # Add content for Stats Read screen here
        tk.Label(self, text="Data for Stats Read").pack()
        
class StatsPredictionScreen(Screen):
    """Stats Prediction screen."""
    def create_widgets(self):
        self.create_header("Stats Prediction")
        


        tk.Button(headerFrame, text="Home", command=lambda: self.parent.show_screen(HomeScreen)).pack()
        tk.Label(headerFrame, text="STATS PREDICTION").pack()
        
        tk.Label(self, text="Data for Stats Prediction").pack()
    
class SchemasScreen(Screen):
    def create_widgets(self):
        headerFrame = self.create_header("Schemas")
        headerFrame.pack()


        tk.Button(headerFrame, text="Home", command=lambda: self.parent.show_screen(HomeScreen)).pack()
        tk.Label(headerFrame, text="STATS PREDICTION SCHEMA").pack()
        
        tk.Label(self, text="Data for Stats Prediction").pack()
        
class CreditsScreen(Screen):
    def create_widgets(self):
        headerFrame = self.create_header("Credits")
        headerFrame.pack()

        
        tk.Button(headerFrame, text="Home", command=lambda: self.parent.show_screen(HomeScreen)).pack()
        tk.Label(headerFrame, text="CREDITS").pack()
        
        tk.Label(self, text="Makers of this project").pack()
        
class TestScreen(Screen):
    def create_widgets(self):
        headerFrame = self.create_header("Tester")
        headerFrame.pack()

        
        tk.Button(headerFrame, text="Home", command=lambda: self.parent.show_screen(HomeScreen)).pack()
        tk.Label(headerFrame, text="TEST").pack()
        


class GUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.setup_window()
        self.current_screen: Screen = None
        self.show_screen(HomeScreen)  # Show the home screen initially
        self.root.mainloop()
        
    def setup_window(self):
        """Setup the main window for the application."""
        self.root.geometry("1280x720")
        self.root.title("TOUT SUR COMMENCEMENT")
        
    def show_screen(self, screen_class: Screen):
        print("changing screens")
        """Show the specified screen class and hide the current one."""
        if self.current_screen is not None:
            print("hiding")
            self.current_screen.hide()  # Hide the current screen
        self.current_screen = screen_class(self)  # Create a new instance of the screen
        self.current_screen.show()