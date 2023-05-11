import PySimpleGUI as sg
import os  #Lo uso para crear directorios
import json


with open(os.getcwd()+"/configuracion/archivo_config.json", 'r') as config:
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

#El repositorio de imágenes será la carpeta de donde elegiremos las imagenes para hacer los memes y collages.
#Los directorios es elegir la carpeta a donde queremos los guarde.

def ventana_configuracion():
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

           # print(f"{elemento} comienza con {ka}")

            #print (config_datos)
            archivo = open(os.getcwd()+"/configuracion/archivo_config.json", "w")
            json.dump(config_datos, archivo)
            archivo.close()   
            window.close()
            break
    return accion


#configuracion ruta_carpeta.json  #Creo el archivo json con esos datos

if __name__ == "__main__":
       ventana_configuracion()
