import numpy as np
import matplotlib
from kivy.uix.gridlayout import GridLayout
matplotlib.use("module://kivy.garden.matplotlib.backend_kivy")
from kivy.garden.matplotlib import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import matplotlib.figure
plt.style.use('dark_background')


class ImageSonogram(GridLayout):

    def __init__(self, **kwargs):
        # create the fig, axes, and canvas
        self.fig1 = matplotlib.figure.Figure()
        self.plot_sonogram_canvas = FigureCanvasKivyAgg(self.fig1)

        # make plot take up the entire space
        self.ax1 = self.fig1.add_axes([0., 0., 1., 1.])
        self.ax1.set_axis_off()
        super(ImageSonogram, self).__init__(**kwargs)

    def image_sonogram_initial(self, rows, cols):
        # clear axes and reformat to make plot take up the entire space
        self.ax1.clear()
        self.ax1.set_axis_off()

        # plot data
        data = np.zeros((rows, cols))
        self.plot_sonogram = self.ax1.imshow(np.log(data + 3), cmap='hot',
                                             extent=[0, cols, 0, rows],
                                             aspect='auto')

        # create widget
        self.clear_widgets()
        self.add_widget(self.plot_sonogram_canvas)

    def image_sonogram(self, data):
        self.plot_sonogram.set_data(np.log(data + 3))
        self.plot_sonogram.autoscale()
        self.plot_sonogram_canvas.draw_idle()