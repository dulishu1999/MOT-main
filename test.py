# import required modules

import sys, time
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon,QFont,QScreen
from PySide6 import QtCore
# Create our main window
class SampleWindow(QWidget):   # 创建一个窗口类，并让他继承Qwidget
    # 构造函数
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('Sample Window with Icon')
        self.setGeometry(300,300,200,150)

        # add tool tips
        # set tooltips first and then use in following code
        QToolTip.setFont(QFont('Decorative',8,QFont.Bold))
        self.setToolTip('Main Window')
        print('Sample window is showing ')

    # function to set icon
        appIcon = QIcon('source_data/hacking icon.png')
        self.setWindowIcon(appIcon)
        self.setIconModes()
        
    # add button here
        self.setButton()
        self.setAboutButton()
    # centerilized the window
        self.center()


    def setIconModes(self):
        myIcon1 = QIcon('source_data/hacking icon.png')
        myLabel1 = QLabel('sample',self)
        pixmap1 = myIcon1.pixmap(50,50,QIcon.Active,QIcon.On)
        myLabel1.setPixmap(pixmap1)
        myLabel1.setToolTip('Active Icon')
        myLabel1.show()

        myIcon2 = QIcon('source_data/hacking icon.png')
        myLabel2 = QLabel('sample', self)
        pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
        myLabel2.setPixmap(pixmap2)
        myLabel2.move(50,0)
        myLabel2.setToolTip('Disable Icon')
        myLabel2.show()

        myIcon3 = QIcon('source_data/hacking icon.png')
        myLabel3 = QLabel('sample', self)
        pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
        myLabel3.setPixmap(pixmap3)
        myLabel3.move(100, 0)
        myLabel3.setToolTip('Selected Icon')
        myLabel3.show()

    def setButton(self):
        '''
        add quit button
        '''
        myButton = QPushButton('Quit',self)
        myButton.move(50,100)
        myButton.clicked.connect(self.quitApp) # link to Quit App, this function will be create later

    def msgApp(self,title,msg):
        # Create a dialog with title and msg
        userInfo = QMessageBox.question(self,title,msg,QMessageBox.Yes , QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            return 'Y'
        if userInfo == QMessageBox.No:
            return "N"



    def quitApp(self):
        # decide quit app by using message dialog return value.
        response = self.msgApp('Confirmation','This will quit this app , do you want to continue?')    # self is default value, no need to pass value
        if response == 'Y':
            myApp.quit()
        else:
            pass



    def center(self):
        '''
        Function to show window in the center of screen
        '''
        qRect = self.frameGeometry() # frameGeometry will give us a QtCore.QRect object, it will hold height, width and other dimension of window
        centerPoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        # move window to centerPoint
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

        # 这一段看起来是先得到一个QRect，然后移动到屏幕中心位置。然后再把真正的窗口移动到 QRect的位置。


    def setAboutButton(self):
        '''
        this function is to setup a about button
        '''
        self.aboutButton = QPushButton('About',self)
        self.aboutButton.move(200,100)
        self.aboutButton.clicked.connect(self.showAbout)

    def showAbout(self):
        '''
        function to show About Window
        '''
        QMessageBox.about(self.aboutButton,'About PySide','PySide6')



if __name__ == '__main__':
    #Expception Handler
    try:
        myApp = QtWidgets.QApplication(sys.argv)
        myWindow = SampleWindow()
        myWindow.center()
        myWindow.show()

        #QtCore.QCoreApplication.processEvents()
        '''
        time.sleep(3)
        myWindow.resize(300,300)
        myWindow.setWindowTitle('My Window is resized')
        myWindow.repaint()
        
        '''

        sys.exit(myApp.exec())
    except NameError:
        print('Name Error:' , sys.exc_info()[1])
    except SystemExit:
        print('Closeing Window...')
    except Exception:
        print(sys.exc_info()[1])