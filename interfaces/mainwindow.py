# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import QDate


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

    def _setup_mx_data(self, logbook: str):
        cur: sqlite3.Cursor = mx_utils.get_logs(self._conn, logbook)
        res: list[tuple] = cur.fetchall()

        getattr(self.ui, f"table_{logbook.lower()}").setRowCount(len(res))
        for row, entry in enumerate(res):
            for column, value in enumerate(entry):
                item: QTableWidgetItem = QTableWidgetItem(str(value))
                getattr(self.ui, f"table_{logbook.lower()}").setItem(row, column, item)
        getattr(self.ui, f"table_{logbook.lower()}").resizeColumnsToContents()

    def setup_airframe(self):
        self._setup_mx_data("Airframe")

        self.ui.table_airframe.itemClicked.connect(self.connect_airframe_form)

    def connect_airframe_form(self, item: QTableWidgetItem):
        row = self.ui.table_airframe.row(item)

        date_val: list[str] = self.ui.table_airframe.item(row, 0).text().split('-')
        date: QDate = QDate(int(date_val[0]), int(date_val[1]), int(date_val[2]))

        self.ui.airframe_date.setDate(date)
        self.ui.airframe_ttaf.setValue(float(self.ui.table_airframe.item(row, 1).text()))
        self.ui.airframe_tach.setValue(float(self.ui.table_airframe.item(row, 2).text()))
        self.ui.airframe_description.setText(self.ui.table_airframe.item(row, 3).text())

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
