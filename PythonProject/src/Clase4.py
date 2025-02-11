import sys

from PySide6.QtGui import QAction, QKeySequence, Qt, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QMenu, \
    QMenuBar, QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ##CONFIGURO LA VENTANA PRINCIPAL

        self.setWindowTitle("Ejercicio con Pyside6")
        self.setGeometry(100, 100, 600, 400)

        ##PRIMERO ELIJO EL CONTENEDOR PRINCIPAL Y LUEGO EL LAYOUT PRINCIPAL

        central_widget = QWidget()                                                                              ##Contenedor Principal
        self.setCentralWidget(central_widget)                                                                   ##Seleccionamos el contenedor principal como "Contenedor principal
        layout = QVBoxLayout()                                                                                  ##Creamos un vertical Layout
        central_widget.setLayout(layout)                                                                        ##Le decimos al central widget su tipo de layout

        ##BOTON PRINCIPAL
        self.button=QPushButton("Presioname")                                                                   ##Creamos un boton "Presionar"
        self.button.clicked.connect(self.show_message)                                                          ##Cuando lo presionemos, llamara a la funcion "show_message" para mostrar un mensaje
        layout.addWidget(self.button)                                                                           ##Añadimos el boton al layout

        ##CREAMOS EL MENU PRINCIPAL
        menu_bar=QMenuBar()                                                                                     ##Creamos un menu principal
        self.setMenuBar(menu_bar)                                                                               ##Seleccionamos el tipo del menuBar con el menu creada antes

        ##CREAR LAS OPCIONES DEL MENU
        file_menu=QMenu("Archivo",self)                                                                         ##Creamos la opcion "Archivo"
        menu_bar.addMenu(file_menu)                                                                             ##Añadimos esta opcion al menu

        new_action=QAction("Nuevo",self)                                                                        ##Creamos la opcion "Nuevo" para el desplegable de archivo
        new_action.triggered.connect(lambda: self.show_info("Nuevo seleccionado"))                              ##Cuando se pulse el boton, disparará la funcion lambda que muestra el mensaje
        new_action.setShortcut(QKeySequence("Ctrl+N"))                                                          ##Añadimos un atajo de teclado
        file_menu.addAction(new_action)                                                                         ##Por ultimo, añadimos la opcion "Nuevo" al desplegable del menu
        open_action = QAction("Abrir", self)
        open_action.triggered.connect(lambda: self.show_info("Archivo seleccionado"))
        open_action.setShortcut(QKeySequence("Ctrl+O"))
        file_menu.addAction(open_action)                                                                        ##Hacemos lo mismo con las opciones Abrir y Guardar...
        save_action = QAction("Guardar", self)
        save_action.triggered.connect(lambda: self.show_info("Guardar seleccionado"))
        save_action.setShortcut(QKeySequence("Ctrl+S"))
        file_menu.addAction(save_action)

        self.setContextMenuPolicy(Qt.CustomContextMenu)                                                         ##Damos forma al tipo de menu que aparecera con el click derecho
        self.customContextMenuRequested.connect(self.show_context_menu)                                         ##Llamamos a la funcion que mostrará el contenido de ese menu del click derecho

        tool_bar=QToolBar("Barra de Herramientas")                                                              ##Creamos ya la barra de herramientas
        self.addToolBar(tool_bar)                                                                               ##La añadimos

        tool_bar_action=QAction(QIcon.fromTheme("help-browser"),"Mostrar mensaje",self)                         ## Creamos un icono "Help" con un texto
        tool_bar_action.setShortcut(QKeySequence("Ctrl+M"))                                                     ## Le damos un atajo de teclado
        tool_bar_action.triggered.connect(lambda: self.show_info("Mensaje desde la barra de herramientas"))     ## Disparador que, al clicar en el icono, mostrara este mensaje
        tool_bar.addAction(tool_bar_action)                                                                     ##Anadimos todo lo anterior a la barra de herramientas



    def show_message(self):                                                                                     ##Metodo para mostrar un mensaje de "Boton presionado"
        QMessageBox.information(self, "Mesasge", "Boton presionado")

    def show_info(self,message):                                                                                ##Metodo "molde" para mostrar mensajes a traves de un mensaje "Parametro"
        QMessageBox.information(self, "Mensaje", message)

    def show_context_menu(self,position):                                                                       ## Metodo para crear el menu click derecho
        context_menu=QMenu(self)                                                                                ##Creamos el widget del menu y guardamos en variable

        context_action=QAction("Accion conceptual",self)                                                        ##Contenido u opcion que aparecera en el menu
        context_action.setShortcut(QKeySequence("Ctrl+X"))                                                      ##Atajo de teclado
        context_action.triggered.connect(lambda: self.show_info("Accion conceptual abierta"))                   ##Cuando pulsemos, mostrara este mensaje a traves de una funcion lambda

        context_menu.addAction(context_action)                                                                  ##Aniadimos todo lo anterior al menu
        context_menu.exec(self.mapToGlobal(position))                                                           ##definimos la posicion de donde va a aparecer dicho menu


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())