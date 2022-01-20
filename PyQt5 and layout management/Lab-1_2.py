import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QGridLayout,
                             QVBoxLayout)
from PyQt5.QtCore import QSize

class ToDoList(QWidget):
    def __init__(self):  # Constructor
        super().__init__()
        self.initializeUI()
        self.label()
        self.show()
       
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(500, 500, 600, 800)
        self.setWindowTitle('Lab1-2 ToDo List GUI')
        self.setupWidgets()
        

        self.setMinimumSize(QSize(100, 20))    
        self.setWindowTitle("Checkbox")
        k=0 
        for i in range (20):
           
            self.b = QCheckBox(self)
            self.b.move(20,10+k)
            self.b.resize(320,100)
            k=k+50
        t=0
        for i in range (20):
            self.name=QLineEdit(self)
            self.name.setPlaceholderText("write here")
            self.name.move(50,50+t)
            t=t+50
     
        t=0
        for i in range (3):
            self.Morning =QTextEdit(self)
            self.Morning.move(300, 50+t)
            t=t+250
        
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)
        close_button.move(250,750)

    def setupWidgets(self):
        main_grid = QGridLayout()
        todo_title = QLabel("To Do List")
        todo_title.setFont(QFont('Arial', 24))
        todo_title.setAlignment(Qt.AlignCenter)
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        
# Create section labels for to-do list
# Create must-do section

        # Create checkboxes and line edit widgets
    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')
    appt_v_box = QVBoxLayout()
    appt_v_box.setContentsMargins(5, 5, 5, 5)
    def label(self):

        t=0
        for i in["Morning ","Noon","Evening"]:
            text = QLabel(self)
            text.setText(i)
            text.setFont(QFont('Arial', 18))
            text.move(400, 30+t)
            t=t+250
        t=0

        for i in ["Must Dos","Appointment"]:
            text = QLabel(self)
            text.setText(i)
            text.setFont(QFont('Arial', 24))
            text.move(50+t, 0)
            t=t+300
    
        
        
        self.name=QLineEdit(self)
        self.name.setPlaceholderText("李松磊")
        self.name.move(200,50) 
        
    
        # Create labels for appointments section
    
        # Create vertical layout and add widgets

        # Add other layouts to main layout
     
      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoList()
    sys.exit(app.exec_())
