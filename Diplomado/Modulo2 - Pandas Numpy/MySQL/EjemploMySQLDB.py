# Instalar sqlalchemy
# Instalar pymysql

# Importar las librerias
from sqlalchemy import create_engine
import pymysql
import pandas as pd

# Crear el motor (dialecto :// usuarioBD:clave @ ipHostDBMS:puerto /esquema
sqlEngine = create_engine('mysql+pymysql://live:live@192.168.196.130:3306/pandasLIVE', pool_recycle=3600)

# Establecer la conexión
dbConnection = sqlEngine.connect()

# Realizar la consulta
datos  = pd.read_sql("select * from datos", dbConnection);
print('Datos en la tabla datos de la base de datos pandasLIVE')
print(datos)
print('\nPromedio de edades: ', datos['edad'].mean())

# Cerrando la Conexión
dbConnection.close()