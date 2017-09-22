import numpy as np
import matplotlib.pyplot as plt


class Cold_water():
    """Predict volume of cold water in litres per second."""
    def __init__(self, N, X, data_filename='data.tsv'):
        self.N = N
        self.X = X
        self.data_filename = data_filename
        self.y = [0, 0, 0]
        self.f = None
        self.x = [4, 6, 8]

    def error(self, f, x, y):
        # Error of prediction on given points.
        return np.sum((self.f(self.x) - self.y)**2)

    def get_data(self):
        # Get data from file.
        with open(self.data_filename) as f:
            for i, line in enumerate(f):
                arr = line.split()
                if int(arr[0]) == self.N:
                    arr = arr[1:]
                    for j in range(len(arr)):
                        self.y[j] = float(arr[j])
        print(self.y)

    def train(self):
        # Train model.
        fp = np.polyfit(self.x, self.y, 3)
        self.f = np.poly1d(fp)
        print('Error = {}'.format(self.error(self.f, self.x, self.y)))

    def predict(self):
        # Predict the result.
        self.get_data()
        self.train()

        print('For N = {} and X = {}, f(X) = {}'.format(
            self.N, self.X, self.f(self.X))
        )

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
