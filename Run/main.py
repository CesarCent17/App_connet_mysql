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
        self.opciones = ("Crear usuario", "Consultar usuarios", "Eliminar usuario", "Salir")
        opc = self.obM.menuyop(self.opciones)

        if opc == 1:
            self.crearuser()
            self.main()

        elif opc == 2:
            self.queryusers()
            self.main()
        elif opc == 3:
            pass

        elif opc == 4:
            print("Gracias, adios")

    def crearuser(self):
        print("\t\t Registro de usuario")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = input("Cedula: ")
        edad = self.obE.Int("Edad: ")
        direccion =  input("Direccion: ")
        regis = self.obCo.consultanorepetir(cedula)
        if regis != 0:
            print("Usted ya tiene cuenta")

        else:
            self.obCo.insertar_usuario(cedula= cedula, nombre= nombre, apellido= apellido, edad= edad, direccion=direccion)
            print("\t\t Cuenta creada con exito!")

        print("\t\t Cuenta creada con exito!")




    def queryusers(self):
        print(self.obCo.consultar_usuario())






