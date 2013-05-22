#-*-encoding:UTF8-*-

import sys
import os
import clientes_modelo
import mainwindow
from Modelos import clientes_modelo
from mainwindow import Ui_VentanaPrincipal
from mainwindow import *
from clientes_modelo import *


class Controlador(mainwindow,clientes_modelo):
    def muestraclientes(self):
        vtnclientes = mainwindow.Ui_VentanaPrincipal.ventanaclientes
        mostrarcliente = mainwindow.Ui_VentanaPrincipal.tableWidgetmostrarclientes
        self.mostarclientes = clientes_modelo.ClientesModelo.recogerClientesbd(self,mostrarcliente)



