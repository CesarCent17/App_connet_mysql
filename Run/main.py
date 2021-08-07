from Entidades.entidades import * #nataly
from Inputs.entradas import * #edward
from Menu.menu import * #edward
from Ubicacion.ubicacion import * #edward
from Conectar.trasferencia import * #nataly

class Core:
    def __init__(self):
        self.opciones = () #tupla
        self.obM = Menu() #para acceder a la funcion que imprime el menu
        self.obE = Entrada() #para verificar que sea entero
        self.obUb = pos() #nos devuelve el indice
        self.obCo = Transferencia() #hace la conexion


    def main(self):
        print("Bienvenido al menu")
        self.opciones = ("Crear usuario", "Consultar usuarios", "Editar usuario", "Consulta personal", "Eliminar usuario",
        "Salir")
        opc = self.obM.menuyop(self.opciones)

        if opc == 1:
            self.crearuser()
            self.main()

        elif opc == 2:
            self.queryusers()
            self.main()

        elif opc == 3:
            self.edit()
            self.main()

        elif opc == 4:
            self.consultapersonal()
            self.main()

        elif opc == 5:
            self.deleteuser()
            self.main()

        elif opc == 6:
            print("Gracias, adios")

    def crearuser(self):
        print("\n")
        print("\t\t Registro de usuario")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = self.obE.Ced_ten("Cedula: ")
        #edad = self.obE.("Edad: ")
        edad = self.obE.year("Edad: ")
        #edad = self.obE.year("Edad: ")
        direccion =  input("Direccion: ")
        regis = self.obCo.consultanorepetir(cedula)
        if regis != 0:
            print("Usted ya tiene cuenta\n")

        else:
            tupla = (cedula, nombre, apellido, edad, direccion)

            msg = self.obCo.insertar_usuario(tupla)
            print(msg)
            print("\t\t Cuenta creada con exito!\n")

    def consultapersonal(self):
        print("\t\t Consulta personal")
        cedula = self.obE.Ced_ten("Cedula: ")
        obj = self.obCo.getUsuario(cedula) #
        if obj != None:
            print(obj.getDatos())
        else:
            print("Usted no esta registrado")


    def queryusers(self):
        print("\n")
        print("\t\t Consulta de usuario\n")

        lista = self.obCo.listar_usuario()

        for i in range(len(lista)):
            print(lista[i].getDatos())


    def deleteuser(self):
        print("\n")
        print("\t\t Eliminacion de cuenta")
        cedula = self.obE.Ced_ten("Cedula: ")
        regis = self.obCo.consultanorepetir(cedula)
        if regis == 1:
            print(self.obCo.eliminar_usuarios(cedula))
            print("Cuenta eliminada con exito\n")
        elif regis == 0:
            print("Usted no tiene cuenta!\n")


    def edit(self):
        print("\n")
        print("\t\t Editar usuario")
        cedula = self.obE.Ced_ten("Cedula: ")
        regis = self.obCo.consultanorepetir(cedula)
        if regis == 1:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = self.obE.year("Edad: ")
            direccion = input("Direccion: ")
            tupla = (nombre, apellido, edad, direccion, cedula)
            print(self.obCo.editar_usuarios(tupla))
            print("Cuenta editada con exito\n")

        elif regis == 0:
            print("Usted no tiene cuenta!\n")

