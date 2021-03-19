from PyQt5 import QtCore, QtGui, QtWidgets
import operations
import subprocess
import datetime
import threading


class Ui_MainWindow(object):
    def __init__(self):
        self.sptime=60
        self.exit_event=threading.Event()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 575)
        font = QtGui.QFont()
        font.setFamily("Miriam")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shutButton = QtWidgets.QPushButton(self.centralwidget)
        self.shutButton.setGeometry(QtCore.QRect(850, 490, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.shutButton.setFont(font)
        self.shutButton.setObjectName("shutButton")
        self.shutButton.clicked.connect(self.Shutdown)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 991, 81))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.stopButton = QtWidgets.QPushButton(self.groupBox)
        self.stopButton.setGeometry(QtCore.QRect(300, 20, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.stopButton.clicked.connect(self.Stop)
        self.pauseButton = QtWidgets.QPushButton(self.groupBox)
        self.pauseButton.setGeometry(QtCore.QRect(560, 20, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.pauseButton.setFont(font)
        self.pauseButton.setObjectName("pauseButton")
        self.pauseButton.clicked.connect(self.Pause)
        self.resumeButton = QtWidgets.QPushButton(self.groupBox)
        self.resumeButton.setGeometry(QtCore.QRect(800, 20, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.resumeButton.setFont(font)
        self.resumeButton.setObjectName("resumeButton")
        self.resumeButton.clicked.connect(self.Resume)
        self.startButton = QtWidgets.QPushButton(self.groupBox)
        self.startButton.setGeometry(QtCore.QRect(30, 20, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.Start)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 201, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinTime = QtWidgets.QSpinBox(self.centralwidget)
        self.spinTime.setGeometry(QtCore.QRect(230, 120, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(36)
        self.spinTime.setFont(font)
        self.spinTime.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinTime.setMaximum(120)
        self.spinTime.setProperty("value", 60)
        self.spinTime.setObjectName("spinTime")
        self.spinTime.valueChanged.connect(self.timerset)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.timerLabel = QtWidgets.QLabel(self.centralwidget)
        self.timerLabel.setGeometry(QtCore.QRect(750, 120, 141, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.timerLabel.setFont(font)
        self.timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerLabel.setObjectName("timerLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 220, 361, 251))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 70, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 130, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 180, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.f1Speed = QtWidgets.QSpinBox(self.groupBox_2)
        self.f1Speed.setGeometry(QtCore.QRect(170, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(30)
        self.f1Speed.setFont(font)
        self.f1Speed.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.f1Speed.setMouseTracking(False)
        self.f1Speed.setWrapping(False)
        self.f1Speed.setFrame(True)
        self.f1Speed.setReadOnly(False)
        self.f1Speed.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.f1Speed.setMaximum(10)
        self.f1Speed.setProperty("value", operations.f1)
        self.f1Speed.setObjectName("f1Speed")
        self.f1Speed.valueChanged.connect(self.F1speed)
        self.m1Speed = QtWidgets.QSpinBox(self.groupBox_2)
        self.m1Speed.setGeometry(QtCore.QRect(170, 70, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(30)
        self.m1Speed.setFont(font)
        self.m1Speed.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.m1Speed.setMaximum(10)
        self.m1Speed.setProperty("value", operations.m1)
        self.m1Speed.setObjectName("m1Speed")
        self.m1Speed.valueChanged.connect(self.M1speed)
        self.m2Speed = QtWidgets.QSpinBox(self.groupBox_2)
        self.m2Speed.setGeometry(QtCore.QRect(170, 130, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(30)
        self.m2Speed.setFont(font)
        self.m2Speed.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.m2Speed.setMaximum(10)
        self.m2Speed.setProperty("value", operations.m2)
        self.m2Speed.setObjectName("m2Speed")
        self.m2Speed.valueChanged.connect(self.M2speed)
        self.f2Speed = QtWidgets.QSpinBox(self.groupBox_2)
        self.f2Speed.setGeometry(QtCore.QRect(170, 190, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(30)
        self.f2Speed.setFont(font)
        self.f2Speed.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.f2Speed.setMaximum(10)
        self.f2Speed.setProperty("value", operations.f2)
        self.f2Speed.setObjectName("f2Speed")
        self.f2Speed.valueChanged.connect(self.F2speed)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 230, 231, 251))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.mode1 = QtWidgets.QPushButton(self.groupBox_3)
        self.mode1.setGeometry(QtCore.QRect(20, 20, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.mode1.setFont(font)
        self.mode1.setObjectName("mode1")
        self.mode1.clicked.connect(self.Mode1)
        self.mode2 = QtWidgets.QPushButton(self.groupBox_3)
        self.mode2.setGeometry(QtCore.QRect(20, 70, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.mode2.setFont(font)
        self.mode2.setObjectName("mode2")
        self.mode2.clicked.connect(self.Mode2)
        self.mode3 = QtWidgets.QPushButton(self.groupBox_3)
        self.mode3.setGeometry(QtCore.QRect(20, 130, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.mode3.setFont(font)
        self.mode3.setObjectName("mode3")
        self.mode3.clicked.connect(self.Mode3)
        self.mode4 = QtWidgets.QPushButton(self.groupBox_3)
        self.mode4.setGeometry(QtCore.QRect(20, 190, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.mode4.setFont(font)
        self.mode4.setObjectName("mode4")
        self.mode4.clicked.connect(self.Mode4)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(670, 230, 331, 251))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.musicVolume = QtWidgets.QSlider(self.groupBox_4)
        self.musicVolume.setGeometry(QtCore.QRect(10, 170, 301, 61))
        self.musicVolume.setMaximum(100)
        self.musicVolume.setSingleStep(5)
        self.musicVolume.setProperty("value", 50)
        self.musicVolume.setOrientation(QtCore.Qt.Horizontal)
        self.musicVolume.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.musicVolume.setTickInterval(5)
        self.musicVolume.setObjectName("musicVolume")
        self.musicVolume.valueChanged.connect(self.volumec)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.music1 = QtWidgets.QRadioButton(self.groupBox_4)
        self.music1.setGeometry(QtCore.QRect(20, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.music1.setFont(font)
        self.music1.setObjectName("music1")
        self.music1.clicked.connect(self.Music1)
        self.music2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.music2.setGeometry(QtCore.QRect(20, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.music2.setFont(font)
        self.music2.setObjectName("music2")
        self.music2.clicked.connect(self.Music2)
        self.music3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.music3.setGeometry(QtCore.QRect(180, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.music3.setFont(font)
        self.music3.setObjectName("music3")
        self.music3.clicked.connect(self.Music3)
        self.music4 = QtWidgets.QRadioButton(self.groupBox_4)
        self.music4.setGeometry(QtCore.QRect(180, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(16)
        self.music4.setFont(font)
        self.music4.setObjectName("music4")
        self.music4.clicked.connect(self.Music4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 480, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(14)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(920, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(600, 130, 161, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VAKAI CONSOLE"))
        self.shutButton.setText(_translate("MainWindow", "SHUTDOWN"))
        self.shutButton.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.stopButton.setText(_translate("MainWindow", "STOP"))
        self.pauseButton.setText(_translate("MainWindow", "PAUSE"))
        self.resumeButton.setText(_translate("MainWindow", "RESUME"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.label.setText(_translate("MainWindow", "Session Time:"))
        self.label_2.setText(_translate("MainWindow", "mins"))
        self.timerLabel.setText(_translate("MainWindow", "00"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Settings"))
        self.label_4.setText(_translate("MainWindow", "F1 Speed:"))
        self.label_5.setText(_translate("MainWindow", "M1 Speed:"))
        self.label_6.setText(_translate("MainWindow", "M2 Speed:"))
        self.label_7.setText(_translate("MainWindow", "F2 Speed:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Mode Selection"))
        self.mode1.setText(_translate("MainWindow", "High"))
        self.mode2.setText(_translate("MainWindow", "Mid"))
        self.mode3.setText(_translate("MainWindow", "Default"))
        self.mode4.setText(_translate("MainWindow", "LOW"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Music Selection"))
        self.label_3.setText(_translate("MainWindow", "Music Volume"))
        self.music1.setText(_translate("MainWindow", "Music 1"))
        self.music2.setText(_translate("MainWindow", "Music 2"))
        self.music3.setText(_translate("MainWindow", "Music 3"))
        self.music4.setText(_translate("MainWindow", "Music 4"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Total Run Time"))
        self.label_8.setText(str(operations.get_totalrun_time()))
        self.label_10.setText(_translate("MainWindow", "mins"))
        self.label_11.setText(_translate("MainWindow", "Time Left:"))

###################################### User define functions ###########################################
    def Start(self):
        print("Start pressed!")
        self.timerLabel.setText(str(self.sptime))
        self.exit_event.clear()
        clock = threading.Thread(target=self.runtimer,args=[self.sptime])
        clock.start()
        operations.started=1
        operations.play_music()
        operations.serial_update()
    def Stop(self):
        print("Stop pressed!")
        self.exit_event.set()
        operations.started = 0
        operations.stop_music()
        runtime=int(self.sptime)-int(self.timerLabel.text())
        operations.set_totalrun_time(runtime)
        operations.serial_stop()
    def Resume(self):
        print("Resume pressed!")
        self.exit_event.clear()
        clock = threading.Thread(target=self.runtimer, args=[int(self.timerLabel.text())])
        clock.start()
        operations.started = 1
        operations.play_music()
        operations.serial_update()
    def Pause(self):
        print("Pause pressed!")
        self.exit_event.set()
        operations.started = 0
        operations.stop_music()
        operations.serial_stop()
    def Mode1(self):
        operations.f1=operations.f2=operations.m1=operations.m2=10
        self.f1Speed.setValue(operations.f1)
        self.f2Speed.setValue(operations.f2)
        self.m1Speed.setValue(operations.m1)
        self.m2Speed.setValue(operations.m2)
    def Mode2(self):
        operations.f1=operations.f2=operations.m1=operations.m2=7
        self.f1Speed.setValue(operations.f1)
        self.f2Speed.setValue(operations.f2)
        self.m1Speed.setValue(operations.m1)
        self.m2Speed.setValue(operations.m2)
    def Mode3(self):
        operations.f1=operations.f2=operations.m1=operations.m2=5
        self.f1Speed.setValue(operations.f1)
        self.f2Speed.setValue(operations.f2)
        self.m1Speed.setValue(operations.m1)
        self.m2Speed.setValue(operations.m2)
    def Mode4(self):
        operations.f1=operations.f2=operations.m1=operations.m2=2
        self.f1Speed.setValue(operations.f1)
        self.f2Speed.setValue(operations.f2)
        self.m1Speed.setValue(operations.m1)
        self.m2Speed.setValue(operations.m2)
    def volumec(self,x):
        operations.changevol(x/100)
    def Shutdown(self):
        print("Shutdown initiated!")
        subprocess.call(["shutdown", "-h", "now"])
    def timerset(self,min):
        self.sptime=int(min)
        print(min)
    def F1speed(self,speed):
        operations.f1=speed
        if operations.started==1:
            operations.serial_update()
    def F2speed(self,speed):
        operations.f2=speed
        if operations.started == 1:
            operations.serial_update()
    def M1speed(self,speed):
        operations.m1=speed
        if operations.started == 1:
            operations.serial_update()
    def M2speed(self,speed):
        operations.m2=speed
        if operations.started == 1:
            operations.serial_update()
    def Music1(self):
        operations.songname='m1'
    def Music2(self):
        operations.songname = 'm2'
    def Music3(self):
        operations.songname = 'm3'
    def Music4(self):
        operations.songname = 'm4'
    def total_Time(self):
        self.label_8.setText(operations.totalrun_time())

    def runtimer(self, run_min):
        now = datetime.datetime.now()
        start_time = now.strftime("%H:%M")
        future = now + datetime.timedelta(minutes=run_min)
        stop_time = future.strftime("%H:%M")
        print("Session will stop at:", stop_time)
        FMT = '%H:%M'
        tdelta = datetime.datetime.strptime(stop_time, FMT) - datetime.datetime.strptime(start_time, FMT)
        str_tdata = str(tdelta).split(':')
        min = (int(str_tdata[0]) * 60) + int(str_tdata[1])
        lasttime = min
        while lasttime != 0:
            now = datetime.datetime.now()
            start_time = now.strftime("%H:%M")
            tdelta = datetime.datetime.strptime(stop_time, FMT) - datetime.datetime.strptime(start_time, FMT)
            str_tdata = str(tdelta).split(':')
            min = (int(str_tdata[0]) * 60) + int(str_tdata[1])
            if min == lasttime:
                pass
            else:
                #print("left time: ", min)
                self.timerLabel.setText(str(min))
                lasttime = min
            if self.exit_event.isSet():
                break
        else:
            self.Stop()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
