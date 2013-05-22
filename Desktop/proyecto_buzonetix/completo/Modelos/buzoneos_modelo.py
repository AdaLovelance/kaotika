# coding=utf-8
#!/usr/bin/env python

from sqlite3 import dbapi2 as sqlite
import os # Para poder comprobar si existe la base de datos o no.

#"""import clientes_modelo
#import zonas_modelo
#from clientes_modelo import BaseDatosclientes
#from zonas_modelo import BaseDatoszonas""" estos import estan aqui para recordarme que en buzoneos cliente
# el id que debe recurarse es el id del cliente al que pertenece el buzoneo, idem en el resto de los campos



class BaseDatosbuzoneos:
    """Clase que manejará la base de datos"""

    def __init__(self):
        self.__fichero = "buzoneos.dat"


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

            #CREAMOS LA TABLA BUZONEOS
            TABLA = """
                    CREATE TABLE BUZONEOS (
                        ID INTEGER PRIMARY KEY,
                        BUZONEOSCODIGOPOSTAL INT(9)
                        BUZONEOSCLIENTE VARCHAR(30),
                        BUZONEOSZONA VARCHAR(30),
                        NUMEROFOLLETOSBUZONEOS VARCHAR(30),
                        TIPOBUZONEO VARCHAR(30),
                        FECHABUZONEO VARCHAR(30),
                        )"""
            cursor.execute(TABLA)
            # MUY IMPORTANTE:
            conexion.commit()
            # devolvemos la conexión
            return conexion


class Buzoneosmodelo(BaseDatosbuzoneos):

    def recogerBuzoneosbd(self):
        """Método que devolverá una lista de buzoneos"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        # Definimos la sentencia SQL a usar
        SQL = r"SELECT * FROM buzoneos"
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

    def insertarBuzoneosbd(self, buzoneos):
        """Método para insertar nuevos buzoneos a la base de datos"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        # Definimos la sentencia SQL a usar
        SQL = r"INSERT INTO buzoneos VALUES(NULL, ?, ?, ?)"
        # y la ejecutamos
        cursor.executemany(SQL, buzoneos)
        # y ejecutamos el commit
        conexion.commit()
        # Cerramos la conexión
        conexion.close()

    def eliminarBuzoneosbd(self, buzoneos):
        """Método para eliminar buzoneos de la base de datos"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        # Definimos la sentencia SQL a usar
        SQL = r'DELETE FROM buzoneos WHERE id="%d"'
        # y la ejecutamos
        for buzoneo in buzoneos:
            cursor.execute(SQL % buzoneo)
            # y ejecutamos el commit
        conexion.commit()
        # Cerramos la conexion
        conexion.close()

    def modificarBuzoneosbd(self, buzoneos):
        """Método para modificar clientes"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        SQL = "UPDATE * FROM buzoneos WHERE id = '%d'"
        # y la ejecutamos
        for buzoneo in buzoneos:
            cursor.execute(SQL % buzoneo)
            #ejecutamos el commit
        conexion.commit()
        #Cerramos la conexion
        conexion.close()

    def actualiza(self, id, buzoneoscliente, buzoneoszona, numerofolletosbuzoneo, tipobuzoneo, ):
        conexion = self.__conectar()
        cursor = conexion.cursor()
        cursor.execute('UPDATE buzoneos SET buzoneoscliente=%s, buzoneoszona=%s, numerofolletosbuzoneo=%s, '
                       'tipobuzoneo=%s,WHERE id=%s',
            (id, buzoneoscliente, buzoneoszona, numerofolletosbuzoneo, tipobuzoneo,))
        conexion.commit()
        conexion.close()

    def nuevo(self, id, buzoneoscliente, buzoneoszona, numerofolletosbuzoneo, tipobuzoneo,):
        """
        Funcion para crear nuevas zonas
        """
        conexion = self.__conectar()
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO zonas SET buzoneoscliente=%s, buzoneoszona=%s, numerofolletosbuzoneo=%s, '
                       'tipobuzoneo=%s,WHERE id=%s',
                     (id, buzoneoscliente, buzoneoszona, numerofolletosbuzoneo, tipobuzoneo,))
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
