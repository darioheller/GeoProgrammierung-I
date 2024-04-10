import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


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
        self.landLineEdit.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.button1 = QPushButton("Auf Karte zeigen")
        self.button2 = QPushButton("Laden")
        self.button3 = QPushButton("Speichern")

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstagLineEdit)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.landLineEdit)
        layout.addRow(self.button1)
        layout.addRow(self.button2)
        layout.addRow(self.button3)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenstergröße festlegen
        self.resize(600, 400)

        # Fenster anzeigen
        self.show()
        
    def createConnects(self):
        self.button1.clicked.connect(self.menu_map)
        self.button2.clicked.connect(self.menu_open)
        self.button3.clicked.connect(self.menu_save)

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

    # Menu Map definieren
    def menu_map(self):
        strasse = self.adresseLineEdit.text().replace(" ", "+")
        plz = self.plzLineEdit.text()
        ort = self.ortLineEdit.text()
        land = self.landLineEdit.currentText()

        map_url = f"https://www.google.ch/maps/place/{strasse}+{plz}+{ort}+{land}"

#Mit damit funktioniert es nicht........
        #import urllib.parse
        #link = urllib.parse.quote(map_url)

        QDesktopServices.openUrl(QUrl(map_url))
    
    # Menu Open definieren
    def menu_open(self):
        filenameOpen, typ = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Textfile (*.txt)")
        with open(filenameOpen, "r") as file:
            daten = file.readline().strip().split(',')

            self.vornameLineEdit.setText(daten[0])
            self.nameLineEdit.setText(daten[1])
            self.geburtstagLineEdit.setDate(QDate.fromString(daten[2], Qt.ISODate))
            self.adresseLineEdit.setText(daten[3])
            self.plzLineEdit.setText(daten[4])
            self.ortLineEdit.setText(daten[5])
            self.landLineEdit.setCurrentText(daten[6])

    # Menu Save definieren
    def menu_save(self):
        filenameSave, typ = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Textfile (*.txt)")
        vorname = self.vornameLineEdit.text()
        name = self.nameLineEdit.text()
        geburtstag = self.geburtstagLineEdit.date().toString(Qt.ISODate)
        adresse = self.adresseLineEdit.text()
        plz = self.plzLineEdit.text()
        ort = self.ortLineEdit.text()
        land = self.landLineEdit.currentText()

        # Daten in eine Textdatei schreiben
        with open(filenameSave, "w") as file:
            file.write(f"{vorname},{name},{geburtstag},{adresse},{plz},{ort},{land}\n")

        print(f"Daten wurden in {filenameSave} gespeichert.")

    # Menu Quit definieren
    def menu_quit(self):
        print("Menu Quit wurde gewählt...")
        self.close()  # Hauptfenster schliessen = beenden!

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()