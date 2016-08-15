import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
sys.path.append('../Constants')
sys.path.append('../Code')
import Constants
import Calculator

class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.calculadora()

    def calculadora(self):

        self.line = QtGui.QLineEdit(self)
        self.line.move(5,20)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.resize(160,25)

        cero = QtGui.QPushButton("0",self)
        cero.move(10,180)
        cero.resize(35,30)

        uno = QtGui.QPushButton("1",self)
        uno.move(10,145)
        uno.resize(35,30)

        dos = QtGui.QPushButton("2",self)
        dos.move(50,145)
        dos.resize(35,30)

        tres = QtGui.QPushButton("3",self)
        tres.move(90,145)
        tres.resize(35,30)

        cuatro = QtGui.QPushButton("4",self)
        cuatro.move(10,110)
        cuatro.resize(35,30)

        cinco = QtGui.QPushButton("5",self)
        cinco.move(50,110)
        cinco.resize(35,30)

        seis = QtGui.QPushButton("6",self)
        seis.move(90,110)
        seis.resize(35,30)

        siete = QtGui.QPushButton("7",self)
        siete.move(10,75)
        siete.resize(35,30)

        ocho = QtGui.QPushButton("8",self)
        ocho.move(50,75)
        ocho.resize(35,30)

        nueve = QtGui.QPushButton("9",self)
        nueve.move(90,75)
        nueve.resize(35,30)

        mas = QtGui.QPushButton("+",self)
        mas.move(130,75)
        mas.resize(35,30)

        menos = QtGui.QPushButton("-",self)
        menos.move(130,110)
        menos.resize(35,30)

        igual = QtGui.QPushButton("=",self)
        igual.move(130,145)
        igual.resize(35,65)
        igual.clicked.connect(self.Igual)

        c = QtGui.QPushButton("c",self)
        c.move(50,180)
        c.resize(75,30)
        c.clicked.connect(self.C)

        numeros = [cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve]

        operaciones = [c,mas,menos,igual]

        for i in numeros:
            i.clicked.connect(self.Numeros)
        
        for i in operaciones[1:3]:
            i.clicked.connect(self.Operaciones)

        self.setGeometry(300,300,210,220)
        self.setFixedSize(210,220)
        self.setWindowTitle("Calculadora")
        self.show()

    def Numeros(self,presionado):

        sender = self.sender()
        numero2 = int(sender.text())
        ponerNumero = str(numero2)

        if presionado == False:
            self.line.setText(self.line.text() + ponerNumero)

        else:
            self.line.setText(ponerNumero)
            presionado = False

    def Operaciones(self,mostrar):

        mostrar += 1

        if mostrar > 1:
            self.Igual()

        numero1 = self.line.text()
        sender = self.sender()
 
        operador = sender.text()
        presionado = True

    def Igual(self,numero1,operador):

        mostrar = 0
        numero2 = self.line.text()

        print(numero1)
        print(numero2)
        #print(operador)

        if operador == "+":
            resultado = suma(self,numero1,numero2)

        elif operador == "-":
            resultado = resta(self,numero1,numero2)

        print(resultado)
        self.line.setText(str(resultado))
        presionado = True

    def C(self):
        self.line.clear()

        numero1 = 0
        numero2 = 0
        resultado = 0
        operador = ""

def main():
    app = QtGui.QApplication(sys.argv)
    main= Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()        
