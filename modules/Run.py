import sys

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from modules import AutoLogin

UI = '../ui/register_form.ui'
# global game_name, game_numbers, game_year, game_month, game_leader, \
#             game_day, game_start, game_end, first_number, second_number


# main class
class MainWindow(QDialog):  # , UI.Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(UI, self)
        self.register_button.clicked.connect(self.run)

    def run(self):

        game_name = self.game_name.toPlainText()
        game_numbers = self.game_numbers.toPlainText()
        game_year = self.game_year.toPlainText()
        game_month = self.game_month.toPlainText()
        game_day = self.game_day.toPlainText()
        game_start = self.game_start.toPlainText()
        game_end = self.game_end.toPlainText()
        game_leader = self.game_leader.toPlainText()
        first_number = self.first_number.toPlainText()
        second_number = self.second_number.toPlainText()

        print(game_name, game_numbers, game_leader, game_start,
              game_end, game_year, game_month, game_day,
              first_number, second_number)
        print(type(game_name), type(game_numbers), type(game_leader), type(game_start),
              type(game_end), type(game_year), type(game_month), type(game_day),
              type(first_number), type(second_number))

        AutoLogin.autoLogin(game_name, game_numbers, game_leader, game_start,
                            game_end, game_year, game_month, game_day, first_number, second_number)


if __name__ == "__main__":
    # QApplication : The Class For Running Program
    app = QApplication(sys.argv)

    # Option UI Change
    widget = QtWidgets.QStackedWidget()

    # Create Layout Instance
    mainWindow = MainWindow()

    # Add Widget & Sequence Open
    widget.addWidget(mainWindow)

    # Show UI
    widget.show()

    # Running Event Loop
    app.exec_()