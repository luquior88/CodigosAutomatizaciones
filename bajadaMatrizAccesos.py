 # -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# importo librerias 
from Google import Create_Service
import pandas as pd

# manejo errores
from ManejadorError import mailError

# defino clase
def bajadaMatrizAccesos():
	CLIENT_SECRET_FILE = 'C:/Python27/CARPETA/client_secret.json'
	API_SERVICE_NAME = 'sheets'
	API_VERSION = 'v4'
	print("entro aca")
	SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

  # defino la dirección de la googlesheet
	gsheetId = 'PEGO ACA LA DIRECCION'
	
  # 
	s = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
	gs = s.spreadsheets()
	print("paso definicion")
  # pongo la hoja a exportar
	rows = gs.values().get(spreadsheetId=gsheetId,range='Matriz de Accesos').execute()
	data = rows.get('values')
	df = pd.DataFrame(data)

  # Exporto la matriz a un csv
	export_csv = df.to_csv (r"E:/3- Reportes/MatrizAccesos.csv", index = None, header=True)


try:
	bajadaMatrizAccesos()
	print("entro")
except:
	print("Se genero un error en la bajada de la Matriz de Accesos")
