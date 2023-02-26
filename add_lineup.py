import os
from rotate import rotate
from tkinter import *


class add_lineup:
    def __init__(self, player_num):
        # The Creation of this class

        # Create the Main window for all the info
        self.output_value = None
        self.window = Tk()
        self.player_num = player_num
        self.player_array = [0 for x in range(self.player_num)]
        self.player_input = [0 for x in range(20)]
        self.player_button = [0 for x in range(20)]
        self.default_padx = 10

        self.create_screen()
        self.create_buttons()
        self.run()

    def create_screen(self):
        # Sets the resolution of the window
        self.window.geometry('800x600')

        # Set Title of window
        self.window.title("Lineup Program")

        # Welcome text at top
        l_title = Label(self.window, text="Welcome to Lineup Program", font=('', 35))
        l_title.grid(row=0, column=0, columnspan=100, padx=self.default_padx, pady=(20, 5))
        # Into Label and directors
        l_title_l = Label(self.window, text="Insert Director text here", font=('', 12))
        l_title_l.grid(row=1, column=0, columnspan=100, padx=self.default_padx, pady=(5, 20), sticky='W')

    def create_buttons(self):
        for a in range(self.player_num):
            self.add_button(a)
        # Selection button 0
        self.player_button[self.player_num + 1] = Button(self.window, text="Output", font=('', 12),
                                                         command=lambda: self.output_value)
        self.player_button[self.player_num + 1].grid(row=self.player_num + 3, column=0, padx=5, pady=(1, 10),
                                                     sticky='W',
                                                     ipadx=self.default_padx, ipady=5)

    def add_button(self, num):
        # Selection input 0
        self.player_input[num] = Entry(self.window, font=('', 10))
        self.player_input[num].grid(row=num + 2, column=1, padx=self.default_padx, sticky='W')
        # Selection button 0
        self.player_button[num] = Button(self.window, text="Add Player " + str(num), font=('', 12),
                                         command=lambda: self.add_player_to_array(num))
        self.player_button[num].grid(row=num + 2, column=0, padx=5, pady=(1, 10), sticky='W', ipadx=self.default_padx,
                                     ipady=5)

    def add_player_to_array(self, num):
        self.player_array[num] = self.player_input[num].get()
        self.player_button[num].configure(bg="green")

    def output(self):
        self.output_value = rotate(player_array=self.player_array)

    def run(self):
        # Says our method is ready to run
        self.window.mainloop()
