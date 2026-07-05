import sys

#from PySide6.QtCore import QSize, Qt

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox, QRadioButton, QTextEdit, QSlider, QSpinBox, QProgressBar, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QWidget


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Main Widget and Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

       # Function to add widget with label
        def add_widget_with_label(layout, widget, label_text):
           hbox = QHBoxLayout()
           label = QLabel(label_text)
           hbox.addWidget(label)
           hbox.addWidget(widget)
           layout.addLayout(hbox)

        # QLabel
        self.label = QLabel('')
        add_widget_with_label(main_layout, self.label, 'Pipe Friction calculation')

        # QLineEdit
        self.line_edit = QLineEdit()
        add_widget_with_label(main_layout, self.line_edit, 'Volume flow (l/s):')

        self.line_edit = QLineEdit()
        add_widget_with_label(main_layout, self.line_edit, 'Pipe diameter (mm):')

        self.line_edit = QLineEdit()
        add_widget_with_label(main_layout, self.line_edit, 'Kinematic Viscosity (m2/s):')

        # QTextEdit
        self.text_edit = QTextEdit()
        add_widget_with_label(main_layout, self.text_edit, 'Result:')






app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()