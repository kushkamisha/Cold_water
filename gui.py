from tkinter import Tk, Button, Entry, Label, messagebox


class GUI():
    """GUI for cold_water application."""
    def __init__(self, master):
        self.master = master
        self.master.focus_set()
        self.N = 1
        self.X = 4
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
            master, text='Get result', command=self.check_input
        )
        self.result.grid(row=4, column=2)

        self.close_button = Button(master, text='Close', command=exit)
        self.close_button.grid(row=5, column=2)

        self.master.bind("<Return>", self.check_input)
        self.master.bind("<Escape>", exit)

    def get_result(self):
        pass

    def check_input(self, event=None):
        """Check correctness of the user input."""
        self.N = self.entry1.get()
        self.X = self.entry2.get()
        X_is_ok = True
        N_is_ok = True

        if (len(self.N) == 0):
            messagebox.showinfo('Error', 'Enter N first.')
            N_is_ok = False
        elif (len(self.X) == 0):
            messagebox.showinfo('Error', 'Enter X first.')
            X_is_ok = False
        elif (not self.N.isdigit()):
            messagebox.showinfo('Error', 'N must be int type.')
            N_is_ok = False
        elif (int(self.N) < 1 or int(self.N) > 170):
            messagebox.showinfo('Error', 'N must be in a range [1, 170].')
            N_is_ok = False
        else:
            try:
                self.X = float(self.X)
            except ValueError:
                messagebox.showinfo(
                    'Error', 'X must be float or integer number!'
                )
                X_is_ok = False

        if (N_is_ok and X_is_ok):
            self.N = int(self.N)
            self.get_result()


def main():
    root = Tk()
    my_gui = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
