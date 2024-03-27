"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    #df["sexo"] = df["sexo"].str.lower()
    df = df.map(lambda x: x.lower() if isinstance(x, str) else x)
    df = df.dropna()
    def convertir_formato(fecha):
        fecha_objeto = datetime.strptime(fecha, '%Y/%m/%d')
        return fecha_objeto.strftime('%d/%m/%Y')

    # Función para aplicar la conversión en una columna del DataFrame
    def convertir_columna(columna):
        partes = columna.split('/')
        if len(partes) == 3:
            try:
                dia = int(partes[0])
                mes = int(partes[1])
                año = int(partes[2])
                if 1 <= dia <= 31 and 1 <= mes <= 12 and año > 0:
                    return columna  # Formato DD/MM/YYYY ya está presente
                else:
                     return convertir_formato(columna)
            except ValueError:
                pass
        # Si no está en el formato esperado, convertir a DD/MM/YYYY
       

    # Aplicar la función a la columna 'fechas'
    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(convertir_columna)
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio,dayfirst=True)
    #df.fecha_de_beneficio = df.fecha_de_beneficio.dt.strftime('%d/%m/%Y')
    #df['fecha'] = pd.to_datetime(df['fecha'], format='%y/%m/%d')
    #df = df.dropna()
    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.replace({',': ''}, regex=True)
    df.idea_negocio = df.idea_negocio.replace({'-': ' ','_':' '}, regex=True)
    df.barrio = df.barrio.replace({'-': ' ','_':' '}, regex=True)
    df.línea_credito = df.línea_credito.replace({'-': ' ','_':' '}, regex=True)
    df.monto_del_credito = pd.to_numeric(df.monto_del_credito)
    df.monto_del_credito = df.monto_del_credito.astype(int)
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset=df.columns[1:])

    #
    # Inserte su código aquí
    #
    
    #print(df.fecha_de_beneficio.value_counts())
    #print(df[df.comuna_ciudadano == 4.0])
    return df
#print(clean_data().línea_credito.value_counts())