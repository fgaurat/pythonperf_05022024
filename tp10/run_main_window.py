from main_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.doClick)

    def doClick(self):
        print("doClick")




def main():
    app = QApplication([])
    window = MainWindow()
    window.show()

    app.exec()



if __name__=='__main__':
    main()
