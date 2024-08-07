# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
 # importo librerias necesarias.

import pandas as pd
import sqlite3

 # llamo al manejo de errores
from ManejadorError import mailError
 # defino la clase

def SubidaDatosBD():
	# Cargo csv de accesos
	print ("leo datos")
	dfAccesos = pd.read_csv("E:/3- Reportes/accesos.csv")
  # Cargo csv Nomina
  dfRRHH = pd.read_csv("C:/Users/luis.rios/Desktop/RRHH.csv")
	print ("pase lo primero")
  # Cargo csv de Matriz de accesos
	dfMatrizAccesos = pd.read_csv("E:/3- Reportes/MatrizAccesos.csv", header = 2)
	print ("pase subida de Matriz de accesos")

	# ~ #Tomo las columnas que requiero y las concateno
	print ("llegue a lo de columnas de los accesos")
	dfAccesos.columns = dfAccesos.columns.str.strip()
  print ("llegue a lo de columnas de la Matriz")
	dfMatrizAccesos.columns = dfMatrizAccesos.columns.str.strip()
	print ("arranca RRHH")
	dfRRHH.columns = dfRRHH.columns.str.strip()
	# load data y me conecto con la base de datos
	con = sqlite3.connect("E:/3- Reportes/Base de Datos/access.db")
	con.text_factory = str
	cursor = con.cursor()

	print ("ahora dropeo")
  # Dropeo los datos previos en las tablas
	cursor.execute("DROP TABLE IF EXISTS ACCESS")
	cursor.execute("DROP TABLE IF EXISTS MATRIZACCESOS")
	cursor.execute("DROP TABLE IF EXISTS RRHH")

	# cargo data into database
	print ("cargo datos")
	dfAccesos.to_sql("ACCESS", con)
	dfMatrizAccesos.to_sql("MATRIZACCESOS", con)
	print ("llegue hasta rrhh")
	dfRRHH.to_sql("RRHH", con)

  # En el caso de realizar algún alter descomentar lo siguiente
	# print("entro a ejecutar")
	# cursor.execute("ALTER TABLE ACCESS ADD COLUMN "PONER COLUMNA" VARCHAR(6) DEFAULT 'PONER LO QUE NECESTAMOS';")

	con.close()


try:
	SubidaDatosBD()
except:
	print("Se genero un ERROR en la Actualizacion de la Base de Datos Local")
