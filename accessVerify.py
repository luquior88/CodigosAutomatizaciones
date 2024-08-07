# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# importo librerias
import sqlite3
import os
import csv
# ~ manejo de errores: 
from ManejadorError import mailError

# defino clase para verificar los accesos
def accessVerify():
	lista =[]
  # me conecto a la base local
	conn = sqlite3.connect("E:/3- Reportes/Base de Datos/access.db")
	cur = conn.cursor()
	print ("por ejecutar query")

  # agrego la query a ejecutar:
	coords = cur.execute("""
	
	SELECT DISTINCT A3.APPLICATION, A3.ROL, A3.MAIL,RH.[PRIMER_NOMBRE] Nombre, RH.APELLIDO Apellido, RH.DEPARTAMENTO, RH.PUESTO, RH.MANAGER_NAME, RH.TERMINATION_DATE [Fecha de Baja]	
	FROM (SELECt r1.* 
	fROM RRHH r1
	where r1.TERMINATION_DATE is not null and
	r1.EMAIL_ADDRESS in (SELECT a1.EMAIL_ADDRESS from rrhh a1 where a1.TERMINATION_DATE is not null 
	EXCEPT
	SELECT b1.EMAIL_ADDRESS from rrhh b1 where b1.TERMINATION_DATE is null )
	UNION
	SELECT r2.* FROM RRHH r2
	WHERE r2.TERMINATION_DATE is null) RH,
	ACCESS A3,  MATRIZACCESOS MA3	
	WHERE MA3.[ID APLICACION] = A3.ID	
	AND A3.ROL = MA3.[Rol/Permiso]	
	AND A3.MAIL = RH.[EMAIL_ADDRESS]	
	AND ((RH.DEPARTAMENTO  not in ( SELECT MA3.[AREA ADI] from MATRIZACCESOS MA3 WHERE MA3.[ID APLICACION] = A3.ID AND A3.ROL = MA3.[Rol/Permiso])	
	AND RH.PUESTO not in ( SELECT MA3.[PUESTO ADI] from MATRIZACCESOS MA3 WHERE MA3.[ID APLICACION] = A3.ID AND A3.ROL = MA3.[Rol/Permiso]))	
	OR (RH.DEPARTAMENTO  not in ( SELECT MA3.[AREA ADI] from MATRIZACCESOS MA3 WHERE MA3.[ID APLICACION] = A3.ID AND A3.ROL = MA3.[Rol/Permiso])	
	AND RH.PUESTO in ( SELECT MA3.[PUESTO ADI] from MATRIZACCESOS MA3 WHERE MA3.[ID APLICACION] = A3.ID AND A3.ROL = MA3.[Rol/Permiso]))	
	OR (RH.DEPARTAMENTO in ( SELECT MA3.[AREA ADI] from MATRIZACCESOS MA3 WHERE MA3.[ID APLICACION] = A3.ID AND A3.ROL = MA3.[Rol/Permiso])	
	AND RH.PUESTO not in ( SELECT MA3.[PUESTO ADI] from MATRIZACCESOS MA3 WHERE MA3.[ID APLICACION] = A3.ID AND A3.ROL = MA3.[Rol/Permiso]))	
	or RH.TERMINATION_DATE IS NOT NULL)
	
	""").fetchall()
	results = coords
	print ("llene coords")
	for row in results:
		lista.append(row)
		# ~ print ("en el for")
  # escribo el csv con los errores en accesos
	def escribo_csv(lista):
		with open('E:/3- Reportes/ErroresAccesos.csv', 'wb') as outfile:
			writer = csv.writer(outfile)
			writer.writerows(lista)
			print ("escribi lista")
	print("dps del listar")		
	cabecera  =  ["APP","ROL","MAIL","NOMBRE","APELLIDO","Departamento","Puesto","Nombre Supervisor","Fecha de Baja"]
	lista.insert(0, cabecera)
	print ("escribi cabecera")	

	escribo_csv(lista)
	print("funciono")

try:
	accessVerify()
	print ("entre")
except:
	mailError("Se genero un ERROR en el ANALISIS de ACCESOS INCORRECTOS")
