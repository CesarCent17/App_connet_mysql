class Entrada:
    def Int(self, msg):
        while True:
            try: #intentar
                n = int(input(msg))
                break
            except ValueError:
                print("Error, ingrese un numero entero")

        return n

    def Ced_ten(self, msg):

        while True:
            cedula = input(msg)
            if len(cedula) == 10:
                break
            elif len(cedula) != 10:
                print("Error, la cedula debe tener 10 digitos\n")


        return cedula

    def year(self, msg):
        while True:
            try: #intentar
                n = int(input(msg))
                if n <= 127 and n > 0:
                    break
                #elif n >127 and n <0:
                else:
                    print("Error, ingrese una edad correcta")
            except ValueError:
                print("Error, ingrese un numero entero")

        return n




