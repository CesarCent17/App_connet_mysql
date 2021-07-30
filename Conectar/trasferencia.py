from Conectar.conectar import *
class Transferencia:

    def consultar_usuario(self):
        cur = unir.cursor()
        cur.execute("SELECT * FROM usuario")
        datos = cur.fetchall()
        cur.close()
        unir.close()
        return datos
    def consultanorepetir(self,cedula):

        cur = unir.cursor()
        cur.execute(f"SELECT cedula FROM usuario")
        #datos = cur.run_query()

        for cedula in cur.fetchall():
            if cedula == cedula:
                registrado = "si"
            else: #cedula != cur.fetchall():
                registrado = "no"

        cur.close()
        unir.close()
        return registrado


    def insertar_usuario(self, cedula, nombre, apellido, edad, direccion):
        cur = unir.cursor()
        sql = f"INSERT INTO usuario (cedula, nombre, apellido, edad, direccion) " \
              f"VALUES('{cedula}', '{nombre}', '{apellido}', {edad}, '{direccion}')"
        cur.execute(sql)
        contar = cur.rowcount
        msg = f"Se agrego: {contar} registro"
        unir.commit()
        cur.close()
        return msg

    def eliminar_usuarios(self, cedula):
        cur = unir.cursor()
        sql = f'DELETE FROM usuario WHERE cedula = {cedula}'
        cur.execute(sql)
        contar = cur.rowcount
        msg = f"Se eliminaron: {contar} registro"
        unir.commit()
        cur.close()
        return msg


Gaspar = Transferencia()
cedula = "0929240356"
print(Gaspar.consultanorepetir(cedula))
