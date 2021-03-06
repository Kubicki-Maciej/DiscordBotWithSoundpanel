# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_concept.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import this

import settings as S
import files as F
import Sound as SoundP
from PyQt5 import QtCore, QtGui, QtWidgets


class Manager:

    def __init__(self):
        self.path = None


manager = Manager()

player = SoundP.player_obj
te = F.test


def get_path():
    path = 1
    print(path)


def playsong(path):
    manager.path = path
    print(manager.path)

    # player.load_file(path)
    # player.play_sound()


def stopplay():
    player.stop_play()


def volume_up():
    if player.volume < 1:
        player.volume += 0.1
        player.change_volume()


def volume_down():
    if player.volume > 0:
        player.volume -= 0.1
        player.change_volume()


class Button:

    def __init__(self):
        self.button_name = None
        self.button_x = 0
        self.button_y = 0
        self.button_class = None
        self.button_t = None
        self.button_path = None
        self.click = None

    def take_path(self):
        pass

    def play_sound(self):
        #
        # manager.path = self.button_path
        # print(manager.path)
        """ methods that run sounds from discord i hope so  """
        print(" player.load_file(self.button_path)")
        player.load_file(self.button_path)
        print("player.discord_play_file()")
        player.discord_play_file()


        """ methods that run sounds localy """
        # player.load_file(self.button_path)
        # player.play_sound()


        #
        # import discord
        # from discord import FFmpegPCMAudio
        # from discord.ext import commands
        # import auth as a
        #
        # intents = discord.Intents.default()
        # intents.members = True
        #
        #
        #
        # client = commands.Bot(command_prefix="!", intents=intents)
        #
        # @client.event
        # async def on_ready():
        #     print("Bot is ready to use")
        #     print("*******************")
        #
        # @client.command(pass_context=True)
        # async def player(ctx):
        #
        #     if ctx.author.voice:
        #         channel = ctx.message.author.voice.channel
        #         voice = await channel.connect()
        #         source = FFmpegPCMAudio(manager.path)
        #         player = voice.play(source)
        #
        #     else:
        #         await ctx.send("you are not in voice channel")
        # client.run(a.token)

    def button_type(self, len_list):
        if len_list > 30:
            self.button_type = "smallbutton"
        else:
            self.button_type = "bigbutton"


class Tabs:

    def __init__(self, obj):
        self.nested_obj = obj
        self.table_name = None
        self.object_list = []  # can take files or file needed to create
        self.name_list = []

        self.tab = None

        # self.tab = QtWidgets.QWidget()
        # self.tab.setObjectName(self.table_name)
        # self.tabWidget.addTab(self.tab, "")

    def make_list(self):
        for item in self.nested_obj:
            self.object_list.append(item)


