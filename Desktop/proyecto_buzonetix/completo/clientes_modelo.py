# coding=utf-8
#!/usr/bin/env python

import sqlite3
from sqlite3 import dbapi2 as sqlite
import os # Para poder comprobar si existe la base de datos o no.




class BaseDatosclientes:
    """Clase que manejará la base de datos"""

    def __init__(self):
        self.__fichero = "clientes.dat"


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
# Creamos la tabla CLIENTES
            TABLA = """
                    CREATE TABLE CLIENTES (
                    ID INTEGER PRIMARY KEY,
                    NOMBRE VARCHAR(20),
                    APELLIDOS VARCHAR(40),
                    EMAIL VARCHAR(30),
                    TELEFONO VARCHAR(12),
                    EMPRESA VARCHAR(30),
                    CIFONIF VARCHAR(30),
                        );"""
                        # ejecutamos la sentencia
            cursor.execute(TABLA)
                        # MUY IMPORTANTE:
            conexion.commit()
                        # devolvemos la conexión
            return conexion


class ClientesModelo(BaseDatosclientes):
    """A partir de aqui comienza el código de la bd para insertar,
        mostrar,
        y eliminar clientes. Todo esto es lo relativo a clientes
    """

    def recogerClientesbd(self):
        """Método que devolverá una lista de clientes"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        # Definimos la sentencia SQL a usar
        SQL = r"SELECT * FROM clientes"
        # y la ejecutamos
        cursor.execute(SQL)
        # Recojemos los resultados
        resultados = cursor.fetchall()
        # Cerramos la conexión
        conexion.close()
        #Devolvemos los resultados o None si no hay
        if resultados:
            return resultados
        else:
            return None

    def insertarClientesbd(self, clientes):
        """Método para insertar nuevos clientes a la base de datos"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        # Definimos la sentencia SQL a usar
        SQL = r"INSERT INTO clientes VALUES(NULL, ?, ?, ?)"
        # y la ejecutamos
        cursor.executemany(SQL, clientes)
        # y ejecutamos el commit
        conexion.commit()
        # Cerramos la conexión
        conexion.close()

    def eliminarClientesbd(self, clientes):
        """Método para eliminar clientes de la base de datos"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        # Definimos la sentencia SQL a usar
        SQL = r'DELETE FROM clientes WHERE id="%d"'
        # y la ejecutamos
        for cliente in clientes:
            cursor.execute(SQL % cliente)
            # y ejecutamos el commit
        conexion.commit()
        # Cerramos la conexion
        conexion.close()

    def modificarClientesbd(self, clientes):
        """Método para modificar clientes"""
        conexion = self.__conectar()
        cursor = conexion.cursor()
        SQL = "UPDATE * FROM clientes WHERE id = '%d'"
        # y la ejecutamos
        for cliente in clientes:
            cursor.execute(SQL % cliente)
        #ejecutamos el commit
        conexion.commit()
        #Cerramos la conexion
        conexion.close()

    def actualiza(self, id, nombre, apellidos, telefono, email, empresa, cifonif ):

        """
        Esta funcion sirve para actualizar los campos individualmente*?
        """
        conexion = self.__conectar()
        cursor = conexion.cursor()

        cursor.execute('UPDATE clientes SET nombre=%s, apellidos=%s, telefono=%s, email=%s, empresa=%s,'
                     'cifonif=%s WHERE id=%s',
            (id, nombre, apellidos, telefono, email, empresa, cifonif))

        conexion.commit()
        conexion.close()

    def nuevo(self, id, nombre, apellidos, telefono, email, empresa, cifonif):

        """
        Esta funcion sirve para crear un cliente nuevo campo a campo
        """
        conexion = self.__conectar()
        cursor = conexion.cursor()

        cursor.execute('INSERT INTO zonas SET nombre=%s, apellidos=%s, telefono=%s, email=%s, empresa=%s,'
                     'cifonif=%s WHERE id=%s',
                     (id, nombre, apellidos, telefono, email, empresa, cifonif))
        conexion.commit()
        conexion.close()
        return cursor.execute()

    def borra(self, id):
        conexion = self.__conectar()
        cursor = conexion.cursor()

        cursor.execute('DELETE FROM clientes WHERE id=%s', (id))
        conexion.commit()
        conexion.close()


    def recupera(self, id):
        conexion = self.__conectar()
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM clientes WHERE id=%s', (id))

        conexion.commit()
        conexion.close()
        return cursor.execute()
