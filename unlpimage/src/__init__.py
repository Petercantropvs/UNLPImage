import os
import sys
import csv
from datetime import datetime
from src.default.pathing import BASE_PATH

#################################################################################
def function_registo(usuario, accion,values = None,texts = None):
    '''Registra en un csv todas las acciones que hace un usuario.
    values debe mostrar los nombres de las imagenes que se usaron en el meme o en el collage en formato lista [a,b,c]
    texts debe mostrar los textos que se incluyeron tanto en el collage como en el meme en formato string.'''

    os.makedirs(os.path.join(BASE_PATH,'src','log'), exist_ok = True)
    hora_actual = datetime.now().strftime('%d-%m-%y %H:%M:%S')


    actividades_anteriores = []         #Para que no sobrescriba lo que ya está guardado en el archivo
    try:
        with open(os.path.join(BASE_PATH,'src','log','users_logs.csv'), 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            actividades_anteriores = list(lector_csv)
    except FileNotFoundError:
        with open(os.path.join(BASE_PATH,'src','log','users_logs.csv'), 'x', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['User', 'Action', 'Time', 'Values', 'Texts'])
            actividades_anteriores.append(['User', 'Action', 'Time', 'Values', 'Texts'])

# Agregar la nueva actividad a la lista
    nueva_actividad = [usuario, accion, hora_actual, values, texts]
    actividades_anteriores.append(nueva_actividad)


    # Escribir todas las actividades en el archivo CSV
    with open(os.path.join(BASE_PATH,'src','log','users_logs.csv'), 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(actividades_anteriores)
