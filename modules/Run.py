import sys
from datetime import datetime, timedelta

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

import AutoLogin, UI

# pyinstaller -w -F --add-binary "chromedriver.exe";"." Run.py
# pyinstaller --onefile --noconsole --add-binary "chromedriver.exe";"." Run.py


# main class
class MainWindow(QDialog, UI.Ui_Form):  # , UI.Ui_Form):
    def __init__(self):
        # super(MainWindow, self).__init__()
        QDialog.__init__(self, None)
        self.setupUi(self)
        self.register_button.clicked.connect(self.run)
        now = datetime.now()
        after_one_week = now + timedelta(weeks=2)
        print(after_one_week, type(after_one_week))
        Date = str(after_one_week)
        print(Date[0:10])
        self.game_year.setPlainText(Date[0:4])
        self.game_month.setPlainText(Date[5:7])
        self.game_day.setPlainText(Date[8:10])

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
    app = QtWidgets.QApplication(sys.argv)

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
