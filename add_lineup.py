import math
from tkinter import *
from tkinter import filedialog


class add_lineup:
    def __init__(self):
        # The Creation of this class

        # Final values of the program
        self.default_padx = 10
        self.position_array = ["Server", "Hitter", "Setter", "Hitter", "Hitter", "Hitter"]

        # The window
        self.window = Tk()

        # The checkbox for if you want labels
        self.labels = False
        self.two_subs = False
        self.checkbox_output = None
        self.checkbox_output_subs = None
        self.labels_input = [None for x in range(3)]
        self.both_subs = [None for x in range(3)]
        self.import_file = [None for x in range(2)]

        # Player number
        self.player_num = -1
        self.player_number_change_entry = [None for x in range(3)]
        self.num_info_row = 5
        self.two_column = 0

        # The arrays containing the players
        self.first_input_output = False
        self.default_array = None
        self.player_array = None
        self.player_input = None
        self.player_button = None
        self.player_labels = None
        self.position_array_labels = None

        # Output values
        self.net_label = None
        self.other_player_label_two = None
        self.other_player_label = None
        self.rotate_button = None
        self.output_value = None
        self.first_output = True

        # Create the screen
        self.create_screen()

        # Creates the feild for player numbers
        self.get_player_number()

        # Creates the labels input
        self.player_labels_checkbox()
        self.both_sides_subs()

        # TODO Remove- Just for testing
        # self.create_player_inputs()
        # self.output()

        # Runs the program
        self.run()

    def create_screen(self):
        # Sets the resolution of the window
        self.window.geometry('1200x700')

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
                                                ipadx=self.default_padx, ipady=5)

    def player_labels_checkbox(self):
        self.checkbox_output = IntVar()
        self.labels_input[0] = Label(self.window, text="Position Labels?", font=('', 12))
        self.labels_input[0].grid(row=3, column=0, padx=self.default_padx, pady=(10, 10),
                                  sticky='W')
        self.labels_input[1] = Checkbutton(self.window, variable=self.checkbox_output,
                                           command=lambda: self.checkbox_to_int(self.checkbox_output.get(),
                                                                                "labels"))
        self.labels_input[1].grid(row=3, column=1, padx=self.default_padx, pady=(10, 10), sticky='W')
        self.labels_input[2] = Label(self.window, text="* Label the positions \n of the players", font=('', 10))
        self.labels_input[2].grid(row=3, column=2, padx=self.default_padx, pady=(10, 10), sticky='W', columnspan=4)

    def both_sides_subs(self):
        self.checkbox_output_subs = IntVar()
        self.both_subs[0] = Label(self.window, text="Sub in both sides?", font=('', 12))
        self.both_subs[0].grid(row=4, column=0, padx=self.default_padx, pady=(10, 10),
                                  sticky='W')
        self.both_subs[1] = Checkbutton(self.window, variable=self.checkbox_output_subs,
                                           command=lambda: self.checkbox_to_int(self.checkbox_output_subs.get(),
                                                                                "two_subs"))
        self.both_subs[1].grid(row=4, column=1, padx=self.default_padx, pady=(10, 10), sticky='W')
        self.both_subs[2] = Label(self.window, text="* The players sub in \n from both sides", font=('', 10))
        self.both_subs[2].grid(row=4, column=2, padx=self.default_padx, pady=(10, 10), sticky='W', columnspan=4)

    def checkbox_to_int(self, num, what_to_change):
        if num:
            result = True
        else:
            result = False

        if what_to_change == "labels":
            self.labels = result
        elif what_to_change == "two_subs":
            self.two_subs = result

    def create_player_inputs(self):

        self.forget_output_buttons()
        # If it is not the first time displaying all the inputs get rid of all the previos stuff
        if self.first_input_output:
            # Removes the player_input labels
            for c in range(len(self.player_button)):
                self.player_button[c].grid_forget()
            # Removes the player inputs themselves
            for d in range(len(self.player_input)):
                self.player_input[d].grid_forget()

        # Try setting to integer value inputted if not just set it to 6
        try:
            self.player_num = int(self.player_number_change_entry[1].get())
        except ValueError:
            self.player_num = 6
            # TODO print out error if this occurs

        if self.player_num > 8:
            self.two_column = 2
        else:
            self.two_column = 0

        if self.player_num < 6: self.player_num = 6
        # The default array of values [1-Playernum]
        self.default_array = [x + 1 for x in range(self.player_num)]
        # The Array of player names
        self.player_array = self.default_array.copy()
        # The input feilds for each of the player names
        self.player_input = [0 for x in range(self.player_num)]
        # The labels for each of the name inputs
        self.player_button = [0 for x in range(self.player_num + 1)]

        # Output Arrays
        # The output labels for each of the player
        self.player_labels = [0 for x in range(self.player_num)]
        # The position labels for each of the players
        self.position_array_labels = [0 for x in range(6)]

        # Reset output
        self.first_output = True

        # Add all the inputs and the add button
        for a in range(self.player_num):
            self.add_player_creation(a)
        # Selection button 0
        self.player_button[self.player_num] = Button(self.window, text="Output", font=('', 12),
                                                     command=lambda: self.output())
        self.player_button[self.player_num].grid(row=self.player_num + self.num_info_row, column=0, padx=5,
                                                 pady=(1, 10),
                                                 sticky='W',
                                                 ipadx=self.default_padx, ipady=5)
        self.first_input_output = True

    def add_player_creation(self, num):
        if self.two_column == 2 and num > 7:
            column = 2
            row = num - 8
        else:
            column = 0
            row = num
        # Selection button 0
        self.player_button[num] = Label(self.window, text="Player # " + str(num + 1), font=('', 12), fg="Purple")
        self.player_button[num].grid(row=row + self.num_info_row, column=column, padx=5, pady=(1, 10), sticky='W',
                                     ipadx=self.default_padx,
                                     ipady=5)
        # Selection input 0
        self.player_input[num] = Entry(self.window, font=('', 10))
        self.player_input[num].grid(row=row + self.num_info_row, column=column + 1, padx=self.default_padx, sticky='W')

    def output(self):
        # TODO Check array size

        # Makes the default array before checking view
        if not self.first_output:
            self.player_array = self.default_array.copy()
            self.forget_output_buttons()

        # Get the array of player inputs
        for e in range(self.player_num):
            if self.player_input[e].get() != "":
                self.player_array[e] = self.player_input[e].get()

        # If there are more than 6 people
        if len(self.player_array) > 6:

            if self.two_subs:
                above = math.floor((self.player_num - 6) / 2) + 6
                # Into Label and directors
                self.add_output_button(0, 0)
                self.add_output_button(1, 0)
                self.add_output_button(2, 0)
                self.add_output_button(above - 3, 1, above)
                self.add_output_button(above - 2, 1, above)
                self.add_output_button(above - 1, 1, above)
            else:
                above = 6
                # Into Label and directors
                self.add_output_button(0, 0)
                self.add_output_button(1, 0)
                self.add_output_button(2, 0)
                self.add_output_button(3, 1)
                self.add_output_button(4, 1)
                self.add_output_button(5, 1)

            self.other_player_label = Label(self.window, text="Subs:", font=('', 12), fg="Red")
            self.other_player_label.grid(row=self.num_info_row, column=2 + self.two_column, columnspan=1,
                                         padx=self.default_padx,
                                         pady=(5, 20),
                                         sticky='W')
            if self.two_subs:
                self.other_player_label_two = Label(self.window, text="Subs:", font=('', 12), fg="Red")
                self.other_player_label_two.grid(row=self.num_info_row, column=6 + self.two_column, columnspan=1,
                                                 padx=self.default_padx,
                                                 pady=(5, 20),
                                                 sticky='W')
            size = above - 6
            for b in range(len(self.player_array) - above):
                self.player_labels[b + above] = Label(self.window, text=self.player_array[b + above], font=('', 12),
                                                      fg="Red")
                self.player_labels[b + above].grid(row=6 + b, column=2 + self.two_column,
                                                   columnspan=1,
                                                   padx=self.default_padx,
                                                   pady=(5, 20),
                                                   sticky='W')
            for b in range(size):
                self.player_labels[b + 3] = Label(self.window, text=self.player_array[b + 3], font=('', 12), fg="Red")
                self.player_labels[b + 3].grid(row=size - b + self.num_info_row, column=6 + self.two_column,
                                               columnspan=1,
                                               padx=self.default_padx,
                                               pady=(5, 20),
                                               sticky='W')
        else:
            # Into Label and directors
            self.add_output_button(0, 0)
            self.add_output_button(1, 0)
            self.add_output_button(2, 0)
            self.add_output_button(3, 1)
            self.add_output_button(4, 1)
            self.add_output_button(5, 1)
        if self.labels:
            bottom_labels_row = self.num_info_row + 4
        else:
            bottom_labels_row = self.num_info_row + 2

        # Label for the net
        self.net_label = Label(self.window, text="          NET         ", font=('', 15), fg="blue4", bg="gray80")
        self.net_label.grid(row=bottom_labels_row + 1, column=3 + self.two_column, columnspan=3, padx=self.default_padx,
                            pady=(5, 20),
                            sticky='s')
        # Make the rotate button
        self.rotate_button = Button(self.window, text="Rotate ", font=('', 12),
                                    command=lambda: self.rotate())
        self.rotate_button.grid(row=bottom_labels_row + 2, column=3 + self.two_column, padx=10, pady=(10, 10),
                                sticky='W',
                                ipadx=self.default_padx, ipady=5, columnspan=3)
        # As it has now output the first output is now true
        self.first_output = False

    def forget_output_buttons(self):
        if not self.first_output:
            if not self.other_player_label is None:
                self.other_player_label.grid_forget()
            if not self.other_player_label_two is None:
                self.other_player_label_two.grid_forget()
            if not self.net_label is None:
                self.net_label.grid_forget()
            self.rotate_button.grid_forget()
            # Forget all the label objects
            for f in range(len(self.player_labels)):
                self.player_labels[f].grid_forget()
            # Forget all the position labels if they exist
            if self.position_array_labels[0] != 0:
                for g in range(len(self.position_array_labels)):
                    self.position_array_labels[g].grid_forget()

    def add_output_button(self, num, row, above_num=0):

        # If there are labels it takes the row down by one
        if self.labels and row == 1:
            row = 2

        if self.two_subs:
            # Sets the column of the second row based on the number
            if num == above_num - 3:
                column = 5
                label = 3
            elif num == above_num - 2:
                column = 4
                label = 4
            elif num == above_num - 1:
                column = 3
                label = 5
            else:
                column = num + 3
                label = num
        else:
            # Sets the column of the second row based on the number
            label = num
            if num == 3:
                column = 5
            elif num == 4:
                column = 4
            elif num == 5:
                column = 3
            else:
                column = num + 3

        self.player_labels[num] = Label(self.window, text=self.player_array[num], font=('', 14))
        self.player_labels[num].grid(row=row + self.num_info_row + 1, column=column + self.two_column,
                                     padx=self.default_padx, pady=(5, 20), sticky='s')
        if self.labels:
            self.position_array_labels[label] = Label(self.window, text=self.position_array[label], font=('', 12))
            self.position_array_labels[label].grid(row=row + 2 + self.num_info_row, column=column + self.two_column,
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


# Line that actually runs the class
lineup = add_lineup()
