import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel
from PyQt5.QtGui import QIcon,QFont

class my_class(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000,200,600,600)
        self.setWindowTitle("My GUI")
        label=QLabel("vanakam",self)
        label.setFont(QFont("arial",35))
        label.setStyleSheet("color:red;" "background-color:blue;" "background")
        label.setGeometry(10,20,200,300)

def main():
    app=QApplication(sys.argv)
    gui_window=my_class()
    gui_window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()



