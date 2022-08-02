#!/usr/bin/python3

from PyQt5 import QtCore
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QCursor
import sys, os, time
from playsound import playsound

dirname = os.path.dirname(os.path.abspath(__file__)) + '/'

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Study With Me")
        self.setWindowIcon(QIcon(QPixmap(dirname+'media/icons/coding.svg'))) 
        self.setFixedSize(1900,1000)

        # This line for updateting window for seconds timer       
        QApplication.processEvents()

        menubar = self.menuBar()
        menubar.setObjectName('menu')        

        file_menu = menubar.addMenu('&File')
        help_menu = menubar.addMenu('&Help')
        
        help = QAction(QIcon(dirname+'media/icons/information.svg'), 'ShortCuts', self)
        help.triggered.connect(self.help_info)
        help_menu.addAction(help)

        file_video = QAction(QIcon(dirname+'media/icons/video.svg'), 'Select videofile', self)
        file_video.triggered.connect(self.user_video)
        file_menu.addAction(file_video)

        #VIDEOPLAYER

        '''
        Installing VideoPlayer settings
        '''
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        videoWidget.setFixedSize(1700,1000)
        self.mediaPlayer.setVideoOutput(videoWidget)
 
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(dirname+'media/videos/video1.mp4')))
        self.mediaPlayer.play()

        '''
        Installing Central Widget for Window
        '''
        wid = QWidget(self)
        self.setCentralWidget(wid)
        
        layout = QHBoxLayout()
    
        #CONFIGURATION SIDEBAR

        self.sideLayout = QVBoxLayout()
        self.sideLayout.setObjectName('sideLayout')

        #CONFIGURATION TIMERBAR

        '''
        Timer_is_run variable created for run report timer
        '''
        self.timer_is_run = False

        self.timerLayout = QHBoxLayout()
        self.count_minute = QLabel('25')
        self.count_minute.setObjectName('counter')
        self.count_second = QLabel('00')
        self.count_second.setObjectName('counter')
        self.count_separater = QLabel(':')
        self.count_separater.setObjectName('counter')
    
        self.start_btn = QPushButton('START')
        self.start_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setObjectName('start_btn')

        self.restart_btn = QPushButton()
        self.restart_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.restart_btn.setIcon(QIcon(QPixmap(dirname+'media/icons/restart.png')))
        self.restart_btn.setIconSize(QSize(40,40))
        self.restart_btn.setObjectName('restart_btn')

        self.pause_btn = QPushButton('PAUSE')
        self.pause_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pause_btn.setObjectName('start_btn')

        # Stack
        '''
        Stack_btn created for switch two buttons - restart button and start button
        '''
        self.stack_btn = QStackedWidget()
        self.stack_btn.addWidget(self.start_btn)
        self.stack_btn.addWidget(self.pause_btn)
        # Selected default button for stack
        self.stack_btn.setCurrentWidget(self.start_btn)

        self.timerLayout.addWidget(self.count_minute)
        self.timerLayout.addWidget(self.count_separater)
        self.timerLayout.addWidget(self.count_second)
        '''
        Stretch created for remove empty space between timer labels and timer buttons
        '''
        self.timerLayout.addStretch()
        self.timerLayout.addWidget(self.stack_btn)
        self.timerLayout.addWidget(self.restart_btn)
        self.sideLayout.addLayout(self.timerLayout)


        self.start_btn.clicked.connect(self.start)
        self.restart_btn.clicked.connect(self.restart)
        self.pause_btn.clicked.connect(self.pause)

        
        #CONFIGURATION RADIO BUTTONS IN GROUPBOX

        self.radio_layout = QHBoxLayout()
        self.radio_group = QGroupBox()
        self.radio_group.setObjectName('radio_group')

        self.pomodoro_rad = QRadioButton('Pomodoro')
        self.pomodoro_rad.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pomodoro_rad.setChecked(True)

        self.short_rad = QRadioButton('Short Break')
        self.short_rad.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.long_rad = QRadioButton('Long Break')
        self.long_rad.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.radio_layout.addWidget(self.pomodoro_rad)
        self.radio_layout.addWidget(self.short_rad)
        self.radio_layout.addWidget(self.long_rad)
    
        self.radio_group.setLayout(self.radio_layout)
        self.sideLayout.addWidget(self.radio_group)
        self.sideLayout.addStretch()


        self.pomodoro_rad.clicked.connect(lambda x: self.set_time('25'))
        self.short_rad.clicked.connect(lambda x: self.set_time('5'))
        self.long_rad.clicked.connect(lambda x: self.set_time('15'))


        #CONFIGURATION VIDEO-BUTTONS FOR SELECT BACKGROUND VIDEO

        self.grid_videos = QGridLayout()

        self.create_video_button(icon=f'{dirname}media/icons/study.svg', url=f'{dirname}media/videos/video1.mp4', row=0, column=0, tip='Study with me', cut='1')
        self.create_video_button(icon=f'{dirname}media/icons/abstract.svg', url=f'{dirname}media/videos/video2.mp4', row=0, column=1, tip='Abstaction', cut='2')
        self.create_video_button(icon=f'{dirname}media/icons/landscape.svg', url=f'{dirname}media/videos/video3.mp4', row=0, column=2, tip='River', cut='3')
        self.create_video_button(icon=f'{dirname}media/icons/forest.svg', url=f'{dirname}media/videos/video4.mp4', row=0, column=3, tip='Nature', cut='4')
        self.create_video_button(icon=f'{dirname}media/icons/mountain.svg', url=f'{dirname}media/videos/video5.mp4', row=1, column=0, tip='Mountains', cut='5')
        self.create_video_button(icon=f'{dirname}media/icons/fire.svg', url=f'{dirname}media/videos/video6.mp4', row=1, column=1, tip='Campfire', cut='6')
        self.create_video_button(icon=f'{dirname}media/icons/programming.svg', url=f'{dirname}media/videos/video7.mp4', row=1, column=2, tip='Coding Time', cut='7')
        self.create_video_button(icon=f'{dirname}media/icons/galaxy.svg', url=f'{dirname}media/videos/video8.mp4', row=1, column=3, tip='Space', cut='8')

        
        #CONFIGURATION VOLUME SLIDER
    
        self.volumeLayout = QHBoxLayout()
        self.vol_ico = QPushButton('')
        self.vol_ico.setIcon(QIcon(QPixmap('media/icons/volume.svg')))
        self.vol_ico.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.vol_ico.clicked.connect(lambda: self.vol_slider.setValue(0))
        self.vol_ico.setIconSize(QSize(40,40))
        self.vol_ico.setObjectName('vol_ico')

        self.vol_slider = QSlider()
        self.vol_slider.setOrientation(QtCore.Qt.Horizontal)
        self.vol_slider.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # SET DEFAULT VOLUME LEVEL
        self.vol_slider.setValue(90)
        self.vol_slider.valueChanged.connect(self.change_volume)

        self.volumeLayout.addWidget(self.vol_ico)
        self.volumeLayout.addWidget(self.vol_slider)
        
        self.sideLayout.addLayout(self.volumeLayout)   
        self.sideLayout.addStretch()
        self.sideLayout.addLayout(self.grid_videos)
        self.sideLayout.addStretch(10)

        layout.addLayout(self.sideLayout)
        layout.addWidget(videoWidget)

        wid.setLayout(layout)
        
        self.x = 0 # для колесика мышки

        help.setShortcut('Ctrl+I')
        file_video.setShortcut('Ctrl+O')
        self.vol_ico.setShortcut('Ctrl+M')
        self.long_rad.setShortcut('Ctrl+L')        
        self.short_rad.setShortcut('Ctrl+S')
        self.pomodoro_rad.setShortcut('Ctrl+P')
        self.restart_btn.setShortcut('Esc')
        self.pause_btn.setShortcut('SPACE')
        self.start_btn.setShortcut('SPACE')

    # APP LOGIC 

    '''
    This functions accept five arguments for create button.
    1. Icon take the path for icon button
    2. Url take the video path
    3. Row and Column set place for object
    4. Tip tells about icon video
    '''
    def create_video_button(self, icon, url, row, column, tip, cut):
        self.button = QPushButton()
        self.button.setShortcut(cut)
        self.button.setIcon(QIcon(QPixmap(icon)))
        self.button.setIconSize(QSize(40,40))
        self.button.setObjectName('video_button')
        self.button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button.setToolTip(tip)
        self.button.clicked.connect(lambda x: self.open_video(url))
        self.grid_videos.addWidget(self.button, row, column)


    '''
    Changing the volume with the mouse
    '''
    def wheelEvent(self, event):
        number =  event.angleDelta().y()
        if number == 120:
            self.vol_slider.setValue(self.vol_slider.value() + 3)
        elif number == -120:
            self.vol_slider.setValue(self.vol_slider.value() - 3)

    
    '''
    This method shows the user possible keyboard shortcuts
    '''
    def help_info(self):
        info = '<h4>Hello, World! We have some shortcuts for you!</h4>\n \
                <p>Press <b>Ctrl+I</b> for call Help info</p>\
                <p>Press <b>Ctrl+M</b> for mute volumn</p>\
                <p>Press <b>Ctrl+L</b> for call Long Break</p>\
                <p>Press <b>Ctrl+S</b> for call Short Break</p>\
                <p>Press <b>Ctrl+P</b> for call Pomodoro method</p>\
                <p>Press <b>Ctrl+O</b> for open your videofile.</p>\
                <p>Press <b>SPACE</b> for Pause/Start timer</p>\
                <p>Press <b>Esc</b> for STOP timer</p>\
                <p>You can use numbers keyboard <b>(1-8)</b> for select video</p>'
        
        QMessageBox.about(self, 'About Program', info)


    '''
    When User selected RadioButton this function set right time for timer
    '''

    def set_time(self, minute):
        self.count_minute.setText(minute)
        self.count_second.setText('00')
        self.timer_is_run = False


    '''
    This function tracks changes for volume slider and set current volume video.
    '''
    def change_volume(self):
        volume = self.vol_slider.value()
        if volume == 0:
            self.vol_ico.setIcon(QIcon(QPixmap('media/icons/volume-x.svg')))
            self.mediaPlayer.setVolume(volume)
        else:
            self.vol_ico.setIcon(QIcon(QPixmap('media/icons/volume.svg')))
            self.mediaPlayer.setVolume(volume)


    '''
    After user clicked  button, this function opens the current video 
    '''
    def open_video(self, path):

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.mediaPlayer.play()
    

    '''
    When user clicked Start-button this function be:
    1. Disabled all radio_buttons
    2. Run timer
    3. Replaces start-button with pause-button
    '''
    def start(self):
        self.radio_group.setDisabled(True)
        self.timer_is_run = True    
        self.stack_btn.setCurrentWidget(self.pause_btn)
        self.tik_tak()


    '''
    Timer Logic.
    First, we take the current value of the timestamps to calculate the total number of seconds. 
    The total number of seconds we use to run the report cycle.
    During the loop, we always check whether the user has pressed pause.
    If pressed, we exit the loop and save the last time value to our labels.

    Otherwise, we start checking: 
        If the second is not equal to zero , we subtract one from it, otherwise we look at what minutes are equal to.
        If the minutes are greater than zero, then we subtract one from the minute, and assign the number 59 to the second.
        If there are no minutes and seconds, we exit the cycle

    At the end, we start the sound signal
    '''
    def tik_tak(self):
        min, sec = map(int, (self.count_minute.text(), self.count_second.text()))
        len_seconds = min * 60 + sec
        for s in range(len_seconds):
            QApplication.processEvents()    
            if self.timer_is_run:
                if sec > 0:
                    sec -= 1
                    self.count_second.setText(str(sec))
                    time.sleep(1)
                    # print(self.count_minute.text(), self.count_second.text())
                else:
                    if min > 0:
                        sec = 59
                        min -= 1
                        self.count_second.setText(str(sec))
                        self.count_minute.setText(str(min))
                        time.sleep(1)
                        # print(self.count_minute.text(), self.count_second.text())

        if sec == min == 0:                
            self.radio_group.setDisabled(False)
            self.stack_btn.setCurrentWidget(self.start_btn)
            playsound('media/sounds/over_sound.mp3', True)
            self.timer_is_run = False


    '''
    When user clicked restart button activated this function.ц
    Before exiting the loop, the function checks which button is currently active to replace the text on the label
    '''    
    def restart(self):
        times = {
            'Pomodoro': '25',
            'Short Break': '5',
            'Long Break': '15'
        }
        self.radio_group.setDisabled(False)
        self.stack_btn.setCurrentWidget(self.start_btn)
        self.timer_is_run = False
        time.sleep(1)

        for item in self.radio_group.children()[1::]:
            if item.isChecked():
                self.count_minute.setText(times[item.text()])
                self.count_second.setText('00')



    '''
    The function interrupts the timer and saves the last time value on the label
    '''
    def pause(self):
        self.radio_group.setDisabled(False)
        self.timer_is_run = False
        self.stack_btn.setCurrentWidget(self.start_btn)



    def user_video(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '',
                        'MP4 Files (*.mp4);; MOV Files (*.mov)', options=options)
        if fileName:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.mediaPlayer.play()


    '''
    Exit from app
    '''
    def closeEvent(self, event):
        event.accept()
        sys.exit()
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    videoplayer = VideoPlayer()

    style = ''
    with open('style.css', 'r') as file:
        for line in file:
            style += line

    videoplayer.setStyleSheet(style)
    videoplayer.showMaximized()
    videoplayer.show()

    sys.exit(app.exec_())