class Ui_MainWindow(object):

    def __init__(self):
        self.button_objects = []
        self.tabs_objects = []
        self.logic_for_tabs_create(te)
        self.button_listener = []

    def button_list(self):
        """ function not used"""
        for tmp_btn in self.button_objects:
            click = tmp_btn.button_class.clicked.connect(lambda: playsong(tmp_btn.button_path))

            self.button_listener.append(click)

    def logic_for_tabs_create(self, object_form_files):
        """first tab crated is list folders, as name take path """
        first_file_list = object_form_files.new_class_files
        FirstTab = Tabs(first_file_list)
        FirstTab.make_list()
        FirstTab.table_name = "Folders"

        self.tabs_objects.append(FirstTab)
        x = 1
        for file in FirstTab.object_list:
            temp_obj = Tabs(file)
            temp_obj.object_list = temp_obj.nested_obj.objects_music
            temp_obj.table_name = temp_obj.nested_obj.name
            self.tabs_objects.append(temp_obj)

        # return self.tabs_objects

    def tab_adder(self, tabs_obj, widget):
        """add tab"""

        for obj in tabs_obj:
            print("tworze tab" + obj.table_name)
            obj.tab = QtWidgets.QTabWidget()
            obj.tab.setObjectName(obj.table_name)
            widget.addTab(obj.tab, "")

    def button_adder(self, tabs_objs):
        files = tabs_objs[0]
        # for files in tabs_objs:
        # pierw logika tworzenia dla jednej wybranej tabeli files
        width = S.btn_w
        # start x,y values
        x = 10
        y = 10

        if len(files.object_list) > 30:
            height = S.btn_h
        else:
            height = S.big_btn_h

        # check len list if files.objec_list > 30 add small buttons if not take from s big buttons
        for file in files.object_list:
            if x > 700:
                y += height + 10
                x = 10

            tmp_btn = Button()
            tmp_btn.button_name = file.name
            tmp_btn.button_x = x
            tmp_btn.button_y = y
            tmp_btn.button_class = QtWidgets.QPushButton(files.tab)
            tmp_btn.button_class.setGeometry(QtCore.QRect(x, y, width, height))
            tmp_btn.button_class.setStyleSheet(S.button_color)
            tmp_btn.button_class.setCheckable(False)
            tmp_btn.button_class.setObjectName(file.name)
            x += width + 10
            self.button_objects.append(tmp_btn)

        nu = 0
        for j in range(len(tabs_objs) - 1):

            x = 10
            y = 10

            if len(tabs_objs[j + 1].object_list) > 30:
                height = S.btn_h
            else:
                height = S.big_btn_h

            for file in tabs_objs[j + 1].object_list:

                if x > 700:
                    y += height + 10
                    x = 10

                nu += 1
                tmp_btn = Button()
                tmp_btn.button_name = file.file_name
                tmp_btn.button_path = file.file_full_path
                tmp_btn.button_x = x
                tmp_btn.button_y = y
                tmp_btn.button_class = QtWidgets.QPushButton(tabs_objs[j + 1].tab)
                tmp_btn.button_class.setGeometry(QtCore.QRect(x, y, width, height))
                tmp_btn.button_class.setStyleSheet(S.button_color)
                tmp_btn.button_class.setCheckable(False)
                tmp_btn.button_class.setObjectName("button" + str(nu))
                # tmp_btn.button_class.click(print("me"))
                tmp_btn.button_t = "button" + str(nu)
                tmp_btn.click = tmp_btn.button_class.clicked.connect(tmp_btn.play_sound)

                x += width + 10
                self.button_objects.append(tmp_btn)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(840, 620))
        MainWindow.setSizeIncrement(QtCore.QSize(1, 1))
        MainWindow.setStyleSheet("color: rgb(122, 122, 122);\n"
                                 "background-color: rgb(93, 93, 93);")

        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(32, 50, 771, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(5, 5))
        self.tabWidget.setMaximumSize(QtCore.QSize(800, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 138, 138))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)

        # tab created here
        self.tabWidget.setPalette(palette)
        self.tabWidget.setStyleSheet("background-color: rgb(138, 138, 138);\n"
                                     "alternate-background-color: rgb(193, 193, 193);\n"
                                     "border-bottom-color: rgb(156, 156, 156);\n"
                                     "color: rgb(0, 0, 0);")

        self.tabWidget.setIconSize(QtCore.QSize(20, 16))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")

        # tab logic
        # self.tab = QtWidgets.QWidget()
        # self.tab.setObjectName("tab")
        # self.tabWidget.addTab(self.tab, "")

        # add multiple tabs
        self.tab_adder(self.tabs_objects, self.tabWidget)
        # add multiple buttons to ta

        self.button_adder(self.tabs_objects)

        # create button clicks
        # self.button_list()

        # self.Small_button_1 = QtWidgets.QPushButton(self.tab)
        # self.Small_button_1.setGeometry(QtCore.QRect(10, 10, 101, 41))
        # self.Small_button_1.setStyleSheet(S.button_color)
        #
        # self.Small_button_1.setCheckable(False)
        # self.Small_button_1.setObjectName("Small_button_1")
        #
        # self.Big_button_2 = QtWidgets.QPushButton(self.tab)
        #
        # self.Big_button_2.setGeometry(QtCore.QRect(120, 10, 121, 91))
        # self.Big_button_2.setStyleSheet("\n"
        #                                 "color: rgb(0, 0, 0);")

        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(320, 10, 61, 31))
        self.pushButton_14.setStyleSheet("\n"
                                         "color: rgb(0, 0, 0);")
        self.pushButton_14.setCheckable(False)
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(385, 10, 30, 31))
        self.pushButton_16.setStyleSheet("\n"
                                         "color: rgb(0, 0, 0);")
        self.pushButton_16.setCheckable(False)
        self.pushButton_16.setObjectName("pushButton_16")

        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(420, 10, 61, 31))
        self.pushButton_15.setStyleSheet("\n"
                                         "color: rgb(0, 0, 0);")
        self.pushButton_15.setCheckable(False)
        self.pushButton_15.setObjectName("pushButton_15")

        self.pushButton_14.clicked.connect(volume_down)
        self.pushButton_15.clicked.connect(volume_up)
        self.pushButton_16.clicked.connect(stopplay)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.Small_button_1.setText(_translate("MainWindow", "PushButton"))
        # self.Big_button_2.setText(_translate("MainWindow", "PushButton"))

        # tabs class creator
        for ta in self.tabs_objects:
            self.tabWidget.setTabText(self.tabWidget.indexOf(ta.tab), _translate("MainWindow", ta.table_name))

        for btn in self.button_objects:
            btn.button_class.setText(_translate("MainWindow", btn.button_name))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))

        self.pushButton_14.setText(_translate("MainWindow", "Volume -"))
        self.pushButton_16.setText(_translate("MainWindow", "Stop"))
        self.pushButton_15.setText(_translate("MainWindow", "Volume +"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


def run():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
