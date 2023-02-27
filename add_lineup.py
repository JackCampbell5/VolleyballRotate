from tkinter import *


class add_lineup:
    def __init__(self, player_num, position_array):
        # The Creation of this class

        # Create the Main window for all the info
        self.output_value = None
        self.window = Tk()
        self.player_num = player_num
        self.player_array = [0 for x in range(self.player_num)]
        self.player_input = [0 for x in range(20)]
        self.player_button = [0 for x in range(20)]
        self.default_padx = 10
        self.player_labels = [0 for x in range(self.player_num + 1)]
        self.position_array = position_array
        self.position_array_labels = [0 for x in range(6)]

        self.create_screen()
        self.create_player_inputs()
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

    def create_player_inputs(self):
        for a in range(self.player_num):
            self.add_player_creation(a)
        # Selection button 0
        self.player_button[self.player_num + 1] = Button(self.window, text="Output", font=('', 12),
                                                         command=lambda: self.output())
        self.player_button[self.player_num + 1].grid(row=self.player_num + 3, column=0, padx=5, pady=(1, 10),
                                                     sticky='W',
                                                     ipadx=self.default_padx, ipady=5)

    def add_player_creation(self, num):
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

    def rotate(self):
        temp = self.player_array[len(self.player_array)-1]
        self.player_array.pop(len(self.player_array)-1)
        self.player_array.insert(0,temp)
        for c in range(len(self.player_array)):
            self.player_labels[c]["text"] = self.player_array[c]


    def output(self):
        # TODO Check array size
        # Into Label and directors
        self.add_output_button(0, 4)
        self.add_output_button(1, 4)
        self.add_output_button(2, 4)
        self.add_output_button(3, 6)
        self.add_output_button(4, 6)
        self.add_output_button(5, 6)
        print(len(self.player_array))
        if len(self.player_array) > 5:
            other_player_label = Label(self.window, text="Subs:", font=('', 12))
            other_player_label.grid(row=2, column=2, columnspan=1, padx=self.default_padx, pady=(5, 20),
                                       sticky='W')
            print("hi")
        for b in range(len(self.player_array) - 6):
            self.player_labels[b + 6] = Label(self.window, text=self.player_array[b + 6], font=('', 12))
            self.player_labels[b + 6].grid(row=2, column=b + 3, columnspan=1, padx=self.default_padx, pady=(5, 20),
                                           sticky='W')
        rotate_button = Button(self.window, text="Rotate ", font=('', 12),
                               command=lambda: self.rotate())
        rotate_button.grid(row=9, column=2, padx=5, pady=(1, 10), sticky='W', ipadx=self.default_padx,
                           ipady=5)

    def add_output_button(self, num, row):
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
        self.player_labels[num].grid(row=row, column=column, columnspan=1, padx=self.default_padx, pady=(5, 20),
                                     sticky='W')
        self.position_array_labels[num] = Label(self.window, text=self.position_array[num], font=('', 12))
        self.position_array_labels[num].grid(row=row + 1, column=column, columnspan=1, padx=self.default_padx,
                                             pady=(5, 20),
                                             sticky='W')

    def run(self):
        # Says our method is ready to run
        self.window.mainloop()
