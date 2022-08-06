from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
import sys
import os


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('form.ui', self)
        # list file names
        self.name_folders = ['BAD', 'GOOD', 'STRANGE']
        # start value
        self.directory_name = ""
        self.file_names = None

        self.button_open_directory = self.findChild(QPushButton, 'pushButton')
        self.button_create_folders = self.findChild(QPushButton, 'pushButton_2')
        self.button_go = self.findChild(QPushButton, 'pushButton_3')
        self.button_move_bad = self.findChild(QPushButton, 'pushButton_4')
        self.button_move_good = self.findChild(QPushButton, 'pushButton_5')
        self.button_move_strange = self.findChild(QPushButton, 'pushButton_6')

        self.label_img = self.findChild(QLabel, 'label')

        self.button_open_directory.clicked.connect(self.button_open_directory_clicked)
        self.button_create_folders.clicked.connect(self.button_create_folders_clicked)
        self.button_go.clicked.connect(self.button_go_clicked)
        self.button_move_bad.clicked.connect(self.button_move_bad_clicked)
        self.button_move_good.clicked.connect(self.button_move_good_clicked)
        self.button_move_strange.clicked.connect(self.button_move_strange_clicked)

    # print img to label
    def print_img(self):
        pixmap = QPixmap(self.directory_name + '\\' + self.file_names[0])
        self.label_img.setPixmap(pixmap.scaled(1000, 1000, aspectRatioMode=1))

    def button_open_directory_clicked(self):
        self.directory_name = QFileDialog.getExistingDirectory(self, "OPEN!!",
                                                               'C:\\Users\\petrs\\PycharmProjects',
                                                                QFileDialog.ShowDirsOnly)

    def is_files_empty(self):
        if self.file_names:
            self.print_img()
        else:
            self.label_img.setText("It's All..")

    def button_create_folders_clicked(self):
        for name in self.name_folders:
            os.mkdir(self.directory_name + '\\' + name)

    def button_move_bad_clicked(self):
        os.replace(self.directory_name + '\\' + self.file_names[0],
                   self.directory_name + '\\' + 'BAD\\' + self.file_names[0])
        del self.file_names[0]
        self.is_files_empty()

    def button_move_good_clicked(self):
        os.replace(self.directory_name + '\\' + self.file_names[0],
                   self.directory_name + '\\' + 'GOOD\\' + self.file_names[0])
        del self.file_names[0]
        self.is_files_empty()

    def button_move_strange_clicked(self):
        os.replace(self.directory_name + '\\' + self.file_names[0],
                   self.directory_name + '\\' + 'STRANGE\\' + self.file_names[0])
        del self.file_names[0]
        self.is_files_empty()

    def button_go_clicked(self):

        with os.scandir(self.directory_name) as files:
            self.file_names = []
            for file in files:
                if file.is_file():
                    self.file_names.append(file.name)
        self.file_names.sort()
        self.is_files_empty()


def main():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

