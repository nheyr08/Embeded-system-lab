import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot 


class HelloWorldWindow(QWidget):
   
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.show()

    def initializeUI(self):
        k=50
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Lab 1')
        self.displayLabels()
        self.name=QLineEdit(self)
        self.name.setPlaceholderText("李松磊")
        self.name.move(50,60) 
        
        for a in  ['enter yr name:','enter yr Fullname:']:
            
            self.name=QLineEdit(self)
            self.name.setPlaceholderText(a)
            self.name.move(200,150+k)
            k=k+40
        self.pswd_entry = QLineEdit(self)
        self.pswd_entry.setEchoMode(QLineEdit.Password)
        self.name=QLineEdit(self)
        #self.LeUsuario.setEchoMode(QtWidgets.QLineEdit.Password)
        self.name.setPlaceholderText("Enter yr Password:")
        self.name.move(200,150+k)
        self.pswd_entry = QLineEdit(self)
        self.pswd_entry.setEchoMode(QLineEdit.Password)
        self.name=QLineEdit(self)
        #self.LeUsuario.setEchoMode(QtWidgets.QLineEdit.Password)
        self.name.setPlaceholderText("Confirm")
        self.name.move(200,150+k+40)
           
        button= QPushButton('Submit',self)
        button.move(220,370)
        button.clicked.connect(self.On_click)
    @pyqtSlot()
    def On_click(self):
        print('Submit')

    def displayLabels(self):
        """
        Display text and images using QLabels.
        Check to see if image files exist, if not throw an
        exception.
        """
        text = QLabel(self)
        text.setText("Create New Account")
        text.setFont(QFont('Arial', 24))
        text.move(150, 30)
        k=50
        for a in  ['Username:','Fullname:','Password:','Confirm:']:
            text = QLabel(self)
            text.setText(a) 
            text.move(75,150+k )
            k=k+40

        image = "image/face-with-tears-of-joy.png"
        try:
            with open(image):
                emoji = QLabel(self)
                pixmap = QPixmap(image)
                emoji.setPixmap(pixmap)
                emoji.move(200, 75)
        except FileNotFoundError:
            print("Image not found.")
    
    
# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    sys.exit(app.exec_())
