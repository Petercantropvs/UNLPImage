import PySimpleGUI as sg
import os  
import json
from src.default.pathing import BASE_PATH, tosave, toload
from src.default.setup import *
from src.default.data import read_config
from src import function_registo


def layout_configuracion():
    ruta_repositorio, ruta_collages, ruta_memes = read_config()
    layout = [[sg.Text('Elegí las carpetas donde querés guardar tus imágenes:\n',**text_format15)],
             [sg.Text('Repositorio de imagenes:',**text_format10), sg.Text(tosave(ruta_repositorio),**text_format8), sg.Push(), sg.FolderBrowse("Seleccionar", **text_format10, key='-ruta-repositorio-')],
             [sg.Text('Directorio de collage:', **text_format10), sg.Text(tosave(ruta_collages),**text_format8), sg.Push(), sg.FolderBrowse("Seleccionar", **text_format10, key='-ruta-collage-')],
             [sg.Text('Directorio de memes:', **text_format10), sg.Text(tosave(ruta_memes),**text_format8), sg.Push(), sg.FolderBrowse("Seleccionar", **text_format10, key='-ruta-meme-')],
             [ sg.Push(), sg.Submit('Cerrar', key='-CERRAR-', **text_format10), sg.Submit("Guardar", key='-GUARDAR-', **text_format10), sg.Push()]]                    
    return layout


def ventana_configuracion(perfil):
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

            if values['-ruta-repositorio-'] != '':
                ruta_repositorio = values['-ruta-repositorio-']
            if values['-ruta-collage-'] != '':
                ruta_collages = values['-ruta-collage-']
            if values['-ruta-meme-'] != '':
                ruta_memes = values['-ruta-meme-']
            
            ruta_repositorio =  tosave(ruta_repositorio)
            ruta_collages = tosave(ruta_collages)
            ruta_memes = tosave(ruta_memes)
            config_datos = [{"nombre": "Repositorio", "ruta": ruta_repositorio}, {"nombre": "Collage", "ruta": ruta_collages}, {"nombre": "Memes", "ruta": ruta_memes}]
            accion = "Entró a ventana de configuracion y cambió las rutas"

            archivo = open(os.path.join(BASE_PATH,'src', 'users-data','archivo_config.json'), "w")
            function_registo(perfil, accion)
            json.dump(config_datos, archivo)
            archivo.close()   
            window.close()
            break
    #return accion


if __name__ == "__main__":
       ventana_configuracion()
