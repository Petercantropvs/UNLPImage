from src.windows import collage, configuracion, memes, editarperfil, nuevoperfil, ayuda, seleccion_perfil, generar_etiquetas
from src.default.pathing import BASE_PATH
import PySimpleGUI as sg
import json
from PIL import Image, ImageTk
import os
import sys, inspect
import csv
from datetime import datetime
from src.default.data import lectura
from src import function_registo

sg.theme('light green 3')

#Defino las fuentes de las ventanas
text_format10 = {'font' : ('latin modern sansquotation', 10)}
text_format15 = {'font' : ('latin modern sansquotation', 15)}
text_format25 = {'font' : ('latin modern sansquotation', 25)}
text_format20 = {'font' : ('latin modern sansquotation', 20)}

# Defino el tamaño de laa ventanas
window_size_grande = (600, 500)
window_margins150 = (150, 100)
window_margins90 = (90, 75)


##################################################################################

err = b'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'
def layout():
    """Este primer layout abre la ventana de Menú prinicpal, una vez q entrás a tu perfil"""

    col_1 = [[sg.Text('¡Hola, '+perfil+'!', **text_format20)],
            [sg.Image(data=nuevoperfil.get_img_data(BASE_PATH+'/src/users-data/prof_pictures/'+perfil+'.png', first = True), key='-PIC-', enable_events=True, metadata=0 ) ],
            [sg.Button('Editar Perfil',**text_format15, key='-EDIT-', enable_events=True )],
            [sg.Button('Ayuda', key = '-HELP-' ), sg.Button('Configuracion', key = '-CONFIG-')]
            ]


    col_2 = [
              [sg.Button('Crear collage', key = '-COLLAGE-')],
              [sg.Button('Crear meme', key = '-MEME-')],
              [sg.Button('Generar etiquetas', key = '-TAGS-')],
              [sg.Button('Salir', key = '-EXIT-')],]
    

    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout

with open(BASE_PATH+"/src/users-data/archivo_config.json", 'r') as config:
    datos = json.load(config)    
    ruta_repositorio = datos[0]["ruta"]    #--> Ruta de lo q haya guardado como repositorio de imagenes
    ruta_collages = datos[1]["ruta"]
    ruta_memes = datos[2]["ruta"]          #--> Ruta de lo q haya guardado como  direcotrio de memes para guardar los memes ya hechos



#seleccion_perfil.ventana_eleccionperfil()
while True:
    perfil, event_seleccion = seleccion_perfil.ventana_seleccionperfil()
    if event_seleccion == sg.WIN_CLOSED:
        quit()
    if perfil != None:
        break
#window = sg.Window('UNLPimage', layout(), margins=(90, 75))
window = sg.Window('UNLPimage', layout(), margins=window_margins90, size=window_size_grande)




##################################################################################
while True:
    event, values = window.read()

    #print(event, values)

    if event == '-CONFIG-':
        accion = configuracion.ventana_configuracion()
        function_registo(perfil, accion)
    if event == '-PIC-' or event == '-EDIT-':
        accion = editarperfil.ventana_editarperfil(perfil)
        window['-PIC-'].update(data=nuevoperfil.get_img_data(BASE_PATH+'/src/users-data/prof_pictures/'+perfil+'.png', first = True))
        function_registo(perfil, accion)
    elif event == '-COLLAGE-':
        accion = collage.ventana_collage()
        function_registo(perfil, accion)
    elif event == '-HELP-':
        accion = ayuda.ventana_ayuda() 
        function_registo(perfil, accion)
    elif event == '-MEME-':
        accion = memes.ventana_meme()
        function_registo(perfil, accion)

    elif event == '-TAGS-':
        # try:
        accion = generar_etiquetas.ventana_etiquetas(ruta_repositorio)
        # except NameError:
        #     print('entré al nameerror')
        #     generar_etiquetas.ventana_etiquetas()
    if event == sg.WIN_CLOSED or event == '-EXIT-':
        break

window.close()



window.close()
