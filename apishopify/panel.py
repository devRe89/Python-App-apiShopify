from apishopify import connect
import os
from io import open
import pathlib
import requests
import shopify
import json
import datetime
from dotenv import load_dotenv
load_dotenv()

class Panel:

    # Conexión bd Panel
    conx = connect.Connect()
    res_conx = conx.conexion()
    conexion = res_conx[0]
    cursor = res_conx[1]

    def validaSku(self, sku):
        sql = f'SELECT id FROM base_stock WHERE sku = "{sku}"'
        self.cursor.execute(sql)
        self.cursor.fetchall()
        tuplas = self.cursor.rowcount
        return tuplas


    def actualizarStock(self, sku, stock):
        tuplas = self.validaSku(sku)
        if (tuplas > 0):
            self.updateStock(sku, stock)
        else:
            self.addStock(sku, stock)   


    def addStock(self, sku, stock):
        tiempo = datetime.datetime.now()
        sql = "INSERT INTO base_stock (sku, stock, date_upd) VALUES (%s, %s, %s)"
        data = (sku, stock, tiempo)
        try:   
            self.cursor.execute(sql, data)
            self.conexion.commit()
            print(f'se creo el stock del sku {sku}')
        except:
            print('no se pudo ingresar el stock')

    def updateStock(self, sku, stock):
        tiempo = datetime.datetime.now()
        sql = "UPDATE base_stock SET stock = %s WHERE sku = %s"
        data = (stock, sku)
        try:
            self.cursor.execute(sql, data)
            self.conexion.commit()
            print(f'Se actualizo el stock del sku {sku}')
        except:
            print('No se pudo actualizar el stock del sku {sku}')    





