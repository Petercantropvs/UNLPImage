import os
import sys
import csv
from datetime import datetime
from src.default.pathing import BASE_PATH

#################################################################################
def function_registo(usuario, accion):
    '''Registra en un csv todas las acciones que hace un usuario.'''
    os.makedirs(os.path.join(BASE_PATH,'src','log'), exist_ok = True)
    hora_actual = datetime.now().strftime('%d-%m-%y %H:%M:%S')


    actividades_anteriores = []         #Para que no sobrescriba lo que ya está guardado en el archivo
    try:
        with open(os.path.join(BASE_PATH,'src','log','users_logs.csv'), 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            actividades_anteriores = list(lector_csv)
    except FileNotFoundError:
        pass
# Agregar la nueva actividad a la lista
    nueva_actividad = [usuario, accion, hora_actual]
    actividades_anteriores.append(nueva_actividad)


    # Escribir todas las actividades en el archivo CSV
    with open(os.path.join(BASE_PATH,'src','log','users_logs.csv'), 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(actividades_anteriores)
