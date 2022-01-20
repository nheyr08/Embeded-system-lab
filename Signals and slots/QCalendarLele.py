from PyQt5.QtWidgets import QApplication, QDialog,\
    QVBoxLayout, QCalendarWidget, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont

class Window(QDialog):
    def __init__(self):
        super().__init__()


        #window requrements like geometry,icon and title
        self.setGeometry(200,200,400,200)
        self.setWindowTitle("PyQt5 QCalendar")
        self.setWindowIcon(QIcon("python.png"))
        
        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.calendar_date)

        self.label =QLabel("Hello")
        self.label.setFont(QFont("Sanserif", 15))
        self.label.setStyleSheet('color:red')

        vbox.addWidget(self.calendar)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def calendar_date(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate())

        self.label.setText("Date Is : " + date_in_string)


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())