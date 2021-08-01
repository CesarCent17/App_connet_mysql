class Usuario:
    def __init__(self, cedula, nombre, apellido, edad, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion

    def getDatos(self):
        msg = f"cedula: {self.cedula}\n" \
              f"nombre: {self.nombre}\n"\
              f"apellido: {self.apellido}\n" \
              "edad: "+ str(self.edad)+"\n" \
              f"direccion: {self.direccion}\n"
        return msg


