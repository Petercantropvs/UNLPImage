import PySimpleGUI as sg
import os  #Lo uso para crear directorios
import json

nombre_directorio1 = "Directorio de collage"
nombre_directorio2 = "Directorio de memes"
nombre_directorio3 = "Repositorio de imagenes"

# Verifica si el directorio ya existe
if not os.path.exists(nombre_directorio1):
    # Crea el directorio si no existe
    os.mkdir(nombre_directorio1)
    
if not os.path.exists(nombre_directorio2):
    # Crea el directorio si no existe
    os.mkdir(nombre_directorio2)

if not os.path.exists(nombre_directorio3):
    # Crea el directorio si no existe
    os.mkdir(nombre_directorio3)    


def layout_configuracion():
    layout = [[sg.Text('Elegí la carpeta donde querés guardar tus memes/collage',font = ('latin modern sansquotation', 15))],
             [sg.Text('Repositorio de imagenes',font = ('latin modern sansquotation', 10)), sg.FolderBrowse("Seleccionar", font = ('latin modern sansquotation', 10), key='-ruta-repositorio-')],
             [sg.Text('Directorio de collage', font = ('latin modern sansquotation', 10)), sg.FolderBrowse("Seleccionar", font = ('latin modern sansquotation', 10), key='-ruta-collage-')],
             [sg.Text('Directorio de memes', font = ('latin modern sansquotation', 10)), sg.FolderBrowse("Seleccionar", font = ('latin modern sansquotation', 10), key='-ruta-meme-')],
             [sg.Submit("Guardar", font = ('latin modern sansquotation', 10))]]                    
    return layout

#El repositorio de imágenes será la carpeta de donde elegiremos las imagenes para hacer los memes y collages.
#Los directorios es elegir la carpeta a donde queremos los guarde.

def ventana_configuracion():
    window = sg.Window('Configuración',layout_configuracion())

    event, values = window.read()
    window.close()

    ruta_repositorio = values['-ruta-repositorio-']
    ruta_collage = values['-ruta-collage-']
    ruta_memes = values['-ruta-meme-']     
    
    config_datos = [{"nombre": "Repositorio", "ruta": ruta_repositorio}, {"nombre": "Collage", "ruta": ruta_collage}, {"nombre": "Memes", "ruta": ruta_memes}]

    #print (config_datos)
    archivo = open("archivo_config.json", "w")
    json.dump(config_datos, archivo)
    archivo.close()   


#configuracion ruta_carpeta.json  #Creo el archivo json con esos datos

if __name__ == "__main__":
       ventana_configuracion()
