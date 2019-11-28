# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:12:06 2019

@author: Grupo01
"""
import datetime

class OrdenCompraModel:
    nCodigoOrden = 0
    sRucCliente = ""
    nPrecioTotal = 0.0
    dFechaCompra = datetime.datetime.now()
    dFechaPago = datetime.datetime.now()
    sEstado = ""
    lDetalleCompra = []

