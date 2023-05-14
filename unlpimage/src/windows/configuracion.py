import PySimpleGUI as sg
import os  
import json
from src.default.pathing import BASE_PATH
from src.default.setup import *
from src.default.data import read_config


def layout_configuracion():
    ruta_repositorio, ruta_collages, ruta_memes = read_config()
    layout = [[sg.Text('Elegí la carpeta donde querés guardar tus memes/collage',**text_format15)],
             [sg.Text('Repositorio de imagenes:',**text_format10), sg.Text(ruta_repositorio,**text_format8), sg.FolderBrowse("Seleccionar", **text_format10, key='-ruta-repositorio-')],
             [sg.Text('Directorio de collage:', **text_format10), sg.Text(ruta_collages,**text_format8), sg.FolderBrowse("Seleccionar", **text_format10, key='-ruta-collage-')],
             [sg.Text('Directorio de memes:', **text_format10), sg.Text(ruta_memes,**text_format8), sg.FolderBrowse("Seleccionar", **text_format10, key='-ruta-meme-')],
             [sg.Submit("Guardar", key='-GUARDAR-', **text_format10), sg.Submit('Cerrar', key='-CERRAR-', **text_format10)]]                    
    return layout


def ventana_configuracion():
    """
    Esta función permite el acceso a la configuración del almacenamiento y manejo de carpetas.
    Los botones permiten elegir cuál será la carpeta de inicio de donde buscar las imágenes (Resositorio de Imágenes),
    y las carpetas donde guardar los memes/collage generados por los usuarios (Directorio de memes/collage).
    Originalmente, no hay ninguna carpeta guardada por default, pùdiendo de estar forma elegir cualquiera en su computadora.
    """
    ruta_repositorio, ruta_collages, ruta_memes = read_config()
    accion = "Entró a ventana de configuracion y no realizó cambios"
    window = sg.Window('Configuración',layout_configuracion())


    while True: 
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == '-CERRAR-':
            window.close()
            break
        if event == '-GUARDAR-':

            ruta_repositorio = values['-ruta-repositorio-']
            ruta_collage = values['-ruta-collage-']
            ruta_memes = values['-ruta-meme-']     
            
            config_datos = [{"nombre": "Repositorio", "ruta": ruta_repositorio}, {"nombre": "Collage", "ruta": ruta_collage}, {"nombre": "Memes", "ruta": ruta_memes}]
            accion = "Entró a ventana de configuracion y generó cambió las rutas"

            archivo = open(os.path.join(BASE_PATH,'src', 'users-data','archivo_config.json'), "w")

            json.dump(config_datos, archivo)
            archivo.close()   
            window.close()
            break
    return accion


if __name__ == "__main__":
       ventana_configuracion()
