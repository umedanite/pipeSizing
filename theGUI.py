import sys

#from PySide6.QtCore import QSize, Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QCheckBox,
    QRadioButton,
    QTextEdit,
    QSlider,
    QSpinBox,
    QProgressBar,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QWidget)

from Calculation import haaland

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pipe Friction Calculation")
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
        self.line_edit_V = QLineEdit()
        add_widget_with_label(main_layout, self.line_edit_V, 'Volume flow (l/s):')

        self.line_edit_d = QLineEdit()
        add_widget_with_label(main_layout, self.line_edit_d, 'Pipe diameter (mm):')

        self.line_edit_v = QLineEdit()
        add_widget_with_label(main_layout, self.line_edit_v, 'Kinematic Viscosity (m2/s):')

        self.line_edit_k = QLineEdit()
        add_widget_with_label(main_layout, self.line_edit_k, 'Pipe roughless (mm):')

        # QPushButton
        self.button = QPushButton('Calculate')
        self.button.clicked.connect(self.on_button_clicked)
        add_widget_with_label(main_layout, self.button, 'Click to Calculate')

        # QTextEdit
        self.text_edit = QTextEdit()
        add_widget_with_label(main_layout, self.text_edit, 'Result:')

    def on_button_clicked(self):
        try:
            V = float(self.line_edit_V.text())
            d = float(self.line_edit_d.text())
            v = float(self.line_edit_v.text())
            k = float(self.line_edit_k.text())

            u, re, f, pd = haaland(V,d,v,k)

            result_text = (
                f"Flow velocity u: {u} m/s\n"
                f"Reynolds number Re: {re:.0f}\n"
                f"Friction factor f: {f}\n"
                f"Pressure drop per meter: {pd} m/m\n"
                f"Pressure drop per meter: {1000 * 9.81 * pd:.2f} Pa/m\n"
                f"Pressure drop over 300 m: {300 * pd:.2f} m"
            )

            self.text_edit.setText(result_text)

        except ValueError:
            self.text_edit.setText("Please enter valid numbers in all input fields.")

        except ZeroDivisionError:
            self.text_edit.setText("Diameter and kinematic viscosity must be greater than zero.")

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()