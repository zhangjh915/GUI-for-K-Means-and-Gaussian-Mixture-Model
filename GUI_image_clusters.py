# This creates an interactive GUI for users to play with images and parameters for K-means.
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
        self.images = ['data/Bird.png', 'data/Landscape.png', 'data/City.png']
        self.dataset_index = 0
        self.image = self.images[self.dataset_index]
        self.K = 1
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
        self.K = 1
        if self.method_name == 'kmeans':
            self.method_name = 'gmm'
        else:
            self.method_name = 'kmeans'
        self.draw()
        self.canvas.draw()

    def dataset_change(self):
        self.K = 1
        self.dataset_index = (self.dataset_index + 1) % 3
        self.image = self.images[self.dataset_index]
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

    def draw(self):
        if self.method_name == 'kmeans':
            self.ax1.cla()
            self.ax2.cla()
            image_values = image_to_matrix(self.image)
            new_image = k_means_segment(image_values, k=self.K)
            self.ax1.set_title('Segmented Image with %d K-means Clusters' % self.K)
            self.ax2.set_title('Original Image')
            self.ax1.imshow(new_image)
            self.ax2.imshow(image_values)
        else:
            self.ax1.cla()
            self.ax2.cla()
            original_image_matrix = image_to_matrix(self.image)  # Save original image
            image_matrix = original_image_matrix.reshape(-1, 3)  # collapse the dimension
            _, best_seg = best_segment(image_matrix, self.K, iters=10)
            new_image = best_seg.reshape(*original_image_matrix.shape)  # reshape collapsed matrix to original size
            # Show the image
            self.ax1.set_title('Segmented Image with %d GMM Clusters' % self.K)
            self.ax2.set_title('Original Image')
            self.ax1.imshow(new_image)
            self.ax2.imshow(original_image_matrix)


def main():
    root = Tk()
    app = App(root)
    root.title("K-means and GMM on image clustering")
    root.mainloop()


if __name__ == '__main__':
    main()
