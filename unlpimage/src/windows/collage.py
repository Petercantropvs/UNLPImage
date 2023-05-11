#Genedor de collage:
#Vamos a usar la biblioteca Pillow --> Bilbioteca de manejo de imágenes
import PySimpleGUI as sg
import json
import os


#Necesito ir al repositorio de imágenes, que está en el archivo json de configuración
#archivo = open("../configuracion/archivo_config.json", "r")
#datos = json.load(archivo)

archivo = open(os.getcwd()+'/configuracion/archivo_config.json', 'r')
datos = json.load(archivo)

ruta_repositorio = datos[0]["ruta"]    #--> Ruta de lo q haya guardado como repositorio de imagenes
ruta_memes = datos[1]["ruta"]          #--> Ruta de lo q haya guardado como  direcotrio de collage para guardar los collage ya hechos
archivo.close()
#Además deberá haber una carpeta con los templtes posibles a elegir --> todavía no está en el trabajo, solo emerge la ventana

def layout_collage():
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
    accion1 = "Entró a generar un collage."
    window = sg.Window('Crea tu collage', layout_collage())

    while True:
        event, values = window.read()
        if event == '-SELECCIONAR-IMAGEN-': #'Generar':
            files = values['-SELECCIONAR-IMAGEN-'].split(';')

        if event == '-FINSELECCION-':
            accion2 = "Hizo una selección de imagenes para un collage"
            window['-OUTPUT-'].update('Las imagenes seleccionadas son '  + values['-SELECCIONAR-IMAGEN-'])

        if event == sg.WINDOW_CLOSED or event == 'Cancelar' or event == 'Generar':
            break
    window.close()
    accion = accion1 + " " + accion2
    return accion


    #if event == 'Generar':
        # Split the string of file paths into a list
     #   files = values['-FILES-'].split(';')
      #  print('Selected files:', files)

if __name__ == '__main__':
    ventana_collage()

