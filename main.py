import multiprocessing
from time import sleep

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from win32api import GetSystemMetrics
try:
    import application as app
except Exception as e:
    from assistant import TextToSpeak
    print(f"error: {e}\n")
    print(
        "Missing Vlc Media Player!!!\n Make sure VlC player is Download and in the \"program files\" directory, before running this program\nIf not download here: https://www.videolan.org/vlc/download-windows.html ")
    TextToSpeak("Missing Vlc Media Player!!!\n Make sure VlC player is Download and in the program files directory, before running this program. here is the link")
    sleep(10)
    sys.exit(404)


def assistant():
    app.TextToSpeak("")
    app.TextToSpeak("")
    app.TextToSpeak("")
    app.assistant()


assistantProcess = multiprocessing.Process(target=assistant, args=())


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        # setting geometry
        self.setGeometry(100, 100, 400, 300)
        # calling method
        self.UiComponents()
        # showing all the widgets
        self.showFullScreen()
        # assistant()

    # method for widgets
    def UiComponents(self):
        # creating label
        label = QLabel(self)
        # setting geometry to label
        label.setGeometry(0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
        # loading image
        pixmap = QPixmap('res/images/audimax_assisted_bg.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.resize(GetSystemMetrics(0), GetSystemMetrics(1))

        # label1 = QLabel(self)
        # label1.setGeometry(0, 0, 500, 500)
        # movie = QMovie("res/images/bg-assited.gif")
        # label1.setMovie(movie)
        # # label1.setScaledContents(True)
        # label1.resize(GetSystemMetrics(0), GetSystemMetrics(1))
        # movie.start()


def pyQtWindow():
    # create pyqt5 app
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()
    # start the app
    sys.exit(App.exec())


windowProcess = multiprocessing.Process(target=pyQtWindow, args=())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    multiprocessing.freeze_support()
    windowProcess.start()
    assistantProcess.start()
    while windowProcess.is_alive() and assistantProcess.is_alive():
        sleep(1)
    for process in multiprocessing.process.active_children():
        process.terminate()
    app.TextToSpeak("Audi-Max Shutting Down")
    sys.exit(100)


