# coding=utf-8
#!/usr/bin/env python

from sqlite3 import dbapi2 as sqlite
import os # Para poder comprobar si existe la base de datos o no.



class BaseDatoszonas:
    """Clase que manejará la base de datos"""

    def __init__(self):
        self.__fichero = "zonas.dat"


    def __conectar(self):
        """Método privado, que nos servirá para conectarnos a la base de datos."""

# Comprobamos si ya existe la base de datos
# para simplemente, conectarnos.

        if os.path.exists(self.__fichero):
            return sqlite.connect(self.__fichero)

        # En caso de que no exista, creamos la base de datos.

        else:

            conexion = sqlite.connect(self.__fichero)
            cursor = conexion.cursor()
            #CREAMOS LA TABLA ZONAS
            TABLA = """
                    CREATE TABLE ZONAS (
                    ID INTEGER PRIMARY KEY,
                    CODIGOPOSTAL VARCHAR(20),
                    TIPOZONA VARCHAR(30),
                    CANTIDADFOLLETOS VARCHAR(20),
                    PRECIOPORMILLAR VARCHAR(30),
                    PRECIOTOTAL VARCHAR(20)"""
            cursor.execute(TABLA)
            #CREAMOS LA TABLA BUZONEOS
            conexion.commit()
                        # devolvemos la conexión
            return conexion

class Zonasmodelo(BaseDatoszonas):
    """A partir de aqui comienza el código de la bd para insertar,
        mostrar,
        y eliminar Zonas. Todo esto es lo relativo a Zonas
    """
    def recogerZonasbd(self):
        """Método que devolverá una lista de zonas"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        # Definimos la sentencia SQL a usar
        SQL = r"SELECT * FROM zonas"
        # y la ejecutamos
        cursor.execute(SQL)
        # Recojemos los resultados
        resultados = cursor.fetchall()
        # Cerramos la conexión
        conexion.close()
        # Devolvemos los resultados o None si no hay
        if resultados:
            return resultados
        else:
            return None

    def insertarZonasbd(self, zonas):
        """Método para insertar nuevas zonas a la base de datos"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        # Definimos la sentencia SQL a usar
        SQL = r"INSERT INTO zonas VALUES(NULL, ?, ?, ?)"
        # y la ejecutamos
        cursor.executemany(SQL, zonas)
        # y ejecutamos el commit
        conexion.commit()
        # Cerramos la conexión
        conexion.close()

    def eliminarZonasbd(self, zonas):
        """Método para eliminar zonas de la base de datos"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        # Definimos la sentencia SQL a usar
        SQL = r'DELETE FROM zonas WHERE id="%d"'
        # y la ejecutamos
        for zona in zonas:
            cursor.execute(SQL % zona)
            # y ejecutamos el commit
        conexion.commit()
        # Cerramos la conexion
        conexion.close()

    def modificarZonasbd(self, zonas):
        """Método para modificar clientes"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        SQL = "UPDATE * FROM zonas WHERE id = '%d'"
        # y la ejecutamos
        for zona in zonas:
            cursor.execute(SQL % zona)
            #ejecutamos el commit
        conexion.commit()
        #Cerramos la conexion
        conexion.close()


    def actualiza(self, id, codigopostal, tipozona, cantidadfolletos, preciomillar, preciototal, ):
        conexion = self.__conectar()
        cursor = conexion.cursor()
        cursor.execute('UPDATE zonas SET codigopostal=%s, tipozona=%s, cantidadfolletos=%s, preciomillar=%s, preciototal=%s,'
                     'WHERE id=%s',
            (id, codigopostal, tipozona, cantidadfolletos, preciomillar, preciototal))
        conexion.commit()
        conexion.close()

    def nuevo(self, id, codigopostal, tipozona, cantidadfolletos, preciomillar, preciototal,):
        """
        Funcion para crear nuevas zonas
        """
        conexion = self.__conectar()
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO zonas SET codigopostal=%s, tipozona=%s, cantidadfolletos=%s, preciomillar=%s,'
                     ' preciototal=%s, WHERE id=%s',
                     (id, codigopostal, tipozona, cantidadfolletos, preciomillar, preciototal))
        conexion.commit()
        conexion.close()
        return cursor.execute()

    def borra(self, id):
        conexion = self.__conectar()
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM zonas WHERE id=%s', (id))
        conexion.commit()
        conexion.close()

    def recupera(self, id):
        conexion = self.__conectar()
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM zonas WHERE id=%s', (id))
        conexion.commit()
        conexion.close()
        return cursor.execute()

