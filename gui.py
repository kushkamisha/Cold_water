from tkinter import Tk, Label, Button, Message, Entry, LEFT, RIGHT


class GUI():
    """GUI for cold_water application."""
    def __init__(self, master):
        self.master = master
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        app_width = 270
        app_height = 150

        master.title('Cold water program GUI')
        x = screen_width / 2 - app_width / 2
        y = screen_height / 2 - app_height / 2
        master.geometry('%dx%d+%d+%d' % (app_width, app_height, x, y))

        self.label1 = Label(master, text='Enter N here text text text')
        self.label1.grid(row=1, column=1, columnspan=2)
        self.entry1 = Entry(master, width=4)
        self.entry1.grid(row=1, column=3)

        self.label1 = Label(master, text='Enter X here more text')
        self.label1.grid(row=2, column=1, columnspan=2)
        self.entry2 = Entry(master, width=4)
        self.entry2.grid(row=2, column=3)

        self.label3 = Label(master, text='Result will be here...')
        self.label3.grid(row=3, column=2)

        self.result = Button(
            master, text='Get result', command=self.get_result
        )
        self.result.grid(row=4, column=2)

        self.close_button = Button(master, text='Close', command=master.quit)
        self.close_button.grid(row=5, column=2)

    def get_result(self):
        """Calculate the result."""
        N = self.entry1.get()
        X = self.entry2.get()

        # if (self.entry1 == ''):
        #     print('Enter N first.')
        # if (self.entry2 == ''):
        #     print('Enter X first.')

        if (not N.isdigit()):
            print('N must be int type.')

        try:
            X = float(X)
        except ValueError:
            print('X must be float or integer number!')


def main():
    root = Tk()
    my_gui = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
