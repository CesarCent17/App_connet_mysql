import mysql.connector

class Conexion:
    def conecta(self):
        dic = {"host" : "localhost", "user" :"root",
            "passwd" :"Artn0w21", "database" :"supermercado"}
        cnn = None
        try:
            cnn= mysql.connector.connect(**dic)

        except(mysql.connector.DatabaseError, mysql.connector.OperationalError, mysql.connector.IntegrityError) as e:
            print("Error de conexion"+ str(e))
        return cnn











