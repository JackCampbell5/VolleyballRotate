import os
from tkinter import *


class rotate:
    def __init__(self, player_array):
        # The Creation of this class

        # Create the Main window for all the info
        self.window = Tk()
        self.player_array = player_array
        self.default_padx = 10

        self.create_screen()
        self.run()

    def create_screen(self):
        # Sets the resolution of the window
        self.window.geometry('800x600')

        # Set Title of window
        self.window.title("Line2 Program")

        # Welcome text at top
        l_title = Label(self.window, text="Welcome to Lineup Program", font=('', 35))
        l_title.grid(row=0, column=0, columnspan=100, padx=self.default_padx, pady=(20, 5))
        # Into Label and directors
        l_title_l = Label(self.window, text="Insert Director text here", font=('', 12))
        l_title_l.grid(row=1, column=0, columnspan=100, padx=self.default_padx, pady=(5, 20), sticky='W')

    def run(self):
        # Says our method is ready to run
        self.window.mainloop()
