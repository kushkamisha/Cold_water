from tkinter import Tk, Button, Entry, Label, messagebox, N, S, E, W, StringVar, filedialog
from tkinter import ttk
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Cold_water():
    """Predict volume of cold water in litres per second."""
    def __init__(self, N, X, data_filename='data.tsv'):
        self.N = N
        self.X = X
        self.data_filename = data_filename
        self.f = None
        self.df = None
        self.x = [4, 6, 8]
        self.y = []

    def get_data(self):
        """Get data from file."""
        self.df = pd.read_csv('data.tsv', sep='\t', header=None)
        # Try to find current value of N in the file.
        lst = [i for i,x in enumerate(np.array(self.df[0])) if x == self.N]
        if (lst == []):
            # Can't find N in the file.
            self.get_y()
        else:
            # N is in the file.
            self.y = [self.df[i][lst[0]] for i in range(1, self.df.shape[1])]

    def get_y(self):
        """
        Find row with N in the table or create
        this row if can't find.
        """
        for num in range(1, self.df.shape[1]):
            x = self.df[0]
            yy = self.df[num]
            i = 1
            while (i <= (len(x) - 3)):
                curr_x = x[i:i+3]
                curr_y = yy[i:i+3]

                fp = np.polyfit(curr_x, curr_y, 2)
                f = np.poly1d(fp)
        
                if (self.N >= min(x[i:i+3]) and self.N <= max(x[i:i+3])):
                    self.y.append(f(self.N))
        
                i += 2

    def train(self):
        # Train model.
        fp = np.polyfit(self.x, self.y, 3)
        self.f = np.poly1d(fp)

    def predict(self):
        # Predict the result.
        self.get_data()
        self.train()

        return self.f(self.X)

    def visualize_function(self):
        # Visualize the result.
        fx = np.linspace(0, self.x[-1], 1000)

        plt.title('N = {}'.format(self.N))
        plt.xlabel('Liters per hour')
        plt.ylabel('Liters per second')

        plt.plot(fx, self.f(fx), linewidth=2, c='b', zorder=1)
        plt.scatter(self.X, self.f(self.X), s=180, marker='*', c='r', zorder=2)
        plt.scatter(self.x, self.y, s=30, c='r', zorder=2)

        plt.grid(True, linestyle='-', color='0.75')
        plt.show()


class GUI():
    """GUI for cold_water application."""
    def __init__(self, master):
        self.master = master
        self.master.focus_set()
        self.N = 1
        self.X = 4
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        app_width = 400 # 283
        app_height = 230

        master.title('Витрата води')
        x = screen_width / 2 - app_width / 2
        y = screen_height / 2 - app_height / 2

        master.geometry('%dx%d+%d+%d' % (app_width, app_height, x, y))
        master.minsize(app_width, app_height)
        master.maxsize(app_width, app_height)

        self.label0 = Label(
            master,
            text='Визначення максимальних секундних витрат \n'\
                'води в залежності від кількості приладів'
        )
        self.label0.grid(row=0, column=0, columnspan=3)

        # Horisontal line.
        sep = ttk.Separator(master, orient="horizontal")
        sep.grid(row=1, column=0, columnspan=3, padx=8, pady=10, sticky="EW")
        sty = ttk.Style(master)
        sty.configure("TSeparator", background="black")

        self.label1 = Label(master, text='Кількість приладів, шт')
        self.label1.grid(row=2, column=0, columnspan=2, sticky=W, padx=5)
        self.entry0 = Entry(master, width=6)
        self.entry0.grid(row=2, column=2, padx=8)

        self.label2 = Label(master, text='Середньодобова витрата води одним споживачем, л/добу')
        self.label2.grid(row=3, column=0, columnspan=2, sticky=W, padx=5)

        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.callback(sv))
        self.entry1 = Entry(master, width=6, textvariable=sv)
        self.entry1.grid(row=3, column=2, padx=8)

        self.label3 = Label(master, text='Секундна витрата води, л/с')
        self.label3.grid(row=4, column=0, columnspan=2, sticky=W, padx=5)

        self.label4 = Label(master, text='...')
        self.label4.grid(row=4, column=2, pady=10)

        self.result = Button(
            master, text='Отримати результат', command=self.check_input
        )
        self.result.grid(row=5, column=0, columnspan=3)

        # Horisontal line.
        sep = ttk.Separator(master, orient="horizontal")
        sep.grid(row=6, column=0, columnspan=3, padx=8, pady=10, sticky="EW")
        sty = ttk.Style(master)
        sty.configure("TSeparator", background="black")

        # Copyright.
        Label(master,
              text = "Copyright © 2017, Kushka Misha,"
              ).grid(row = 7, column = 0, columnspan = 3, sticky = S)
        Label(master,
              text = "All Rights Reserved"
              ).grid(row = 8, column = 0, columnspan =3, sticky = S)

        self.master.bind("<Return>", self.check_input)
        self.master.bind("<Escape>", self.quit_app)
        
    def quit_app(self, event):
        plt.close()
        global root
        root.destroy()

    def get_result(self):
        """Calculate the result."""
        my_water = Cold_water(self.N, self.X)
        my_result = my_water.predict()
        self.label4['text'] = str(round(my_result, 2))
        my_water.visualize_function()

    def callback(self, sv):
        c = sv.get()[:6]
        sv.set(c)

    def check_input(self, event=None):
        """Check correctness of the user input."""
        self.N = self.entry0.get()
        self.X = self.entry1.get()
        X_is_ok = True
        N_is_ok = True

        if (len(self.N) == 0):
            messagebox.showinfo('Помилка', 'Спершу введіть кількість приладів.')
            N_is_ok = False
        elif (len(self.X) == 0):
            messagebox.showinfo(
                'Помилка', 'Спершу введіть середньодобову витрату.'
            )
            X_is_ok = False
        elif (not self.N.isdigit()):
            messagebox.showinfo(
                'Помилка', 'Кількість приладів мусить бути натуральним числом.'
            )
            N_is_ok = False
        elif (int(self.N) < 1 or int(self.N) > 1500):
            messagebox.showinfo(
                'Помилка',
                'Кількість приладів мусить належати проміжку [1, 1500].'
            )
            N_is_ok = False
        else:
            try:
                self.X = float(self.X)
            except ValueError:
                messagebox.showinfo(
                    'Помилка',
                    'Середньодобова витрата мусить бути цілим чи дійсним числом.'
                )
                X_is_ok = False

        if (X_is_ok):
            if (self.X > 170):
                messagebox.showinfo(
                    'Помилка',
                    'Середньодобова витрата мусить бути не більше за 170.'
                )
                X_is_ok = False

        if (N_is_ok and X_is_ok):
            self.N = int(self.N)
            self.X = self.X / 24
            self.get_result()


root = Tk()
my_gui = GUI(root)
root.mainloop()
