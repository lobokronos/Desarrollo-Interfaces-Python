import sqlite3
import sys
from base64 import b64encode
from multiprocessing.reduction import register

import bcrypt
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, \
    QMessageBox, QTableWidget, QTableWidgetItem, QAbstractItemView, QCheckBox


def crear_base_datos():

    conexion= sqlite3.connect('usuarios.db')                                        ##Apunta a la base de datos (usuarios.db). Si no existe, la crea nueva.
    cursor = conexion.cursor()                                                      ##Objeto que nos va a permitir la interaccion entre nuestra BBDD y el programa.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        contrasea TEXT NOT NULL,
        es_admin INTEGER NOT NULL DEFAULT 0)
    ''')

    conexion.commit()                                                               ##Guarda los cambios realizados en la base de datos.
    conexion.close()                                                                ##Cierra la conexion.

class LoginForm(QMainWindow):                                                       ##Clase para la ventana de LOGIN.
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesion")                                     ##Titulo de la ventana.
        self.setGeometry(100,100,200,200)                                           ##Dimensiones.

        main_layout = QVBoxLayout()                                                 ##Tipo de Layout (Vertical).
        title= QLabel("Inicio de Sesion")                                           ##Titulo del recuadro del campo para usuario.
        main_layout.addWidget(title)                                                ##Añade TITULO al Layout principal.

        ##ENTRADA DE TEXTO PARA EL USUARIO
        self.username_input=QLineEdit()                                             ##Campo de entrada para el nombre de usuario.
        self.username_input.setPlaceholderText("Nombre de usuario")                 ##Texto en gris que aparece cuando no hay escrito nada.
        main_layout.addWidget(self.username_input)                                  ##Añade el layout al main

        ##ENTRADA DEL TEXTO PARA LA CONTRASEÑA
        self.password_input=QLineEdit()                                              ##Campo de entrada para la contraseña
        self.password_input.setPlaceholderText("Introduce la contraseña")            ##Texto en gris
        self.password_input.setEchoMode(QLineEdit.Password)
        main_layout.addWidget(self.password_input)

        ##BOTON PARA INICIO DE SESION
        login_button=QPushButton("Inicio de Sesion")                                ##Creamos un boton para iniciar sesion y lo guardamos en una variable
        login_button.clicked.connect(self.iniciar_sesion)                           ##Al pinchar el boton, llamara a la funcion "iniciar_sesion"
        main_layout.addWidget(login_button)

        ##BOTON PARA PASAR A LA VENTANA DE REGISTRO
        register_button=QPushButton("Registrar")                                    ##Creamos un boton para registrar
        register_button.clicked.connect(self.volver_a_registro)                     ##Al pulsar el boton, llamamos a la funcion "volver_al_registro"
        main_layout.addWidget(register_button)                                      ##Añadimos el boton al layout principal


        ##ESTABLECER EL LAYOUT PRINCIPAL
        central_widget=QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def volver_a_registro(self):                                                        ##Metodo para volver a la pantalla de LOGIN
            self.login = RegisterForm()                                                 ##Creamos una variable donde guardamos la posicion de la ventana LOGIN
            self.login.show()                                                           ##Le decimos que muestre dicha ventana
            self.close()

    def iniciar_sesion(self):                                                           ##metodo para iniciar sesion
        usuario=self.username_input.text()                                              ##recogemos el texo en campos de texto
        contrasea=self.password_input.text()

        if not usuario or not contrasea:                                                ##Si usuario o contraseña estan vacios saltara un error
            QMessageBox.warning(self,"Error","Todos los campos son obligatorios")

        conexion= sqlite3.connect('usuarios.db')                                        ##Conectamos con BBDD
        cursor=conexion.cursor()                                                        ##Creamos cursor
        cursor.execute("SELECT contrasea FROM usuarios WHERE usuario=?",(usuario,))##Seleccionamos su contraseña en la tabla
        resultado=cursor.fetchone()                                                     ##Cogemos solo el primer resultado (solo hay 1)
        conexion.close()

        if resultado and bcrypt.checkpw(contrasea.encode(),resultado[0]):               
            self.bienvenida=WelcomeForm(usuario)
            self.bienvenida.show()
            self.close()

        else:
            QMessageBox.critical(self,"Error","Usuario o contraseña incorrectos")
            self.username_input.clear()
            self.password_input.clear()



class RegisterForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro")
        self.setGeometry(100, 100, 400, 400)                                                ##Dimensiones.

        main_layout = QVBoxLayout()                                                         ##Tipo de Layout (Vertical).
        title = QLabel("Registro")                                                          ##Titulo del recuadro del campo para usuario.
        main_layout.addWidget(title)                                                        ##Añade TITULO al Layout principal.

        ##ENTRADA DE TEXTO PARA EL USUARIO
        self.username_input = QLineEdit()                                                   ##Campo de entrada para el nombre de usuario.
        self.username_input.setPlaceholderText("Nombre de usuario")                         ##Texto en gris que aparece cuando no hay escrito nada.
        main_layout.addWidget(self.username_input)                                          ##Añade el layout al main

        ##ENTRADA DEL TEXTO PARA LA CONTRASEÑA
        self.password_input = QLineEdit()                                                   ##Campo de entrada para la contraseña
        self.password_input.setPlaceholderText("Introduce la contraseña")                   ##Texto en gris
        self.password_input.setEchoMode(QLineEdit.Password)                                 ##Propiedad que hace que aparezcan puntitos para ocultar la contraseña al escribirla
        main_layout.addWidget(self.password_input)                                          ##Añade este widget al layout principal de la ventana

        ##CHECKBOX PARA MARCAR SI ES AADMINISTRADOR

        self.admin_checkbox = QCheckBox("¿Es administrador?")                               ##Creamos un checkbox con un texto
        main_layout.addWidget(self.admin_checkbox)                                          ##Añadimos el checkbox al layout principal

        ##BOTON PARA Registro de Usuario
        register_button = QPushButton("Registrar")                                          ##Creamos un boton "Registrar" y lo guardamos en una variable
        register_button.clicked.connect(self.registrar_usuario)                             ##Cuando pulsemos ese boton, se disparara la funcion "registrar_usuario"
        main_layout.addWidget(register_button)                                              ##Añade este boton al layout principal de la ventana

        ##BOTON PARA PASAR A LA VENTANA DE REGISTRO
        back_button = QPushButton("Volver a Inicio de Sesion")                              ##Creamos el boton "volver al inicio de sesion y lo guardamos en una variable
        back_button.clicked.connect(self.volver_a_login)                                    ##Cuando pulsemos ese boton, se disparara la funcion "volver_a_login"
        main_layout.addWidget(back_button)                                                  ##Añade este boton al layout principal de la ventana


        ##ESTABLECER EL LAYOUT PRINCIPAL
        central_widget = QWidget()                                                          ##Establece el tipo layout principal de dicha ventana
        central_widget.setLayout(main_layout)                                               ##Indicamos que este layout va a ser el principal
        self.setCentralWidget(central_widget)                                               ##Indicamos que este widget va a ser el principal de esta ventana


    def volver_a_login(self):                                                               ##Metodo para volver a la pantalla de LOGIN
        self.login=LoginForm()                                                              ##Creamos una variable donde guardamos la posicion de la ventana LOGIN
        self.login.show()                                                                   ##Le decimos que muestre dicha ventana
        self.close()                                                                        ##Cerramos la ventana actual


    def registrar_usuario(self):                                                            ##funcion para registrar usuarios
        usuario= self.username_input.text()                                                 ##Guardamos los textos recogidos en los campos de usuario y ctsña y los guardamos en variables
        contrasea= self.password_input.text()
        es_admin=1 if self.admin_checkbox.isChecked() else 0

        if not usuario or not contrasea:                                                    ##Si no hay usuario o contraseña...
            QMessageBox.warning(self,"Error","Todos los campos son obligatorios")

        else:
            ##Encriptar la contraseña
            contrasea_encriptada=bcrypt.hashpw(contrasea.encode(),bcrypt.gensalt())         ##Codigo para encriptar la contraseña
            try:
                conexion=sqlite3.connect("usuarios.db")                                     ##conexion a BBDD
                cursor=conexion.cursor()                                                    ##creamos cursor
                cursor.execute("INSERT INTO usuarios (usuario, contrasea,es_admin) VALUES(?,?,?)",(usuario,contrasea_encriptada,es_admin))##Insertamos los datos nuevos en la tabla
                conexion.commit()                                                           ##guardamos
                conexion.close()                                                            ##cerramos
                QMessageBox.information(self,"Exito","Usuario registrado correctamente")
                self.volver_a_login()                                                       ##volvemos a la pantalla de LOGIN

            except sqlite3.IntegrityError:
                QMessageBox.critical(self,"Error","Usuario ya existente")          ##Texto de advertencia para cuando un usuario ya existe



class WelcomeForm(QMainWindow):
    def __init__(self,usuario):                                                             ##Metdo constructor de la clase Welcome
        super().__init__()                                                                  ##Herencias del constructor
        self.setWindowTitle("Bienvenido")                                                   ##Titulo de la ventana
        self.setGeometry(100, 100, 600, 400)                                                ##Dimensiones de la ventana

        self.usuario=usuario                                                                ##Guardamos el dato usuario como el propio usuario de la clase para facilitar las cosas


        ##LAYOUT PRINCIPAL
        main_layout = QVBoxLayout()                                                         ## El layout principal (Tipo QBoxLayout)


        ## ETIQUETA PRINCIPAL
        self.welcome_label=QLabel(f"¡Bienvenido,{self.usuario}!")                           ##Texto que aparece nada mas entrar en la ventana que recoge el nombre de usuario introducido en el inicio de sesion
        main_layout.addWidget(self.welcome_label)                                           ##Añade el label de la etiqueta (texto) al layout principal de esta ventana


        ## PINTAR LA TABLA

        self.table=QTableWidget()                                                           ##Elemento de una tabla guardado en una variable
        self.table.setColumnCount(2)                                                        ##Establecemos dos numeros de columnas (usuario y contraseña)
        self.table.setHorizontalHeaderLabels(["Usuario","Contraseña encriptada"])           ##Establece el titulo de las columnas por orden de colocacion
        main_layout.addWidget(self.table)                                                   ##Añade al layout la tabla
        self.cargar_usuario()                                                               ##Llama al metodo que carga los datos en la tabla


        ## BOTON PARA BORRAR CUENTA
        delete_button=QPushButton("Borrar cuenta")                                          ##Boton para borrar cuenta
        delete_button.clicked.connect(self.borrar_cuenta)                                   ##Al pulsar el boton, llama a la funcion " borrar_cuenta"
        main_layout.addWidget(delete_button)                                                ##Añade el boton al layout principal


        ## ESTABLECER EL LAYOUT CENTRAL COMO PRINCIPAL

        central_widget =QWidget()                                                           ##Crea el widget central
        central_widget.setLayout(main_layout)                                               ##Añade el centralWidget al layout principal
        self.setCentralWidget(central_widget)                                               ##Establece y llama al propio centralWidget

    def cargar_usuario(self):                                                               ##Metodo para cargar los datos en la tabla
        conexion = sqlite3.connect("usuarios.db")                                           ##Conectamos con la BBDD
        cursor = conexion.cursor()                                                          ##Creamos un cursor
        cursor.execute("SELECT usuario, contrasea FROM usuarios")                           ##Seleccionamos usuario y contraseña de la tabla
        usuarios = cursor.fetchall()                                                        ##Recogemos todos los datos obtenidos de la consulta
        conexion.close()                                                                    ##Cerramos conexion
        self.table.setRowCount(len(usuarios))                                               ##Cuenta el numero de filas (longitud de usuario)

        for row, (usuario, contrasea) in enumerate(usuarios):                               ##Este bucle establece los contenidos de la tabla
            self.table.setItem(row, 0, QTableWidgetItem(usuario))                    ##Establece como item (pinta en la tabla) en la columna 0 el item de usuario
            contrasea_legible = b64encode(contrasea).decode("utf-8")                        ##Descodifica la contraseña a utf-8 y la guarda en una variable
            self.table.setItem(row, 1, QTableWidgetItem(contrasea_legible))          ##Pinta el la columna 1 (contrasea) el item resultante de su fila (contrasea_legible)


    def borrar_cuenta(self):                                                                ##Funcion para borrar una cuenta
        select_row=self.table.currentRow()                                                  ##Guardamos la fila seleccionada en una variable
        if select_row == -1:                                                                ##Si la fila seleccionada no existe...
            QMessageBox.critical(self,"Error","Selecciona una cuenta para borrarla")##Texto de advertencia
        else:
            usuario=self.table.item(select_row,0).text()                             ##Guardamos el item de la fila actual, de la primera columna
            respuesta=QMessageBox.question(                                                 ##Guardamos las opciones SI y NO de borrar usuario...
                self,
                "Confirmacion",
                f"Estas seguro de borrar la cuenta de '{usuario}' ?",
            QMessageBox.Yes | QMessageBox.No,
            )

            if respuesta == QMessageBox.Yes:                                                ##Si la respuesta es si...
                conexion=sqlite3.connect("usuarios.db")
                cursor=conexion.cursor()
                cursor.execute("DELETE FROM usuarios WHERE usuario=?",(usuario,))##Consulta para borrar de la tabla el usuario correspondiente
                conexion.commit()
                conexion.close()
                QMessageBox.information(self,"Exito","Usuario borrado correctamente")
                self.cargar_usuario()                                                       ##Llamamos al metodo cargar_usuarios para que vuelva a cargar la tabla nuevamente


if __name__ == "__main__":
    crear_base_datos()
    app =QApplication(sys.argv)
    ventana= LoginForm()
    ventana.show()
    sys.exit(app.exec_())