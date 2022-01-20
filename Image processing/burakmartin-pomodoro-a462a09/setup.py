from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QSpinBox, QLabel, QLineEdit
import sys
from PyQt5.QtGui import QIcon

class Window(QDialog):
    def __init__(self):
        super().__init__()


        #our window requirements like icon,title
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("PyQt5 SpinBox")
        self.setWindowIcon(QIcon("python.png"))

        self.create_spinbox()


    def create_spinbox(self):

        #cretae hboxlayout
        hbox = QHBoxLayout()

        #in here we have created our label
        label = QLabel("Laptop Price : ")

        #this is our linedit
        self.lineEdit = QLineEdit()

        #we need to create the object of QSpinBox class
        self.spinbox = QSpinBox()

        #we have connected valueChanged signal
        self.spinbox.valueChanged.connect(self.spin_selected)
        self.totalResult = QLineEdit()


        #add widgets to your hbox layout
        hbox.addWidget(label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.totalResult)


        self.setLayout(hbox)


    def spin_selected(self):
        if self.lineEdit.text() != 0:
            price = int(self.lineEdit.text())
            totalPrice = self.spinbox.value() * price

            self.totalResult.setText(str(totalPrice))


        else:
            print("Wrong value")


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())