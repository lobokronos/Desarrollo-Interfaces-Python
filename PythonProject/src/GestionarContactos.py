
                                        ##USO AVANZADO DE COMPONENTES Y DIALOGOS, EJERCICIO 1

import sqlite3
import sys

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QPushButton, QTableWidget, QListWidget, \
    QLineEdit, QMessageBox, QTableWidgetItem


def base_datos():
    conexion = sqlite3.connect("contactos.db")
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL)
    ''')
    conexion.commit()
    conexion.close()


class GestionarContactos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestionar Contactos")
        self.setGeometry(500, 500, 500, 350)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout=QVBoxLayout()
        self.setLayout(layout)
        central_widget.setLayout(layout)

        self.tabla=QTableWidget()
        self.tabla.setColumnCount(1)
        self.tabla.setHorizontalHeaderLabels(['Nombre'])
        layout.addWidget(self.tabla)

        self.texto=QLineEdit()
        self.texto.setPlaceholderText("Nombre de usuario")
        layout.addWidget(self.texto)


        self.btn_anadir = QPushButton("Anadir contacto")
        self.btn_anadir.clicked.connect(self.anadir_contacto)
        layout.addWidget(self.btn_anadir)

        self.btn_ver= QPushButton("Ver contacto")
        self.btn_ver.clicked.connect(self.listar_nombres)
        layout.addWidget(self.btn_ver)

        self.btn_eliminar=QPushButton("Eliminar contacto")
        self.btn_eliminar.clicked.connect(self.eliminar_contacto)
        layout.addWidget(self.btn_eliminar)


    def anadir_contacto(self):
        nombre=self.texto.text()
        if not nombre:
            QMessageBox.warning(self, "Error", "Escribe un nombre")
        else:
            conexion=sqlite3.connect("contactos.db")
            cursor=conexion.cursor()
            cursor.execute("INSERT INTO usuario (nombre) VALUES (?)", (nombre,))
            conexion.commit()
            conexion.close()


    def eliminar_contacto(self):
        nombre=self.texto.text()
        if not nombre:
            QMessageBox.warning(self, "Error", "Escribe un nombre")

        else:
            conexion=sqlite3.connect("contactos.db")
            cursor=conexion.cursor()
            cursor.execute("DELETE FROM usuario WHERE nombre = ?",(nombre,))
            usuarios=cursor.fetchall()
            conexion.commit()
            conexion.close()





    def listar_nombres(self):
        conexion=sqlite3.connect("contactos.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT nombre FROM usuario")
        usuarios=cursor.fetchall()
        conexion.close()

        self.tabla.setRowCount(len(usuarios))
        for row, (nombre,) in enumerate(usuarios):
            self.tabla.setItem(row, 0, QTableWidgetItem(nombre))



if __name__ == '__main__':
    base_datos()
    app = QApplication(sys.argv)
    window = GestionarContactos()
    window.show()
    sys.exit(app.exec())




