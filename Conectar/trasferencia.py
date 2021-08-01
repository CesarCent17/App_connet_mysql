from Conectar.conectar import *
class Transferencia:

    def consultar_usuario(self):
        cur = unir.cursor()
        cur.execute("SELECT * FROM usuario")
        datos = cur.fetchall()
        cur.close()
        #unir.close()
        return datos
    def consultanorepetir(self,cedula):

        cur = unir.cursor()
        cur.execute(f"SELECT cedula FROM usuario WHERE cedula = '{cedula}'")
        registro = len(cur.fetchall())
        cur.close()
        #unir.close()
        return registro


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


    def editar_usuarios(self,cedula, nombre, apellido, edad, direccion):
        cur = unir.cursor()
        sql = f"UPDATE usuario\
        SET nombre = '{nombre}', apellido = '{apellido}', edad = {edad}, direccion =\
        '{direccion}' WHERE cedula = '{cedula}'"
        cur.execute(sql)
        contar = cur.rowcount
        msg = f"Se modifico: {contar} registro"
        unir.commit()
        cur.close()
        return msg
