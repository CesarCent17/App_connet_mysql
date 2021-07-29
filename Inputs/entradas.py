class Entrada:
    def Int(self, msg):
        while True:
            try: #intentar
                n = int(input(msg))
                break
            except ValueError:
                print("Error, ingrese un numero entero")

        return n





