# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from .ui_form import Ui_MainWindow

from source import mx_utils
import sqlite3
from source import sql_utils


class MainWindow(QMainWindow):
    _conn: sqlite3.Connection
    _filepath: str

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Signals/Slots
        self.ui.tabWidget.currentChanged.connect(self.setup_tab)

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, filepath: str):
        self._filepath = filepath

        # Create Sqlite Connection
        self._conn = sql_utils.create_connection(self._filepath)

        # TODO: This should be platform agnostic
        self.setWindowTitle(self._filepath.split("/")[-1])

    # === Tab Setup ===
    def setup_tab(self, index: int):
        """ General tab entry point """
        name: str = self.ui.tabWidget.tabText(index).lower()

        if name == "ad/sb":
            name = "adsb"

        try:
            getattr(self, f"setup_{name}")()
        except AttributeError:
            print(f"{name} is not currently set up!")

    # TODO: Lots of copy pasta, need to refactor
    def setup_airframe(self):
        cur: sqlite3.Cursor = mx_utils.get_logs(self._conn, "Airframe")
        res: list[tuple] = cur.fetchall()

        self.ui.table_airframe.setRowCount(len(res))
        for row, entry in enumerate(res):
            for column, value in enumerate(entry):
                item: QTableWidgetItem = QTableWidgetItem(str(value))
                self.ui.table_airframe.setItem(row, column, item)
        self.ui.table_airframe.resizeColumnsToContents()

    def setup_engine(self):
        cur: sqlite3.Cursor = mx_utils.get_logs(self._conn, "Engine")
        res: list[tuple] = cur.fetchall()

        self.ui.table_engine.setRowCount(len(res))
        for row, entry in enumerate(res):
            for column, value in enumerate(entry):
                item: QTableWidgetItem = QTableWidgetItem(str(value))
                self.ui.table_engine.setItem(row, column, item)
        self.ui.table_engine.resizeColumnsToContents()

    def setup_avionics(self):
        cur: sqlite3.Cursor = mx_utils.get_logs(self._conn, "Avionics")
        res: list[tuple] = cur.fetchall()

        self.ui.table_avionics.setRowCount(len(res))
        for row, entry in enumerate(res):
            for column, value in enumerate(entry):
                item: QTableWidgetItem = QTableWidgetItem(str(value))
                self.ui.table_avionics.setItem(row, column, item)
        self.ui.table_avionics.resizeColumnsToContents()

    def setup_propeller(self):
        cur: sqlite3.Cursor = mx_utils.get_logs(self._conn, "Propeller")
        res: list[tuple] = cur.fetchall()

        self.ui.table_propeller.setRowCount(len(res))
        for row, entry in enumerate(res):
            for column, value in enumerate(entry):
                item: QTableWidgetItem = QTableWidgetItem(str(value))
                self.ui.table_propeller.setItem(row, column, item)
        self.ui.table_propeller.resizeColumnsToContents()

    def setup_adsb(self):
        pass

    def setup_squawks(self):
        pass

    def setup_dashboard(self):
        pass

    def setup_intervals(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
