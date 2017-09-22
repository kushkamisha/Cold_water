from tkinter import Tk, Button, Entry, Label, messagebox, N, S, E, W
from tkinter.ttk import Separator, Style
from cold_water import Cold_water


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
        app_height = 175

        master.title('Витрата води')
        x = screen_width / 2 - app_width / 2
        y = screen_height / 2 - app_height / 2

        master.geometry('%dx%d+%d+%d' % (app_width, app_height, x, y))
        master.minsize(app_width, app_height)
        master.maxsize(app_width, app_height)

        self.label0 = Label(
            master,
            text='Визначення секундних витрат холодної '\
                'води\nв залежності від кількості приладів'
        )
        self.label0.grid(row=0, column=0, columnspan=3)

        sep = Separator(master, orient="horizontal")
        sep.grid(row=1, column=0, columnspan=3, padx=8, pady=10, sticky="EW")

        sty = Style(master)
        sty.configure("TSeparator", background="black")

        self.label1 = Label(master, text='Кількість приладів, шт')
        self.label1.grid(row=2, column=0, columnspan=2, sticky=W, padx=5)
        self.entry0 = Entry(master, width=4)
        self.entry0.grid(row=2, column=2, padx=8)

        self.label2 = Label(master, text='Середньодобова витрата води, л/добу')
        self.label2.grid(row=3, column=0, columnspan=2, sticky=W, padx=5)
        self.entry1 = Entry(master, width=4)
        self.entry1.grid(row=3, column=2, padx=8)

        self.label3 = Label(master, text='Секундна витрата води, л/сек')
        self.label3.grid(row=4, column=0, columnspan=2, sticky=W, padx=5)

        self.label4 = Label(master, text='...')
        self.label4.grid(row=4, column=2, pady=10)

        self.result = Button(
            master, text='Отримати результат', command=self.check_input
        )
        self.result.grid(row=5, column=0, columnspan=3)

        self.master.bind("<Return>", self.check_input)
        self.master.bind("<Escape>", exit)

    def get_result(self):
        """Calculate the result."""
        my_water = Cold_water(self.N, self.X)
        my_result = my_water.predict()
        my_water.visualize_function()
        self.label4['text'] = str(round(my_result, 2))

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


def main():
    root = Tk()
    my_gui = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
