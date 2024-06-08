from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSlider, QGridLayout

def add_sliders(gridbox):
    slider = QSlider()
    slider.setOrientation(Qt.Horizontal)
    slider.setMinimum(1)
    slider.setMaximum(20)
    gridbox.addWidget(slider, 3, 0)
