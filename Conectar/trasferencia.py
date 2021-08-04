from Conectar.conectar import *
from Entidades.entidades import *


class Transferencia:
    def __init__(self):
        self.obCo = Conexion()



    def consultar_usuario(self):
        cnn = self.obCo.conecta()

        cur = cnn.cursor()
        cur.execute("SELECT * FROM usuario")
        datos = cur.fetchall()
        cur.close()
        #unir.close()
        return datos

    def listar_usuario(self):
        lista = []
        cnn = self.obCo.conecta()
        cur = cnn.cursor()
        cur.execute("SELECT * FROM usuario")
        datos = cur.fetchall()
        for i in range(len(datos)):
            obj = Usuario(datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5])
            lista.append(obj)
        cur.close()
        #unir.close()
        return lista



    def getUsuario(self, cedula):
        obj = None
        cnn = self.obCo.conecta()
        cur = cnn.cursor()
        cur.execute(f"SELECT * FROM usuario WHERE cedula = {cedula}")
        datos = cur.fetchall()
        if len(datos) == 1:
            obj = Usuario(datos[0][1], datos[0][2], datos[0][3], datos[0][4], datos[0][5])
        cur.close()
        #unir.close()
        return obj


    def consultanorepetir(self,cedula):
        cnn = self.obCo.conecta()
        cur = cnn.cursor()
        cur.execute(f"SELECT cedula FROM usuario WHERE cedula = '{cedula}'")
        registro = len(cur.fetchall())
        cur.close()
        #unir.close()

        return registro


    def insertar_usuario(self, tupla):

        cnn = self.obCo.conecta()
        cur = cnn.cursor()
        sql = f"INSERT INTO usuario (cedula, nombre, apellido, edad, direccion) " \
              f"VALUES(%s,%s ,%s,%s,%s)"
        cur.execute(sql, tupla)
        contar = cur.rowcount
        msg = f"Se agrego: {contar} registro"
        cnn.commit()
        cur.close()
        return msg

    def eliminar_usuarios(self, cedula):
        cnn = self.obCo.conecta()
        cur = cnn.cursor()
        sql = f'DELETE FROM usuario WHERE cedula = {cedula}'
        cur.execute(sql)
        contar = cur.rowcount
        msg = f"Se eliminaron: {contar} registro"
        cnn.commit()
        cur.close()
        return msg


    def editar_usuarios(self, tupla):
        cnn = self.obCo.conecta()
        cur = cnn.cursor()
        sql = f"UPDATE usuario\
        SET nombre = %s, apellido = %s, edad = %s, direccion =\
        %s WHERE cedula = %s"
        cur.execute(sql, tupla)
        contar = cur.rowcount
        msg = f"Se modifico: {contar} registro"
        cnn.commit()
        cur.close()
        return msg
