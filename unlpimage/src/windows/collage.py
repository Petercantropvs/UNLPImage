#Genedor de collage:
import PySimpleGUI as sg
import json
import os
from src.default.pathing import BASE_PATH
from src.default.data import read_config


def layout_collage():
    ruta_repositorio, ruta_collages, ruta_memes = read_config()
    layout = [[sg.Text('Selecciona las imágenes que quieres agregar al collage',font = ('latin modern sansquotation', 10))],
             [sg.Input(), sg.FilesBrowse("Seleccionar imagen", key='-SELECCIONAR-IMAGEN-',font = ('latin modern sansquotation', 10), initial_folder=ruta_repositorio, file_types=(("ALL Files", "*.*"),)), sg.Button('Finalizar',key='-FINSELECCION-',font = ('latin modern sansquotation', 10)) ],
             [sg.Text('Selecciona el template para el nuevo collage',font = ('latin modern sansquotation', 10))],
             [sg.Input(), sg.FilesBrowse("Seleccionar template",font = ('latin modern sansquotation', 10)) ],
            #Una vez generados los templates, hacemos la ruta, pues falta crear esta carpeta
            #[sg.Input(), sg.FilesBrowse(initial_folder=template_ruta, file_types=('*.png', '*.jpg'),)],
             [sg.Text(key='-OUTPUT-')],
             [sg.Button('Generar',font = ('latin modern sansquotation', 10)), sg.Button('Cancelar',font = ('latin modern sansquotation', 10))]]
    return layout

def ventana_collage():
    """
    Esta función permite crear tus propios collages, eligiendo varias imágenes y cierto template de collage.
    Las imagenes a seleccionar se encuentran en el Resositorio de Imágenes (elegido en la ventana de Configuración),
    y los templates en la carpeta de default (proximamente....). 
    Los collages creados por los usuarios se guardarán en Directorio de collages.
    """
    window = sg.Window('Crea tu collage', layout_collage())

    while True:
        event, values = window.read()
        if event == '-SELECCIONAR-IMAGEN-': #'Generar':
            files = values['-SELECCIONAR-IMAGEN-'].split(';')

        if event == '-FINSELECCION-':
            window['-OUTPUT-'].update('Las imagenes seleccionadas son '  + values['-SELECCIONAR-IMAGEN-'])

        if event == 'Generar':
            accion = "Creó un collage. "
            break

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            accion = "Entró a generar un collage, pero no lo generó. "
            break
    window.close()
    return accion


if __name__ == '__main__':
    ventana_collage()

