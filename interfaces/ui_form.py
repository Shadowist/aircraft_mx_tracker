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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.verticalLayout_2 = QVBoxLayout(self.tab_squawks)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget.addTab(self.tab_squawks, "")
        self.tab_airframe = QWidget()
        self.tab_airframe.setObjectName(u"tab_airframe")
        self.verticalLayout_3 = QVBoxLayout(self.tab_airframe)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.table_airframe = QTableWidget(self.tab_airframe)
        if (self.table_airframe.columnCount() < 4):
            self.table_airframe.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_airframe.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_airframe.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_airframe.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_airframe.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_airframe.setObjectName(u"table_airframe")

        self.verticalLayout_3.addWidget(self.table_airframe)

        self.tabWidget.addTab(self.tab_airframe, "")
        self.tab_engine = QWidget()
        self.tab_engine.setObjectName(u"tab_engine")
        self.verticalLayout_5 = QVBoxLayout(self.tab_engine)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.table_engine = QTableWidget(self.tab_engine)
        if (self.table_engine.columnCount() < 4):
            self.table_engine.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_engine.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_engine.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_engine.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_engine.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.table_engine.setObjectName(u"table_engine")

        self.verticalLayout_5.addWidget(self.table_engine)

        self.tabWidget.addTab(self.tab_engine, "")
        self.tab_propeller = QWidget()
        self.tab_propeller.setObjectName(u"tab_propeller")
        self.verticalLayout_6 = QVBoxLayout(self.tab_propeller)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.table_propeller = QTableWidget(self.tab_propeller)
        if (self.table_propeller.columnCount() < 4):
            self.table_propeller.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_propeller.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_propeller.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_propeller.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_propeller.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.table_propeller.setObjectName(u"table_propeller")

        self.verticalLayout_6.addWidget(self.table_propeller)

        self.tabWidget.addTab(self.tab_propeller, "")
        self.tab_avionics = QWidget()
        self.tab_avionics.setObjectName(u"tab_avionics")
        self.verticalLayout_4 = QVBoxLayout(self.tab_avionics)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.table_avionics = QTableWidget(self.tab_avionics)
        if (self.table_avionics.columnCount() < 4):
            self.table_avionics.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_avionics.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_avionics.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_avionics.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_avionics.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        self.table_avionics.setObjectName(u"table_avionics")

        self.verticalLayout_4.addWidget(self.table_avionics)

        self.tabWidget.addTab(self.tab_avionics, "")
        self.tab_adsb = QWidget()
        self.tab_adsb.setObjectName(u"tab_adsb")
        self.verticalLayout_7 = QVBoxLayout(self.tab_adsb)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.table_adsb = QTableWidget(self.tab_adsb)
        if (self.table_adsb.columnCount() < 4):
            self.table_adsb.setColumnCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_adsb.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_adsb.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_adsb.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_adsb.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        self.table_adsb.setObjectName(u"table_adsb")

        self.verticalLayout_7.addWidget(self.table_adsb)

        self.tabWidget.addTab(self.tab_adsb, "")
        self.tab_intervals = QWidget()
        self.tab_intervals.setObjectName(u"tab_intervals")
        self.tabWidget.addTab(self.tab_intervals, "")

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

        self.tabWidget.setCurrentIndex(4)


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
        ___qtablewidgetitem = self.table_airframe.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.table_airframe.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TTAF", None));
        ___qtablewidgetitem2 = self.table_airframe.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tach", None));
        ___qtablewidgetitem3 = self.table_airframe.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_airframe), QCoreApplication.translate("MainWindow", u"Airframe", None))
        ___qtablewidgetitem4 = self.table_engine.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem5 = self.table_engine.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"TTAF", None));
        ___qtablewidgetitem6 = self.table_engine.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tach", None));
        ___qtablewidgetitem7 = self.table_engine.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_engine), QCoreApplication.translate("MainWindow", u"Engine", None))
        ___qtablewidgetitem8 = self.table_propeller.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem9 = self.table_propeller.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TTAF", None));
        ___qtablewidgetitem10 = self.table_propeller.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Tach", None));
        ___qtablewidgetitem11 = self.table_propeller.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_propeller), QCoreApplication.translate("MainWindow", u"Propeller", None))
        ___qtablewidgetitem12 = self.table_avionics.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem13 = self.table_avionics.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"TTAF", None));
        ___qtablewidgetitem14 = self.table_avionics.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Tach", None));
        ___qtablewidgetitem15 = self.table_avionics.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_avionics), QCoreApplication.translate("MainWindow", u"Avionics", None))
        ___qtablewidgetitem16 = self.table_adsb.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Logbook", None));
        ___qtablewidgetitem17 = self.table_adsb.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem18 = self.table_adsb.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Event", None));
        ___qtablewidgetitem19 = self.table_adsb.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_adsb), QCoreApplication.translate("MainWindow", u"AD/SB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_intervals), QCoreApplication.translate("MainWindow", u"Intervals", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

