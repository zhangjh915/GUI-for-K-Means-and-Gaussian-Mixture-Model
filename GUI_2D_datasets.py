# This creates an interactive GUI for users to play with data and parameters for K-means.
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from kmeans import *
from GMM import *


class App:
    def __init__(self, master):
        # Create container
        frame = Frame(master)
        # Create buttons
        self.method = Button(frame, text="K-means/GMM", command=self.method_change)
        self.method.pack(side="left")
        self.dataset = Button(frame, text="Change Dataset", command=self.dataset_change)
        self.dataset.pack(side="left")
        self.k_value = Button(frame, text="Increase K", command=self.k_increase)
        self.k_value.pack(side="left")
        self.k_value = Button(frame, text="Decrease K", command=self.k_decrease)
        self.k_value.pack(side="left")
        self.k_value = Button(frame, text="Increase Step", command=self.n_increase)
        self.k_value.pack(side="left")
        self.n_value = Button(frame, text="Decrease Step", command=self.n_decrease)
        self.n_value.pack(side="left")
        self.dataset_index = 0
        self.K = 2
        self.n = 1
        self.method_name = 'kmeans'

        self.fig = Figure(figsize=(15, 6))
        self.ax1 = self.fig.add_subplot(121)
        self.ax2 = self.fig.add_subplot(122)
        self.draw()

        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        frame.pack()

    def method_change(self):
        self.n = 1
        if self.method_name == 'kmeans':
            self.method_name = 'gmm'
        else:
            self.method_name = 'kmeans'
        self.draw()
        self.canvas.draw()

    def dataset_change(self):
        self.dataset_index = (self.dataset_index + 1) % 5
        self.n = 1
        self.draw()
        self.canvas.draw()

    def k_increase(self):
        self.K += 1
        self.draw()
        self.canvas.draw()

    def k_decrease(self):
        if self.K >= 2:
            self.K -= 1
        self.draw()
        self.canvas.draw()

    def n_increase(self):
        if self.method_name == 'kmeans':
            self.n += 1
        else:
            self.n += 10
        self.draw()
        self.canvas.draw()

    def n_decrease(self):
        if self.method_name == 'kmeans':
            if self.n >= 2:
                self.n -= 1
        else:
            if self.n >= 11:
                self.n -= 10
        self.draw()
        self.canvas.draw()

    def draw(self):
        if self.method_name == 'kmeans':
            self.ax1.cla()
            self.ax2.cla()
            X, y, clusters_history = K_means_2D_dataset(self.dataset_index, self.K, self.n)
            clusters = clusters_history[self.n]
            self.ax1.set_title('K-means clsuters - step %d' % self.n)
            for k in range(self.K):
                self.ax1.plot(X[clusters == k, 0], X[clusters == k, 1], '.')

            self.ax2.set_title('Ground truth clusters')
            for i in np.unique(y):
                self.ax2.plot(X[y == i, 0], X[y == i, 1], '.')
        else:
            self.ax1.cla()
            self.ax2.cla()
            X, y, clusters_history = GMM_2D_dataset(self.dataset_index, self.K)
            clusters = clusters_history[self.n]
            self.ax1.set_title('GMM clsuters - step %d' % self.n)
            for k in range(self.K):
                self.ax1.plot(X[clusters == k, 0], X[clusters == k, 1], '.')  #
                # Try to plot the centers of the clusters
                # You can access them by calling means_history[i]
                # How could you plot the area that belong to that cluster?

            # Just to get a flavour of how the data looks like
                self.ax2.set_title('Ground truth clusters')
            for i in np.unique(y):
                self.ax2.plot(X[y == i, 0], X[y == i, 1], '.')


def main():
    root = Tk()
    app = App(root)
    root.title("K-means and GMM on 2D datasets")
    root.mainloop()


if __name__ == '__main__':
    main()
