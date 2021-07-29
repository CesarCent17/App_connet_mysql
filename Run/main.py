#from Entidades.entidades import *
from Inputs.entradas import *
from Menu.menu import *
from Ubicacion.ubicacion import *
from Conectar.trasferencia import *

class Core:
    def __init__(self):
        self.opciones = () #tupla
        self.obM = Menu() #para acceder a la funcion que imprime el menu
        self.obE = Entrada() #para verificar que sea entero
        self.obUb = pos() #nos devuelve el indice
        self.obCo = Transferencia() #hace la conexion


    def main(self):
        print("Bienvenido al menu")
        self.opciones = ("Crear usuario, Eliminar usuario, Salir")
        opc = self.obM.menuyop(self.opciones)

        if opc == 1:
            self.crearuser()
            self.main()

        elif opc == 2:
            pass

        elif opc == 3:
            print("Gracias, adios")

    def crearuser(self):
        print("\t\t Registro de usuario")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = input("Cedula: ")
        edad = self.obE.Int("Edad: ")
        direccion =  input("Direccion: ")
        obj = self.obUb.posicionuser(cedula, self.obCo.consultar_usuario())
        if obj != None:
            print("Usuario ya existe!")
            self.main()
        self.obCo.insertar_usuario(cedula, nombre, apellido, edad, direccion)
        print("\t\t Cuenta creada con exito!")






