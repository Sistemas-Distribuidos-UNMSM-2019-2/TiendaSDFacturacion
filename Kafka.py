# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:26:03 2019

@author: Grupo01
"""

from OrdenCompra import OrdenCompraModel

from kafka import KafkaConsumer, KafkaProducer
from json import dumps, loads

consumer = KafkaConsumer(
    'factura',
     bootstrap_servers=['192.168.4.27:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='fact',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

while(True):

    for message in consumer:
        message = message.value
        
        ordenCompra = OrdenCompraModel()
        ordenCompra.nCodigoOrden = message["nCodigoOrden"]
        ordenCompra.sRucCliente = message["sRucCliente"]
        ordenCompra.nPrecioTotal = message["nPrecioTotal"]
        ordenCompra.dFechaCompra = message["dFechaCompra"]
        ordenCompra.sEstado = message["sEstado"]
        
        
        json = {
                    "nCodigoOrden" : ordenCompra.nCodigoOrden,
                    "sRucCliente" : ordenCompra.sRucCliente,
                    "nPrecioTotal" : ordenCompra.nPrecioTotal,
                    "sEstado" : "Reservado"
                }
        print(dumps(json))
    
        producer = KafkaProducer(bootstrap_servers=['192.168.4.27:9092'],
                             value_serializer=lambda x: 
                             dumps(x).encode('utf-8'))
        producer.send('cuentas', value=json)    
        
    
    