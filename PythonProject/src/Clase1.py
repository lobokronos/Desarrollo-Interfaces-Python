from PySide6.QtWidgets import QMainWindow, QApplication
import sys
from src.Clase2Interfaz import Ui_MainWindow


class Clase1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Instancia la interfaz generada
        self.ui.setupUi(self)      # Configura la interfaz con la ventana principal
        self.ui.btnIncrementar.clicked.connect(lambda : self.sumar_restar(1))
        self.ui.btnDecrementar.clicked.connect(lambda : self.sumar_restar(-1))
        self.ui.btnReset.clicked.connect(lambda : self.sumar_restar(-int(self.ui.lblContador.text())))
        self.ui.bntSumar.clicked.connect(lambda: self.sumarCampo())
        self.ui.btnRestar.clicked.connect(lambda : self.restarCampo())
        self.setWindowTitle("Clase1")

    def sumar_restar(self, numero):
        try:
            # Obtener el valor actual del QLabel y convertirlo en entero
            contador = int(self.ui.lblContador.text())
            # Actualizar el texto del QLabel con el nuevo valor
            self.ui.lblContador.setText(str(contador + numero))

        except ValueError:
            print("Numero invalido")

    def sumarCampo(self):
        try:
            # Convertir el texto del QLabel a entero
            contador = int(self.ui.lblContador.text())
            # Convertir el texto del QPlainTextEdit a entero
            numeroIntroducido = int(self.ui.plainTextEdit.toPlainText())
            # Actualizar el QLabel sumando los valores
            self.ui.lblContador.setText(str(contador + numeroIntroducido))
            # Cambiar el color del QLabel según el nuevo valor
            self.color(contador + numeroIntroducido)
        except ValueError:
            print("Error: Por favor, introduce un número válido en el campo de texto o en el contador.")

    def restarCampo(self):
        try:
            # Convertir el texto del QLabel a entero
            contador = int(self.ui.lblContador.text())
            # Convertir el texto del QPlainTextEdit a entero
            numeroIntroducido = int(self.ui.plainTextEdit.toPlainText())
            # Actualizar el QLabel restando los valores
            self.ui.lblContador.setText(str(contador - numeroIntroducido))
            # Cambiar el color del QLabel según el nuevo valor
            self.color(contador - numeroIntroducido)
        except ValueError:
            print("Error: Por favor, introduce un número válido en el campo de texto o en el contador.")

    def color(self,valor):
            if valor >0:
                self.ui.lblContador.setStyleSheet("QLabel{color: green;}")

            if valor <0:
                self.ui.lblContador.setStyleSheet("QLabel{color: red;}")

            if valor ==0:
                self.ui.lblContador.setStyleSheet("QLabel{color: black;}")




# Bloque principal
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crea la aplicación
    window = Clase1()             # Crea la ventana principal
    window.show()                 # Muestra la ventana
    sys.exit(app.exec())          # Ejecuta el bucle de eventos
