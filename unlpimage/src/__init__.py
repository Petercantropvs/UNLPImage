import os
import sys
import csv
from datetime import datetime

BASE_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

#################################################################################
def function_registo(usuario, accion):
    hora_actual = datetime.now().strftime('%d-%m-%y %H:%M:%S')


    actividades_anteriores = []         #Para que no sobrescriba lo que ya está guardado en el archivo
    try:
        with open(BASE_PATH+"/src/log/users_logs.csv", 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            actividades_anteriores = list(lector_csv)
    except FileNotFoundError:
        pass
# Agregar la nueva actividad a la lista
    nueva_actividad = [usuario, accion, hora_actual]
    actividades_anteriores.append(nueva_actividad)


    # Escribir todas las actividades en el archivo CSV
    with open(BASE_PATH+"/src/log/users_logs.csv", 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(actividades_anteriores)
