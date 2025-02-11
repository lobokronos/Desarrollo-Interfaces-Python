from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PySide6.QtCore import Qt


class ClaseMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")                      ##0. ESTE CODIGO GENERA EL NOMBRE DE LA VENTANA Y SUS DIMENSIONES
        self.setGeometry(100, 100, 300, 400)

                ##LAYOUT PRINCIPAL

        self.layout_principal=QVBoxLayout()                     ##1. QVBoxLayout hace referencia al Vertical_Layout en el PySide6 (Su nombre de clase)
        self.setLayout(self.layout_principal)

                ##PANTALLA PRINCIPAL

        self.pantalla=QLineEdit()                               ##2. Creamos la instancia de la pantalla
        self.pantalla.setAlignment(Qt.AlignmentFlag.AlignRight) ##2.1 Alineamos el texto del interior de la pantalla a la derecha
        self.pantalla.setReadOnly(True)                         ##3. Esto no permite al usuario escribir dentro de ella, solo muestra lectura
        self.pantalla.setStyleSheet("font-size: 24px")          ##4. Ajusta el tamaño del layout de la pantalla (el tamaño de fuente de la pantalla)
        self.layout_principal.addWidget(self.pantalla)          ##5. Añade este Layout al Layout Principal.

                ##GRID DE LOS BOTONES

        self.grid_layout = QGridLayout()                        ##6. Creamos la instancia de los botones
        self.layout_principal.addLayout(self.grid_layout)       ##7. Añade este Layout al Layout principal
        self.crear_botones()

                ##METODO PARA CREAR Y POSICIONAR LOS BOTONES

    def crear_botones(self):
        botones={
            '7': (0,0), '8': (0,1), '9': (0,2), '/': (0,3),
            '4': (1,0), '5': (1,1), '6': (1,2), '*': (1,3),    ##8. Este metodo contiene un array, el cual tiene todos los botones con su texto y posicion.
            '1': (2,0), '2': (2,1), '3': (2,2), '-': (2,3),
            '0': (3,0), 'C': (3,1), '=': (3,2), '+': (3,3),
        }
        for texto, posicion in botones.items():                ##9. Este bucle FOR recorre la posicion y el texto del array botones mediante botones.items()
            boton=QPushButton(texto)                           ##10. Variable boton el cual añadira el texto al boton
            boton.setStyleSheet("font-size: 18px")             ##-- Tamaño del texto de los botones
            boton.clicked.connect(self.manejar_click)
            self.grid_layout.addWidget(boton, *posicion)       ##11. Añadimos el widget indicando en parametros la variable boton (texto) y su posicion (*posicion)

    def manejar_click(self):                                   ##12. Creamos una funcion en la cual recogera las pulsaciones y le dala salida  de texto por pantalla
        boton=self.sender()                                    ##13. Inicializamos la variable boton para recoger el contenido del boton pulsado con .sender()
        texto=boton.text()                                     ##14. Inicializamos la variable texto, donde recogemos la variable anterior y la pasamos a text

        if texto=='C':                                         ##15. Si la tecla pulsada (o el texto que esta contiene...) es =C....
            self.pantalla.clear()                              ##16. ...Le decimos que se borre la pantalla
        elif texto=='=':                                       ##17. Si la tecla pulsada es '='...
                try:
                    resultado=eval(self.pantalla.text())       ##18. Le decimos que evalue la operacion de la pantalla (lo hace automaticamente) y lo guarde en resultado
                    self.pantalla.setText(str(resultado))      ##19. Imprimimos la variable 'resultado' como un string en la pantalla
                except:
                    self.pantalla.setText("ERROR")             ##20. Capturamos la excepcion por si hay errores en la app

        else:
            self.pantalla.setText(self.pantalla.text() + texto) ##21. Si no, le diremos a la pantalla que establezca en su texto lo que ya tiene de texto en ella (...
                                                                ##21.1 ...self.pantalla.text(), mas el texto del boton pulsado.




if __name__ == "__main__":                                      ##22. Creamos el metodo MAIN
    app=QApplication()                                          ##23. Generamos la aplicacion
    ventana=ClaseMain()                                         ##24. Generamos la ventana a partir de los datos recogidos en nuestra clase creada
    ventana.show()                                              ##25. Le decimos que la muestre (la ventana)
    app.exec()                                                 ##26. Ejecutamos el total de la aplicacion.