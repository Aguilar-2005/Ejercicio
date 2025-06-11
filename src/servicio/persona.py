from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow

from src.UI.vtnPrincipal import Ui_vtnPrincipal


class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self).__init__ ()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnBorrar.clicked.connect(self.borrar)
        self.ui.txtCedula.setValidator(QIntValidator())
    def guardar(self):
        if self.ui.txtNombres.text() == '' or self.ui.txtApellidos.text() == ''\
                or self.ui.txtCedula.text() == '' or self.ui.txtEmail.text()  == ''\
                or self.ui.cbGenero.currentText()  == 'Seleccionar':

            print('Ingresar todos los datos')
        else:
            print('Se puede guardar')
            print(self.ui.txtNombres.text())
            print(self.ui.txtApellidos.text())
            print(self.ui.txtCedula.text())
            print(self.ui.cbGenero.currentText())
            print(self.ui.txtEmail.text())
            print("Se hizo click en el botón guardar")

    def borrar(self):
            self.ui.txtNombres.setText("")
            self.ui.txtApellidos.setText("")
            self.ui.txtCedula.setText("")
            self.ui.cbGenero.setCurrentText("")
            self.ui.txtEmail.setText("")
            print("Se eliminó con éxito")

