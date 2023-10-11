# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_dashboard = QWidget()
        self.tab_dashboard.setObjectName(u"tab_dashboard")
        self.tabWidget.addTab(self.tab_dashboard, "")
        self.tab_squawks = QWidget()
        self.tab_squawks.setObjectName(u"tab_squawks")
        self.tabWidget.addTab(self.tab_squawks, "")
        self.tab_airframe = QWidget()
        self.tab_airframe.setObjectName(u"tab_airframe")
        self.tabWidget.addTab(self.tab_airframe, "")
        self.tab_engine = QWidget()
        self.tab_engine.setObjectName(u"tab_engine")
        self.tabWidget.addTab(self.tab_engine, "")
        self.tab_propeller = QWidget()
        self.tab_propeller.setObjectName(u"tab_propeller")
        self.tabWidget.addTab(self.tab_propeller, "")
        self.tab_avionics = QWidget()
        self.tab_avionics.setObjectName(u"tab_avionics")
        self.tabWidget.addTab(self.tab_avionics, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dashboard), QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_squawks), QCoreApplication.translate("MainWindow", u"Squawks", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_airframe), QCoreApplication.translate("MainWindow", u"Airframe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_engine), QCoreApplication.translate("MainWindow", u"Engine", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_propeller), QCoreApplication.translate("MainWindow", u"Propeller", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_avionics), QCoreApplication.translate("MainWindow", u"Avionics", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

