#Genedor de collage:
#Vamos a usar la biblioteca Pillow --> Bilbioteca de manejo de imágenes
import PySimpleGUI as sg
import os  
import json


#Necesito ir al repositorio de imágenes, que está en el archivo json de configuración
archivo = open("archivo_config.json")
datos = json.load(archivo)

ruta_repositorio = datos[0]["ruta"]    #--> Ruta de lo q haya guardado como repositorio de imagenes
ruta_memes = datos[1]["ruta"]          #--> Ruta de lo q haya guardado como  direcotrio de collage para guardar los collage ya hechos

#Además deberá haber una carpeta con los templtes posibles a elegir --> todavía no está en el trabajo, solo emerge la ventana

layout = [[sg.Text('Selecciona las imágenes que quieres agregar al collage',font = ('latin modern sansquotation', 10))],
         [sg.Input(), sg.FileBrowse("Seleccionar imagen", key='-Imagen1',font = ('latin modern sansquotation', 10), initial_folder=ruta_repositorio, file_types=(("ALL Files", "*.*"),))],
         [sg.Input(), sg.FileBrowse("Seleccionar imagen", key='-Imagen2',font = ('latin modern sansquotation', 10), initial_folder=ruta_repositorio, file_types=(("ALL Files", "*.*"),))], 
         [sg.Input(), sg.FileBrowse("Seleccionar imagen", key='-Imagen3',font = ('latin modern sansquotation', 10), initial_folder=ruta_repositorio, file_types=(("ALL Files", "*.*"),))], 
         [sg.Text('Selecciona el template para el nuevo collage',font = ('latin modern sansquotation', 10))],
         [sg.Input(), sg.FileBrowse("Seleccionar template",font = ('latin modern sansquotation', 10)) ],
         #Una vez generados los templates, hacemos la ruta, pues falta crear esta carpeta
         #[sg.Input(), sg.FilesBrowse(initial_folder=template_ruta, file_types=('*.png', '*.jpg'),)],
         [sg.Button('Generar',font = ('latin modern sansquotation', 10)), sg.Button('Cancelar',font = ('latin modern sansquotation', 10))]]

window = sg.Window('Crea tu collage', layout)
#event, values = window.read()
#window.close()


# file_types=(('Imágenes', '*.png;*.jpg'),))],
#key= 'algop', mulpliple_files = True
#(file_types=(("xlsx Files", "*.xlsx")

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break

    if event == 'Generar':
        print("Imagen1= ", values['-Imagen1'],values['-Imagen2'],values['-Imagen3'])
        window.close()


    #if event == 'Generar':
        # Split the string of file paths into a list
     #   files = values['-FILES-'].split(';')
      #  print('Selected files:', files)


