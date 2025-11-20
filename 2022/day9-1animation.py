        
# Native Libraries
import sys

# External Libraries
from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
import numpy as np


class RopeAnimator(QtWidgets.QWidget):
    def __init__(self, head_data, tail_data, interval = 10, xlim=[-100,100], ylim=[-100,100]):
        # Initialize using built-in QWidget __init__ from inherited class
        super().__init__()
        self.head_data = head_data
        self.tail_data = tail_data

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

        self.rope_widget.setLabel("left", "y []")
        self.rope_widget.setLabel("bottom", "x []")

        # Add the plotting widget to the QtWidget layout
        widget_layout = QtWidgets.QHBoxLayout(self)
        widget_layout.addWidget(self.rope_widget)

        self.rope = self.rope_widget.plot()
        self.rope.setPen(pg.mkPen(color=(0, 0, 0), width=2))

        self.head = self.rope_widget.plot([], [], symbol='o', symbolSize=5, symbolBrush=(0, 0, 0))
        self.head.setData([0], [0])

        self.tail = self.rope_widget.plot([], [], symbol='o', symbolSize=5, symbolBrush=(0, 0, 0))
        self.tail.setData([0], [0])
            
        self._timer = QtCore.QTimer(self, timeout=self.update_plot)
        self._timer.setInterval(interval)
        self._timer.start()

    def update_plot(self):
        self.iteration += 1

        [xhead, yhead] = self.head_data[self.iteration]
        self.head.setData([xhead], [yhead])

        [xtail, ytail] = self.tail_data[self.iteration]
        self.tail.setData([xtail], [ytail])

        self.rope.setData([xhead, xtail], [yhead, ytail])

with open("input_day9.txt") as datafile:
    head_movements = datafile.read().split("\n")

movement_dict = {
    "R": np.array([1, 0]),
    "L": np.array([-1, 0]),
    "U": np.array([0, 1]),
    "D": np.array([0, -1]),
}

head = np.array([0,0])
head_movement_history = [head]

tail = np.array([0,0])
tail_movement_history = [tail]

for instruction in head_movements:
    direction, repetitions = instruction.split(" ")
    head_move = movement_dict[direction]

    for i in range(int(repetitions)):
        head += head_move
        head_movement_history.append(np.copy(head))

        diff = head - tail
        if np.linalg.norm(diff) > 2:
            tail += np.array([int(diff[0]/abs(diff[0])), int(diff[1]/abs(diff[1]))])
            
        elif np.linalg.norm(diff) == 2:
            tail += head_move

        tail_movement_history.append(np.copy(tail))


# xlim = [
#         np.min([
#             np.array(tail_movement_history)[:,0], 
#             np.array(head_movement_history)[:,0], 
#         ]), 
#         np.max([
#             np.array(tail_movement_history)[:,0], 
#             np.array(head_movement_history)[:,0], 
#         ])
# ]

# ylim = [
#         np.min([
#             np.array(tail_movement_history)[:,1], 
#             np.array(head_movement_history)[:,1], 
#         ]), 
#         np.max([
#             np.array(tail_movement_history)[:,1], 
#             np.array(head_movement_history)[:,1], 
#         ])
# ]

# print(xlim, ylim)


app = QtWidgets.QApplication(sys.argv)

RA = RopeAnimator(list(head_movement_history), list(tail_movement_history))
RA.show()

sys.exit(app.exec_())