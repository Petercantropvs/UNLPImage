#Generador de memes
import PySimpleGUI as sg
import os  #
import json
from src.default.pathing import BASE_PATH

# Necesito que al apretar el botón me mande al repositorio de imágenes, que está en el archivo json de configuración
archivo = open(BASE_PATH+"/src/users-data/archivo_config.json", "r")
datos = json.load(archivo)

ruta_repositorio = datos[0]["ruta"]    #--> Ruta de lo q haya guardado como repositorio de imagenes
ruta_memes = datos[2]["ruta"]          #--> Ruta de lo q haya guardado como  direcotrio de memes para guardar los memes ya hechos


def layout_memes():
    layout = [[sg.Text("Selecciona una imagen:",font = ('latin modern sansquotation', 10))],
             [sg.Input(key='-IMAGEN-'), sg.FileBrowse("Buscar",font = ('latin modern sansquotation', 10), initial_folder=ruta_repositorio)],
             [sg.Text("Escribe un texto:", font = ('latin modern sansquotation', 10))],
             [sg.InputText(key='-TEXTO-')],
             [sg.Text(key='-OUTPUT-')],
             [sg.Submit("Generar",font = ('latin modern sansquotation', 10)), sg.Cancel("Cancelar",font = ('latin modern sansquotation', 10))]]
    return layout

# Crear la ventana
def ventana_meme():
    """
    Esta función permite crear sus propios memes, eligiendo una imagen y escribiendo un texto para pegarlo a la imagen.
    Las imagenes a seleccionar se encuentran en el Resositorio de Imágenes (elegido en la ventana de Configuración),
    y el texto puede ser cualquier cosa. 
    Los memes creados por los usuarios se guardarán en Directorio de memes.
    """
    window = sg.Window('Crea tu meme', layout_memes())
    while True:
        event, values = window.read()  
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            accion = "Entró a generar un meme y no lo generó."
            break

        if event == 'Generar':
            accion = "Generó un meme."
            window['-OUTPUT-'].update('El texto seleccionado es '  + values['-TEXTO-'])

#Es claro que para la versión final aún queda generara la imagen y guardar su contenido en Directorio de memes/collgage según corresponda
#archivo_generado = Save(file_types=(('PNG', '*.png'),), initial_folder=ruta_memes)
    window.close()
    return accion

if __name__ == "__main__":
       ventana_meme()
