class pos:
    def posicionuser(self, cedula, listadeusuarios):
        for indice in range(len(listadeusuarios)):
            pos = None
            if cedula == listadeusuarios[indice]:
                pos = indice
                break

        return pos



