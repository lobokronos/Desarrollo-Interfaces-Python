##USO AVANZADO DE COMPONENTES Y DIALOGOS, EJERCICIO 2
import sqlite3
import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QMenuBar, QWidget, QVBoxLayout, QApplication, QMenu, QListWidget, \
    QMessageBox, QTextEdit, QPushButton, QDialog, QLineEdit, QTableWidgetItem


def base_datos():
    conexion=sqlite3.connect("tareas.db")
    cursor=conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarea TEXT  UNIQUE )
        ''')
    conexion.commit()
    conexion.close()

class ProgramaTareas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Programa Tareas")
        self.setGeometry(300, 300, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        self.setLayout(layout)
        central_widget.setLayout(layout)


        self.lista_tareas=QListWidget()
        layout.addWidget(self.lista_tareas)

        menubar = QMenuBar()
        self.setMenuBar(menubar)

        file_menu = QMenu("Tareas", self)
        menubar.addMenu(file_menu)

        anadir_action=QAction("Anadir tarea",self)
        anadir_action.triggered.connect(self.anadir_tarea)
        file_menu.addAction(anadir_action)
        eliminar_action = QAction("Eliminar tarea", self)
        file_menu.addAction(eliminar_action)
        editar_action = QAction("Editar tarea", self)
        file_menu.addAction(editar_action)

        self.cargar_tareas()


    def cargar_tareas(self):
        conexion=sqlite3.connect("tareas.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT tarea FROM tareas")
        tareas=cursor.fetchall()
        conexion.close()

        self.lista_tareas.clear()
        for tarea in tareas:
            self.lista_tareas.addItem(tarea[0])

    def anadir_tarea(self):
            dialogo = QDialog(self)
            dialogo.setWindowTitle("Añadir tarea")
            dialogo.setFixedSize(200, 150)

            layout = QVBoxLayout(dialogo)

            texto_tarea = QLineEdit()
            texto_tarea.setPlaceholderText("Escribe la tarea...")
            layout.addWidget(texto_tarea)

            btn_agregar = QPushButton("Agregar")
            layout.addWidget(btn_agregar)


            def guardar(self):
                nueva_tarea=texto_tarea.text()
                conexion=sqlite3.connect("tareas.db")
                cursor=conexion.cursor()
                cursor.execute("INSERT INTO tareas (tarea) VALUES (?)", (nueva_tarea,))

                conexion.commit()
                conexion.close()


            btn_agregar.clicked.connect(guardar)
            dialogo.setLayout(layout)
            dialogo.exec()





if __name__ == '__main__':
    base_datos()
    app = QApplication(sys.argv)
    window = ProgramaTareas()
    window.show()
    sys.exit(app.exec())