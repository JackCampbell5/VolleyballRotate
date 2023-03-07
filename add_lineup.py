from tkinter import *


class add_lineup:
    def __init__(self, player_num, position_array):
        # The Creation of this class

        # Final values of the program
        self.default_padx = 10
        self.position_array = ["Server", "Hitter", "Hitter", "Setter", "Setter", "Setter"]

        # The window
        self.window = Tk()

        # The checkbox for if you want labels
        self.labels = False
        self.checkbox_output = None
        self.labels_input = [None for x in range(2)]

        # Player number
        self.player_num = -1
        self.player_number_change_entry = [None for x in range(3)]
        self.num_info_row = 4

        # The arrays containing the players
        self.default_array = None
        self.player_array = None
        self.player_input = None
        self.player_button = None
        self.player_labels = None
        self.position_array_labels = None
        self.output_value = None

        # Create the screen
        self.create_screen()

        # Creates the feild for player numbers
        self.get_player_number()

        # Creates the labels input
        self.player_labels_checkbox()

        # Runs the program
        self.run()

    def create_screen(self):
        # Sets the resolution of the window
        self.window.geometry('1000x600')

        # Set Title of window
        self.window.title("Lineup Program")

        # Welcome text at top
        l_title = Label(self.window, text="Welcome to Lineup Program", font=('', 35))
        l_title.grid(row=0, column=0, columnspan=100, padx=self.default_padx, pady=(20, 5))
        # Into Label and directors
        l_title_l = Label(self.window, text="Insert Director text here", font=('', 12))
        l_title_l.grid(row=1, column=0, columnspan=100, padx=self.default_padx, pady=(5, 20), sticky='W')

    def get_player_number(self):
        self.player_number_change_entry[0] = Label(self.window, text="Player #:", font=('', 12))
        self.player_number_change_entry[0].grid(row=2, column=0, padx=self.default_padx, pady=(5, 20),
                                                sticky='W')
        self.player_number_change_entry[1] = Entry(self.window, font=('', 10))
        self.player_number_change_entry[1].grid(row=2, column=1, padx=self.default_padx, sticky='W')
        # Selection button 0
        self.player_number_change_entry[2] = Button(self.window, text="Start", font=('', 12),
                                                    command=lambda: self.create_player_inputs())
        self.player_number_change_entry[2].grid(row=2, column=2, padx=5, pady=(1, 10), sticky='W',
                                                ipadx=self.default_padx,
                                                ipady=5)

    def player_labels_checkbox(self):
        self.checkbox_output = IntVar()
        self.labels_input[0] = Label(self.window, text="Position Labels?", font=('', 12))
        self.labels_input[0].grid(row=3, column=0, padx=self.default_padx, pady=(5, 20),
                                  sticky='W')
        self.labels_input[1] = Checkbutton(self.window, variable=self.checkbox_output,
                                           command=lambda: self.checkbox_to_int(self.checkbox_output.get()))
        self.labels_input[1].grid(row=3, column=1, padx=self.default_padx, pady=(20, 1), sticky='W')

    def checkbox_to_int(self, num):
        if num:
            self.labels = True
        else:
            self.labels = False

    def create_player_inputs(self):

        self.player_num = int(self.player_number_change_entry[1].get())
        if self.player_num < 6: self.player_num = 6
        self.default_array = [x + 1 for x in range(self.player_num)]
        self.player_array = self.default_array.copy()
        self.player_input = [0 for x in range(self.player_num)]
        self.player_button = [0 for x in range(self.player_num + 2)]
        self.player_labels = [0 for x in range(self.player_num + 1)]
        self.position_array_labels = [0 for x in range(6)]

        # Add all the inputs and the add button
        for a in range(self.player_num):
            self.add_player_creation(a)
        # Selection button 0
        self.player_button[self.player_num + 1] = Button(self.window, text="Output", font=('', 12),
                                                         command=lambda: self.output())
        self.player_button[self.player_num + 1].grid(row=self.player_num + self.num_info_row, column=0, padx=5,
                                                     pady=(1, 10),
                                                     sticky='W',
                                                     ipadx=self.default_padx, ipady=5)

    def add_player_creation(self, num):
        # Selection button 0
        self.player_button[num] = Label(self.window, text="Player # " + str(num + 1), font=('', 12))
        self.player_button[num].grid(row=num + self.num_info_row, column=0, padx=5, pady=(1, 10), sticky='W',
                                     ipadx=self.default_padx,
                                     ipady=5)
        # Selection input 0
        self.player_input[num] = Entry(self.window, font=('', 10))
        self.player_input[num].grid(row=num + self.num_info_row, column=1, padx=self.default_padx, sticky='W')

    def output(self):
        # TODO Check array size

        # Makes the default array before checking view
        self.player_array = self.default_array.copy()

        for e in range(self.player_num):
            if self.player_input[e].get() != "":
                self.player_array[e] = self.player_input[e].get()

        # Into Label and directors
        self.add_output_button(0, 0)
        self.add_output_button(1, 0)
        self.add_output_button(2, 0)
        self.add_output_button(3, 1)
        self.add_output_button(4, 1)
        self.add_output_button(5, 1)
        if len(self.player_array) > 5:
            other_player_label = Label(self.window, text="Subs:", font=('', 12))
            other_player_label.grid(row=self.num_info_row, column=2, columnspan=1, padx=self.default_padx, pady=(5, 20),
                                    sticky='W')
        for b in range(len(self.player_array) - 6):
            self.player_labels[b + 6] = Label(self.window, text=self.player_array[b + 6], font=('', 12))
            self.player_labels[b + 6].grid(row=self.num_info_row, column=b + 3, columnspan=1, padx=self.default_padx,
                                           pady=(5, 20),
                                           sticky='W')
        rotate_button = Button(self.window, text="Rotate ", font=('', 12),
                               command=lambda: self.rotate())
        rotate_button.grid(row=self.num_info_row + 5, column=2, padx=5, pady=(1, 10), sticky='W',
                           ipadx=self.default_padx,
                           ipady=5)

    def add_output_button(self, num, row):

        # Forget last output
        if self.position_array_labels[num] != 0:
            self.position_array_labels[num].grid_forget()
        if self.player_labels[num] != 0:
            self.player_labels[num].grid_forget()

        # If there are labels it takes the row down by one
        if self.labels and row == 1:
            row = 2

        # Sets the column of the second row based on the number
        if num == 3:
            column = 4
        elif num == 4:
            column = 3
        elif num == 5:
            column = 2
        else:
            column = num + 2

        print("num", num, "row", row, "column", column)
        self.player_labels[num] = Label(self.window, text=self.player_array[num], font=('', 12))
        self.player_labels[num].grid(row=row + self.num_info_row + 1, column=column, columnspan=1,
                                     padx=self.default_padx, pady=(5, 20),
                                     sticky='W')
        if self.labels:
            self.position_array_labels[num] = Label(self.window, text=self.position_array[num], font=('', 12))
            self.position_array_labels[num].grid(row=row + 2 + self.num_info_row, column=column, columnspan=1,
                                                 padx=self.default_padx,
                                                 pady=(5, 20), sticky='W')

    def rotate(self):
        temp = self.player_array[len(self.player_array) - 1]
        self.player_array.pop(len(self.player_array) - 1)
        self.player_array.insert(0, temp)
        for c in range(len(self.player_array)):
            self.player_labels[c]["text"] = self.player_array[c]

    def run(self):
        # Says our method is ready to run
        self.window.mainloop()
