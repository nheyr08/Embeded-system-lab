import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QMessageBox,
                             QLineEdit, QPushButton, QCheckBox)

from Registration import CreateNewUser  # import the registration module


class LoginUI(QWidget):

    def __init__(self):  # constructor
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle('Lab2-1 Login GUI')
        self.loginUserInterface()

        self.show()

    def loginUserInterface(self):
        """
        Create the login GUI.
        """
        login_label = QLabel(self)
        login_label.setText("login")
        login_label.move(180, 10)
        login_label.setFont(QFont('Arial', 20))

        # username and password labels and line edit widgets
        name_label = QLabel("username:", self)
        name_label.move(30, 60)

        self.name_entry = QLineEdit(self)
        self.name_entry.move(110, 60)
        self.name_entry.resize(220, 20)

        password_label = QLabel("password:", self)
        password_label.move(30, 90)

        self.password_entry = QLineEdit(self)
        self.password_entry.move(110, 90)
        self.password_entry.resize(220, 20)

        # sign in push button
        sign_in_button = QPushButton('login', self)
        sign_in_button.move(100, 140)
        sign_in_button.resize(200, 40)
        # TODO: Connect to self.clickLogin

        # display show password check box
        show_password_cb = QCheckBox("show password", self)
        show_password_cb.move(110, 115)
        # TODO: Connect to self.displayPassword, check hint if you don't know how
        show_password_cb.toggle()
        show_password_cb.setChecked(False)

        # display sign up label and push button
        not_a_member = QLabel("not a member?", self)
        not_a_member.move(70, 200)

        sign_up = QPushButton("sign up", self)
        sign_up.move(160, 195)
        # TODO: Connect to self.createNewUser

    def clickLogin(self):
        """
        When user clicks sign in button, check if username and password
        match any existing profiles in users.txt.
        If they exist, display messagebox and close program.
        If they don't, display error messagebox.
        """
        users = {}  # create empty dictionary to store user information
        # check if users.txt exists, otherwise create new file
        try:
            with open("files/users.txt", 'r') as f:
                # TODO: parse file and put data in 'users' dict declared above, username as key, password as value
                pass

        except FileNotFoundError:
            print("The file does not exist. Creating a new file.")
            f = open("files/users.txt", "w")

        username = self.name_entry.text()
        password = self.password_entry.text()
        if (username, password) in users.items():
            # TODO: show a information msg box to tell user that login successful
            self.close()  # close program
        else:
            # TODO: show a warning msg box to tell user that username or password incorrect
            self.name_entry.clear()
            self.password_entry.clear()

    def displayPassword(self, state):
        """
        If checkbutton is enabled, view password.
        Else, mask password so others can not see it.
        """
        if state == Qt.Checked:
            self.password_entry.setEchoMode(QLineEdit.Normal)
        else:
            self.password_entry.setEchoMode(QLineEdit.Password)

    def createNewUser(self):
        """
        When the sign up button is clicked, open
        a new window and allow the user to create a new account.
        """
        self.create_new_user_dialog = CreateNewUser()
        self.create_new_user_dialog.show()

    def closeEvent(self, event):
        """
        Display a QMessageBox when asking the user if they want to
        quit the program.
        """
        # set up message box
        answer = QMessageBox.question(self, "Quit Application?",
                                      "Are you sure you want to Quit?", QMessageBox.No | QMessageBox.Yes,
                                      QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            event.accept()  # accept the event and close the application
        else:
            event.ignore()  # ignore the close event


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginUI()
    sys.exit(app.exec_())
