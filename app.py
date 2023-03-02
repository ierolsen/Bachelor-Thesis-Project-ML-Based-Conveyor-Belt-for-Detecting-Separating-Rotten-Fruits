import sys
import os
from PySide2 import *

from gui import resources
from gui.main_gui import *
from Custom_Widgets.Widgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # APPLY JSON STYLESHEET
        loadJsonStyle(self, self.ui)
        
        self.show()

# EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
