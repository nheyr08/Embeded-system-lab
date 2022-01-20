from PyQt5.QtWidgets import QApplication,QDialog,QLCDNumber,QVBoxLayout
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTime, QTimer

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,400,200)
        self.setWindowTitle("Lele's LCD")

        timer= QTimer()
        timer.timeout.connect(self.lcd_number)

        timer.start(1000)
        self.lcd_number()

    def lcd_number(self):
        vbox=QVBoxLayout()
        lcd = QLCDNumber()
        lcd.setStyleSheet('background: green')
        vbox.addWidget(lcd)

        time=QTime.currentTime()
        text=time.toString('hh:mm')
        lcd.display(text)
        self.setLayout(vbox)
App=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(App.exec())

