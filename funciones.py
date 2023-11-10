# FUNCIONES GENERALES

import requests
import re
import io
import zipfile
import csv
import pandas as pd


def casar_fichero(link: str) -> list:
    """
    :param link: toma este argumento de tipo str.

    :return: devuelve el contenido del fichero csv
    que se necesita del tipo list.
    """
    dataere = re.compile(r'\'(\w+_\w+.\w+)\'')
    fichero_csv = list(dataere.findall(link))
    return fichero_csv


def csv_from_zip(link_fichero: str):
    """
    :param: toma como argumento la url de un fichero zip de datos
     llamado en la función como -> link_fichero_zip de tipo str.

    :return: devuelve el fichero de datos en formato bytes.
    """

    r = requests.get(link_fichero)
    if r.status_code == 404:
        raise ConnectionError('Request to server failed!')
    else:
        bytes = io.BytesIO(r.content)
        fichero_zip = zipfile.ZipFile(bytes)

        # EN ESTA PARTE CASO EL FICHERO CSV LLAMANDO UNA FUNCION Y LO COLOCARE
        # EN LA VARIABLE LINK_CORTO PARA ABRIR EL ARCHIVO CASADO QUE SALDRA DE TIPO BYTES.

        lista_ficheros = str(fichero_zip.filelist)
        link_corto = ''.join(casar_fichero(lista_ficheros))

        # AQUI VOY A ABRIR EL CONTENIDO DEL LINK_CORTO QUE ES LO
        # QUE ME INTERESA.

        with fichero_zip.open(link_corto) as file:
            contents = file.read()
            contents_decode = contents.decode('utf-8')
            file_csv = io.StringIO(contents_decode)
            reader = csv.DictReader(file_csv, delimiter=';')
            dicts = list(reader)

            # CREANDO EL ARCHIVO CSV A PARTIR DE LA LISTA
            # DE DICCIONARIOS QUE YA SE TIENE.

            campos = ['fecha','idBike','fleet','trip_minutes','geolocation_unlock','address_unlock','unlock_date',
                      'locktype','unlocktype','geolocation_lock','address_lock','lock_date','station_unlock',
                      'dock_unlock','unlock_station_name','station_lock','dock_lock','lock_station_name']

            with open('../tabla.csv', mode='w') as cvsfile:
                writer = csv.DictWriter(cvsfile, delimiter=',', fieldnames=campos)
                writer.writeheader()
                writer.writerows(dicts)

            return 'tabla.csv'  # AQUI HAGO RETORNO DEL ARCHIVO CSV PREVIAMENTE CREADO.


def get_data(file: csv) -> pd:
    """
    :param file: Esta función recibe como parametro un fichero
    csv con los datos de bicimadrid.

    :return: Devuelve un objeto de tipo Dataframe con los datos
    del fichero csv bicimadrid.
    """

    datos = pd.read_csv(file, index_col=0, parse_dates=['unlock_date', 'lock_date'])
    return datos


def delete_nan_rows(df: pd.DataFrame):  # FUNCION PARA BORRAR VALORES NAN DEL DATAFRAME.
    """
    Esta funcion toma como argumento un dataframe,
    para eliminar sus valores nan de las filas. La
     funcion no retorna nada.

    """
    df.dropna(inplace=True)


def float_to_str(df, column):  # FUNCION PARA HACER CAMBIO DE VARIABLE.
    """
    Esta funcion hace un cambio de tipo de dato de float a str.

    :param df: Como primer parametro toma un dataframe.

    :param column: En el segundo parametro se especifica en que
    columna se va a realizar el cambio de tipo de datos.

    :return: La funcion no devuelve nada, sin embargo si
    no se encuentra la columna en el dataframe, la funcion
    no hace nada.
    """

    if df[column] in df:
        df[column].map(lambda x: str(x))
    else:
        print(df[column])


def day_time(df: pd) -> pd:  # FUNCION PREGUNTA 3.
    """
    Esta funcion calcula el tiempo en horas de uso de las
    bicis por cada dia del mes.

    :param df: La funcion recibe como argumento un dataframe.

    :return: La funcion devuelve una serie con indice de
    fecha y el tiempo en horas de uso por fecha.
    """
    return df.groupby(['fecha']).trip_minutes.sum() / 60


def total_usage_day(df: pd) -> pd:  # FUNCION PREGUNTA 5.
    """
        Esta funcion calcula el número total de usos de
        bicicletas por día del mes.

        :param df: La funcion recibe como argumento un dataframe.

        :return: La funcion devuelve una serie con indice de
        fecha y la cantidad de bicis usadas en cada fecha.
        """
    return df.groupby(['fecha']).idBike.size()


def most_popular_stations(df: pd) -> set:  # FUNCION PREGUNTA 7.
    """
    Esta funcion calcula la dirección de las estaciones de
    desbloqueo que a lo largo del mes han tenido un mayor número de viajes.

    :param df: Toma como argumento un dataframe.

    :return: La funcion devuelve un set con las direcciones.
    """

    df1 = df.groupby(['address_unlock']).unlock_station_name.size()
    df2 = df1.sort_values(ascending=False)
    df3 = df2.reset_index()
    direcciones = set(df3.loc[0:2, 'address_unlock'])
    return direcciones


def usage_from_most_popular_station(df: pd) -> int:  # FUNCION PREGUNTA 8.
    df1 = df.groupby(['address_unlock']).unlock_station_name.size()
    df2 = df1.sort_values(ascending=False)
    df3 = df2.reset_index()
    numeros = df3.loc[0:2, 'unlock_station_name']
    return numeros
