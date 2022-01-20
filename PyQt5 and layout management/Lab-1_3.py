import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
 
class Dialog(QDialog):
    """Dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        self.setWindowTitle('Application Form GUI')
        
        dlgLayout   = QVBoxLayout()
        formLayout1 = QFormLayout()
        formLayout2 = QFormLayout()
        formLayout3 = QFormLayout()
        formLayout4 = QFormLayout()
        #first part (adding the widgets)
        formLayout1.addRow('Full Name:                    ', QLineEdit())
        formLayout1.addRow('Address:                       ', QLineEdit())
        formLayout1.addRow('Mobile number:                   ', QLineEdit())
        P=QLabel("Age ")
        PP=QLabel("Height")
        PPP=QLabel("Weight")
        QHLayoutInner1=QHBoxLayout()
        Grid=QGridLayout()
        QHLayoutInner1.addWidget(P)
        QHLayoutInner1.addWidget(QSpinBox())
        QHLayoutInner1.addWidget(PP)
        QHLayoutInner1.addWidget(QLineEdit())
        QHLayoutInner1.addWidget(PPP)
        QHLayoutInner1.addWidget(QLineEdit())
        

        P=QFormLayout()
        formLayout2.addRow('', QHLayoutInner1)
        combo_bobot = QComboBox(self)
        combo_bobot.addItem("Male")
        # adding Super Geek to the combobox
        combo_bobot.addItem("Female")
        # adding Ultra Geek to the combobox
        combo_bobot.addItem("Gay")
        formLayout2.addRow('Gender', combo_bobot)
        formLayout2.addRow('Surgeries', QTextEdit())
        
        BloodType=QFormLayout()
        combo_box = QComboBox(self)
        combo_box.addItem("A")
        # adding Super Geek to the combobox
        combo_box.addItem("B")
        # adding Ultra Geek to the combobox
        combo_box.addItem("C")
        BloodType.addRow(' ',combo_box)
        DesiredTime=QHBoxLayout()
        T=QLabel()
        T.setText("Create")
        DesiredTime.addWidget(QLabel('Desired Time'))
        
        commbo_box = QComboBox(self)
        commbo_box.addItem("00")
        # adding Super Geek to the combobox
        commbo_box.addItem("01")
        # adding Ultra Geek to the combobox
        commbo_box.addItem("02")


        comgmbo_box = QComboBox(self)
        comgmbo_box.addItem("AM")
        # adding Super Geek to the combobox
        comgmbo_box.addItem("PM")
       # comgmbo_box.addItem("01")

        DesiredTime.addWidget(QSpinBox()) 
        DesiredTime.addWidget(commbo_box)
        DesiredTime.addWidget(comgmbo_box)
        BloodType.addRow(DesiredTime)

        formLayout3.addRow('Blood Type',BloodType)
        formLayout3.addRow('',QPushButton('Submit Application'))
        

        #formLayout2.addRow("Submit Application", QDialogButtonBox())
       # dlgLayout.addLayout(text)
        dlgLayout.addLayout(formLayout4)
        dlgLayout.addLayout(formLayout1)
        dlgLayout.addLayout(formLayout2)
        dlgLayout.addLayout(formLayout3)
        
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
    