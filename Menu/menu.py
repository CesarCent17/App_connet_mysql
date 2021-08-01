from Inputs.entradas import *

class Menu:

    def __init__(self):
        self.checknum = Entrada()


    def menuyop(self, tupla):
        for indice in range(len(tupla)):
            print(str(indice+1)+".-"+tupla[indice])

        op = -1
        while op < 1 or op > len(tupla):
            op = self.checknum.Int("Ingrese una opcion: ")
        return op