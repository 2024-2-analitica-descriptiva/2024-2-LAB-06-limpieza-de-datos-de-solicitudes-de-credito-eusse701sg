"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    sol_cred = pd.read_csv('files/input/solicitudes_de_credito.csv', sep=';', index_col=0)
    sol_cred.dropna(inplace=True)

    sol_cred['sexo'] = sol_cred['sexo'].str.lower()

    sol_cred['tipo_de_emprendimiento'] = sol_cred['tipo_de_emprendimiento'].str.lower()
    sol_cred['tipo_de_emprendimiento'] = sol_cred['tipo_de_emprendimiento'].str.strip()

    sol_cred['barrio'] = sol_cred['barrio'].str.lower()
    sol_cred['barrio'] = sol_cred['barrio'].str.replace("_", " ")
    sol_cred['barrio'] = sol_cred['barrio'].str.replace("-", " ")

    sol_cred['idea_negocio'] = sol_cred['idea_negocio'].str.lower()
    sol_cred['idea_negocio'] = sol_cred['idea_negocio'].str.replace("_", " ")
    sol_cred['idea_negocio'] = sol_cred['idea_negocio'].str.replace("-", " ")
    sol_cred['idea_negocio'] = sol_cred['idea_negocio'].str.strip()

    sol_cred['monto_del_credito'] = sol_cred['monto_del_credito'].str.strip()
    sol_cred['monto_del_credito'] = sol_cred['monto_del_credito'].str.replace("$","")
    sol_cred['monto_del_credito'] = sol_cred['monto_del_credito'].str.replace(",","")
    sol_cred['monto_del_credito'] = sol_cred['monto_del_credito'].str.replace(".00","")
    sol_cred['monto_del_credito'] = sol_cred['monto_del_credito'].astype(int)

    sol_cred['línea_credito'] = sol_cred['línea_credito'].str.replace("_", " ")
    sol_cred['línea_credito'] = sol_cred['línea_credito'].str.replace("-", " ")
    sol_cred['línea_credito'] = sol_cred['línea_credito'].str.lower()
    sol_cred['línea_credito'] = sol_cred['línea_credito'].str.strip()

    sol_cred['fecha_homologada'] = pd.to_datetime(sol_cred['fecha_de_beneficio'], dayfirst=True, errors='coerce')
    no_identificadas = sol_cred['fecha_homologada'].isnull()
    sol_cred.loc[no_identificadas, 'fecha_homologada'] = pd.to_datetime(sol_cred.loc[no_identificadas, 'fecha_de_beneficio'], format="%Y/%m/%d", errors='coerce')
    sol_cred.drop(columns='fecha_de_beneficio', inplace=True)
    sol_cred.rename(columns={'fecha_homologada':'fecha_de_beneficio'}, inplace=True)

    sol_cred.drop_duplicates(inplace=True)

    output_directory = os.path.join('files', 'output')
    output_file = os.path.join(output_directory, 'solicitudes_de_credito.csv')
    os.makedirs(output_directory, exist_ok=True)
    sol_cred.to_csv(output_file, sep=';')

    return

pregunta_01()