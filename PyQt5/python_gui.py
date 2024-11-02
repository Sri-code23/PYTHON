import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class my_class(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,400,300,200)
        self.setWindowTitle("My GUI")
        self.setWindowIcon(QIcon("profilepicture.jpg"))

def main():
    app=QApplication(sys.argv)
    gui_window=my_class()
    gui_window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()

print(help(sys))

