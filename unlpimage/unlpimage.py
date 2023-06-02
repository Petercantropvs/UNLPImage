from src.windows import collage, configuracion, memes, editarperfil, nuevoperfil, ayuda, seleccion_perfil, generar_etiquetas
from src.default.pathing import BASE_PATH
import PySimpleGUI as sg
from src import function_registo
from src.default.setup import *


##################################################################################

def layout():
    """Ventana de Menú prinicpal."""

    col_1 = [[sg.Text('¡Hola, '+perfil+'!', **text_format20)],
            [sg.Image(data=nuevoperfil.get_img_data(BASE_PATH+'/src/users-data/prof_pictures/'+perfil+'.png', first = True), key='-PIC-', enable_events=True, metadata=0 ) ],
            [sg.Button('Editar Perfil',**text_format15, key='-EDIT-', enable_events=True, expand_x=True)],
            ]


    col_2 = [
              [sg.Button('Crear collage', size = (20,1), key = '-COLLAGE-')],
              [sg.Button('Crear meme', size = (20,1),key = '-MEME-')],
              [sg.Button('Generar etiquetas', size = (20,1),key = '-TAGS-')],
              [sg.Button('Salir', size = (20,1),key = '-EXIT-')],]
    

    layout = [[sg.Button('⚙',font=('',15,''), tooltip = 'Configuración', key = '-CONFIG-'),sg.Push() , sg.Button('❔', font=('',15,''), tooltip = 'Ayuda', key = '-HELP-' )],
              [sg.VPush()],
              [sg.Column(col_1, justification='center', pad = ((0,10),(0,20))), sg.Column(col_2, justification='center', pad = ((10,0),(0,20)))],
              [sg.VPush()]]
    return layout


while True:
    perfil, event_seleccion, accion = seleccion_perfil.ventana_seleccionperfil()
    print(accion)
    if accion != None:
        function_registo(perfil, accion)
    if event_seleccion == sg.WIN_CLOSED:
        quit()
    if perfil != None:
        break

window = sg.Window('UNLPimage', layout(), size=window_size_big) #, margins=window_margins90


##################################################################################

while True:
    event, values = window.read()

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
        accion = generar_etiquetas.ventana_etiquetas(perfil)
        # except NameError:
        #     print('entré al nameerror')
        #     generar_etiquetas.ventana_etiquetas()
    if event == sg.WIN_CLOSED or event == '-EXIT-':
        accion = 'Cerró sesión'
        function_registo(perfil, accion)
        break

window.close()
