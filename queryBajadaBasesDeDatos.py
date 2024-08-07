import pandas as pd
import sqlalchemy
import os

# arriba importo librerias 

# llamo clase de manejo de errores
from ManejadorError import mailError

# clase:
def queryBajadaBasesDeDatos():
  # Defino variables con datos guardados en windows
	usuario = os.environ.get('Usuario')
	contrasenia = os.environ.get('PassNew')

  # Conecto con la base de datos:
	engine = sqlalchemy.create_engine('mysql+pymysql://'+usuario+':'+contrasenia+'@BaseDeDatos')

  # Genero la variable query con la query a ser ejecutada:
	query = ''' 

	SELECT *
	FROM Base de datos
  WHERE Condiciones

	'''

  
	df = pd.read_sql_query(query,engine)

  # Exporto a csv
	export_csv = df.to_csv (r"E:/3- Reportes/accesos.csv", index = None, header=True)


try:
	queryBajadaBasesDeDatos()
except:
	mailError("Se genero un error en la bajada de Accesos")
