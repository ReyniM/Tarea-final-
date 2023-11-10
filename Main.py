# ARCHIVO TRABAJO PRINCIPAL.
from funciones import *


url_general = ("https://opendata.emtmadrid.es/getattachment/7a88cb04-9007-4520-88c5-a94c71a0b925/trips_23_02_February-csv.aspx")


cvs_file = csv_from_zip(url_general) # CREO LA VARIABLE CVS_FILE PARA GUARDAR MI FICHERO CSV.


usos = get_data(cvs_file)

# ELIMINANDO COLUMNAS DEL DATAFRAME.

usos.pop('dock_unlock')
usos.pop('dock_lock')


# COMENTANDO --> usos.info()

# COMENTANDO LOS RESULTADOS DEL INFO() SOBRE EL DATAFRAME SE OBSERVA
# COMO DEVUELVE LOS TIPOS DE DATOS DE CADA COLUMNA (POR EJ. LAS COLUMNAS
# TIPO FECHA SON DE TIPO DATETIME64[NS]), ENUMERA TAMBIEN CUANTOS
# HAY DE CADA UNO. ADEMAS, PRESENTA LA CANTIDAD DE ENTRADAS QUE TIENE
# EL FICHERO UNAS (336988), CUANTAS COLUMNAS TIENE Y LA CANTIDAD DE MEMORIA EN USO QUE UTILIZA.


usos.dropna(inplace=True)

# COMENTANDO --> usos(delete_nan_rows)

# AL EJECUTAR EL COMANDO SE OBSERVA COMO HA DISMINUIDO LA CANTIDAD
# DE FILAS TOTALES EN EL DATAFRAME. ESTO CONCLUYE QUE LA FUNCION
# REALIZADA PARA BORRAR LOS NAN HA RESULTADO.


# EXPLORACION DE LAS COLUMNAS

count_colum_fleet = usos.fleet.unique()
count_colum_locktype = usos.locktype.unique()
count_colum_unlocktype = usos.unlocktype.unique()
print(f'En la columna fleet hay: {len(count_colum_fleet)} valores distintos.'
      f'\n'
      f'En la columna locktype hay: {len(count_colum_locktype)} valor distinto.'
      f'\n'
      f'En la columna unlocktype hay: {len(count_colum_unlocktype)} valor distinto.')



# CAMBIO DE TIPOS DE DATOS
# LLAMAR FUNCION --> FLOAT_TO_STR

# CONSULTAS:

# 1- ¿Cuántas bicicletas han sido desbloqueadas de una estación y no se bloquean en ninguna?

print('\n','PREGUNTA 1')

mask1 = usos.locktype == 'STATION'
mask2 = usos.locktype != 'STATION'
print(f'La cantidad de bicicletas que han sido desbloqueadas '
      f'de una estación y no se bloquean en ninguna es: {len(usos[mask1 & mask2])}')


# 2- Seleccionar solo las bicicletas del tipo de flota '1' . El nuevo dataframe se ha de llamar regular_fleet.
#print('\n','PREGUNTA 2')
#mask = usos['fleet'] == 1
#regular_fleet = usos[mask]
#print(regular_fleet)


# 3- función llamada day_time para calcular las horas totales de uso de bicicletas por día del mes.
# LLAMAR FUNCION DAY_TIME
print('\n','PREGUNTA 3')


# 4- función llamada weekday_time para calcular las horas totales de uso de bicicletas por día de la semana.
print('\n','PREGUNTA 4')

def week_day(df: pd):
    pass

#dia_sem = {0: 'Lunes', 1: 'Martes', 2: 'Miercoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sabado', 6: 'Domingo'}
#dia = usos.fecha
#print(dia)
#calc = dia_sem[dia]
#print(usos.groupby(calc).trip_minutes.sum() / 60)

# 5- Crea una función llamada total_usage_day para calcular el número total de usos de bicicletas por día del mes.
# LLAMAR FUNCION.
print('\n','PREGUNTA 5')


# 6- Calcular el total de usos por fecha y estación de desbloqueo.
print('\n','PREGUNTA 6')

print(usos.groupby(['fecha', 'station_unlock']).station_unlock.size())

# 7- averiguar la dirección de las estaciones de desbloqueo que a lo largo del mes han tenido un mayor número de viajes.
# LLAMAR FUNCION.
print('\n','PREGUNTA 7')


# 8- averiguar el número de usos de las estaciones de desbloqueo que al mes ha tenido un mayor número de viajes.
# LLAMAR FUNCION.
print('\n','PREGUNTA 8')


print(most_popular_stations(usos), '\n', usage_from_most_popular_station(usos))

