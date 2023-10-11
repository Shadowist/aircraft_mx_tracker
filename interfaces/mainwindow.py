# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from .ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tabWidget.currentChanged.connect(self.setup_tab)

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, filepath: str):
        self._filepath = filepath

        # TODO: This should be platform agnostic
        self.setWindowTitle(filepath.split("/")[-1])

    # === Tab Setup ===
    def setup_tab(self, index: int):
        name: str = self.ui.tabWidget.tabText(index).lower()

        if name == "ad/sb":
            name = "adsb"

        try:
            getattr(self, f"setup_{name}")()
        except AttributeError:
            print(f"{name} is not currently set up!")

    def setup_airframe(self):
        pass

    def setup_engine(self):
        pass

    def setup_avionics(self):
        pass

    def setup_propeller(self):
        pass

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
