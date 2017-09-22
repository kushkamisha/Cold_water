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
            print('N is in the file.')
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
