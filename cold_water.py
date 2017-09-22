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

    def predict(self):
        # Predict the result.
        self.get_data()
        self.train()

        return self.f(self.X)
