import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()
        self.createMenuBar()

    def createLayout(self):
        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:

        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.geburtstagLineEdit = QDateEdit()
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.landLineEdit = QComboBox()
        self.button = QPushButton("Save")

        self.landLineEdit.addItems(["Schweiz", "Deutschland", "Österreich"])

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstagLineEdit)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.landLineEdit)
        layout.addRow(self.button)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()
        
    def createMenuBar(self):
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        quit.setMenuRole(QAction.QuitRole)   # Rolle "beenden" (für MacOS)

        filemenu.addAction(save)
        filemenu.addSeparator()
        filemenu.addAction(quit)

    # Menu Save definieren
    def menu_save(self):
        vorname = self.vornameLineEdit.text()
        name = self.nameLineEdit.text()
        geburtstag = self.geburtstagLineEdit.date().toString(Qt.ISODate)
        adresse = self.adresseLineEdit.text()
        plz = self.plzLineEdit.text()
        ort = self.ortLineEdit.text()
        land = self.landLineEdit.currentText()

        # Daten in eine Textdatei schreiben
        with open("output.txt", "w") as file:
            file.write(f"{vorname},{name},{geburtstag},{adresse},{plz},{ort},{land}\n")

        print("Daten wurden in output.txt gespeichert.")

    # Menu Quit definieren
    def menu_quit(self):
        print("Menu Quit wurde gewählt...")
        self.close()  # Hauptfenster schliessen = beenden!

    def createConnects(self):
        self.button.clicked.connect(self.menu_save)

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()