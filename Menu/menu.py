class Menu:
    def menuyop(self, tupla):
        for indice in range(len(tupla)):
            print(str(indice+1)+".-"+tupla[indice])

        op = -1
        while op < 1 or op > len(tupla):
            op = int(input("Ingrese una opcion: "))
        return op