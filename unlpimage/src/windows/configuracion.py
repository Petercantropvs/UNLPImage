import PySimpleGUI as sg
import os  #Lo uso para crear directorios
import json
from src.default.pathing import BASE_PATH


with open(BASE_PATH+"/src/users-data/archivo_config.json", 'r') as config:
    datos = json.load(config)    
    ruta_repositorio = datos[0]["ruta"]    #--> Ruta de lo q haya guardado como repositorio de imagenes
    ruta_collages = datos[1]["ruta"]
    ruta_memes = datos[2]["ruta"]          #--> Ruta de lo q haya guardado como  direcotrio de memes para guardar los memes ya hechos

def layout_configuracion():
    layout = [[sg.Text('Elegí la carpeta donde querés guardar tus memes/collage',font = ('latin modern sansquotation', 15))],
             [sg.Text('Repositorio de imagenes:',font = ('latin modern sansquotation', 10)), sg.Text(ruta_repositorio,font = ('latin modern sansquotation', 8)), sg.FolderBrowse("Seleccionar", font = ('latin modern sansquotation', 10), key='-ruta-repositorio-')],
             [sg.Text('Directorio de collage:', font = ('latin modern sansquotation', 10)), sg.Text(ruta_collages,font = ('latin modern sansquotation', 8)), sg.FolderBrowse("Seleccionar", font = ('latin modern sansquotation', 10), key='-ruta-collage-')],
             [sg.Text('Directorio de memes:', font = ('latin modern sansquotation', 10)), sg.Text(ruta_memes,font = ('latin modern sansquotation', 8)), sg.FolderBrowse("Seleccionar", font = ('latin modern sansquotation', 10), key='-ruta-meme-')],
             [sg.Submit("Guardar", key='-GUARDAR-', font = ('latin modern sansquotation', 10)), sg.Submit('Cerrar', key='-CERRAR-', font=('latin modern sansquotation', 10))]]                    
    return layout


def ventana_configuracion():
    """
    Esta función permite el acceso a la configuración del almacenamiento y manejo de carpetas.
    Los botones permiten elegir cuál será la carpeta de inicio de donde buscar las imágenes (Resositorio de Imágenes),
    y las carpetas donde guardar los memes/collage generados por los usuarios (Directorio de memes/collage).
    Originalmente, no hay ninguna carpeta guardada por default, pùdiendo de estar forma elegir cualquiera en su computadora.
    """
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

            archivo = open(os.getcwd()+"/configuracion/archivo_config.json", "w")
            json.dump(config_datos, archivo)
            archivo.close()   
            window.close()
            break
    return accion


if __name__ == "__main__":
       ventana_configuracion()
