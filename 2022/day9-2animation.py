        
# Native Libraries
import sys

# External Libraries
from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
import numpy as np


class RopeAnimator(QtWidgets.QWidget):
    def __init__(self, links_data, interval = 10, xlim=[-50,50], ylim=[-50,50]):
        # Initialize using built-in QWidget __init__ from inherited class
        super().__init__()
        self.links_data = links_data

        # Number of iterations before a the plot is updated
        self.iteration = -1

        # Set up PyQtGraph styling configurations        
        pg.setConfigOption('background', 0.95)
        pg.setConfigOptions(antialias=True)
        
        # Swinging pendulum animation
        # Create PyQTGraph plotting widget instance and configure layout
        self.rope_widget = pg.PlotWidget()
        self.rope_widget.setAspectLocked(lock=True, ratio=1)
        self.rope_widget.setXRange(*xlim)
        self.rope_widget.setYRange(*ylim)
        self.rope_widget.showGrid(x=True, y=True)

        self.rope_widget.setLabel("left", "y []")
        self.rope_widget.setLabel("bottom", "x []")

        # Add the plotting widget to the QtWidget layout
        widget_layout = QtWidgets.QHBoxLayout(self)
        widget_layout.addWidget(self.rope_widget)

        self.graphicsProxyWidget

        self.links_objects = self.rope_widget.plot([], [], symbol='o', symbolSize=5, symbolBrush=(0, 0, 0))
        
        self._timer = QtCore.QTimer(self, timeout=self.update_plot)
        self._timer.setInterval(interval)
        self._timer.start()

    def update_plot(self):
        if self.iteration < len(self.links_data):
            self.iteration += 1
            xdata = [pos[0] for pos in self.links_data[self.iteration,:, :]]
            ydata = [pos[1] for pos in self.links_data[self.iteration,:, :]]
            self.links_objects.setData(xdata, ydata)
        else:
            self._timer.stop()


with open("input_day9.txt") as datafile:
    head_movements = datafile.read().split("\n")

num_links = 100 + 1

movement_dict = {
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
}

rope = [np.array([0,0]) for x in range(num_links)]
rope_movement_history = [rope]

for instruction in head_movements:
    direction, repetitions = instruction.split(" ")
    head_move = movement_dict[direction]

    for i in range(int(repetitions)):
        rope[0] += head_move

        for link_num in range(1, num_links):
            diff = rope[link_num-1] - rope[link_num]

            if np.linalg.norm(diff) > 2:
                rope[link_num] += np.array([int(diff[0]/abs(diff[0])), int(diff[1]/abs(diff[1]))])
                
            elif np.linalg.norm(diff) == 2:
                rope[link_num] += np.array([int(diff[0]/2), int(diff[1]/2)])

        rope_movement_history.append(np.copy(rope))

rope_movement_history = np.array(rope_movement_history)


app = QtWidgets.QApplication(sys.argv)

RA = RopeAnimator(rope_movement_history)
RA.show()

sys.exit(app.exec_())