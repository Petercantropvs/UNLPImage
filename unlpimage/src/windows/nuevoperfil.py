import io
import os
import PySimpleGUI as sg
from PIL import Image, ImageTk
import json
from src.default.pathing import BASE_PATH
from src.default.data import read_users
from src.default.data import get_img_data_profiles as get_img_data
from src.default.setup import *


def layout(): 

    col_1 =[
            [sg.Text('Nuevo Perfil', **text_format25)],
            [sg.Text('Nick o alias', **text_format15)],
            [sg.Text('(Elija con cuidado, no podrá ser cambiado posteriormente)', font = ('latin modern sansquotation', 8))],
            [sg.Input('', key = '-NICK-', **text_format15, size = (10,10), )],
            [sg.Text('Nombre', font = ('latin modern sansquotation', 15))],
            [sg.Input('', key = '-NAME-' ,**text_format15, size = (10,10) )],
            [sg.Text('Edad', font = ('latin modern sansquotation', 15))],
            [sg.Input('', key = '-AGE-' ,**text_format15, size = (10,10))],
            [sg.Text('Género autopercibido', **text_format15)],
            [sg.OptionMenu(values = (' ','Masculino', 'Femenino', 'No Binarix', 'Trans', 'Prefiero no decirlo'), key = '-GEN-')],
            [sg.Checkbox('Otro', key = '-OTRO-', enable_events=True, **text_format15, size = (10,10))],
            [sg.Input('', key = '-NEW-',**text_format10, size = (18,15), disabled = True)],
            [sg.Ok(font = ('latin modern sansquotation', 15), key = '-OK-'), (sg.Cancel('Cancelar', **text_format15, key = '-CANCEL-' )) ]
            ]
    
    
#images column
    col_2 = [
            [sg.Image(data=get_img_data(BASE_PATH+'/src/default/perfil_vacio.png', first = True), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ],
            [sg.Text('Seleccione su foto de perfil', font = ('latin modern sansquotation', 15))],
            ]
    
    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout

def ventana_nuevoperfil():
    """ 
    Esta función permite crear un nuevo perfil. El usuario puede seleccionar nicknme, nombre, edad, género y la foto de perfil.
    La función no permite que se repitan los nicknames (los cuales además, no podrán ser modificados).
    La función también permite elegir género fuera del binario e incluso no declararlo en caso de asi desearlo.
    
    Para trabajar con las imágenes, se importa el paquete pillow, y guardamos las rutas de imágenes y datos usando un modulo.
    Este archivo de rutas es también una funcon, importada como "lectura".
    """
    ruta_foto = BASE_PATH+'/src/default/perfil_vacio.png'
    accion = 'Creo nuevo perfil.'
    window = sg.Window("UNLPImage", layout(), margins=(150, 100))
     
    while True:
        event, user = window.read()
        
        usuarios = read_users()
   
        if event == '-PIC-':
            ruta_foto = sg.PopupGetFile('Seleccione la imagen de perfil')
            try:
                window['-PIC-'].update(data=get_img_data(ruta_foto, first = True))
            except AttributeError:
                ruta_foto = BASE_PATH+'/src/default/perfil_vacio.png'
                
        if event == '-OTRO-' :
            window['-NEW-'].update(value = 'Complete el género', disabled = False, select = True, move_cursor_to = "end")
        if event == '-OK-':
            if (user['-NICK-'] == '') or (user['-NAME-'] == '') or (user['-AGE-'] == '' ) or (user['-OTRO-'] == False and user['-GEN-'] == '') or (user['-OTRO-'] == True and user['-NEW-'] == ''):      
                sg.popup_ok('Todos los campos son obligatorios', title='Error!')
    
            if str(user['-NICK-']).lower() in str(usuarios).lower():
                if user['-NICK-'] != '':
                    sg.popup_ok('El nick o alias ya está utilizado', title='Error!')   
            else:

                try:
                    age=int(user['-AGE-'])
                except ValueError:
                    sg.popup_ok('Ingrese un número para la edad', title='Error!')   
                else:
                    with open(BASE_PATH+'/src/users-data/users.json', 'w') as u:
                        if user['-OTRO-']:
                           usuarios[user['-NICK-']] = {
                           "nombre": user['-NAME-'],
                           "edad": user['-AGE-'],
                           "genero": user['-NEW-']} 
    
                           json.dump(usuarios, u)
                           os.makedirs(BASE_PATH+'/src/users-data/prof_pictures/', exist_ok = True)
                           Image1 = Image.open(ruta_foto)

                           # hago una copia de la imagen así
                           # la original no se ve afectada
                           Image1copy = Image1.copy()
                           Image2 = Image.open(ruta_foto)
                           Image2copy = Image2.copy()
     
                           # pego la imagen dando dimensiones
                           Image1copy.paste(Image2copy, (0, 0))
     
                           # guardo la imagen
                           Image1copy.save(BASE_PATH+'/src/users-data/prof_pictures/'+ user['-NICK-']+ '.png')
                           perfil = user['-NICK-']
                           window.close()
                           u.close()
                           return perfil
                           
    
    
                        else:
                           usuarios[user['-NICK-']] = {
                           "nombre": user['-NAME-'],
                           "edad": user['-AGE-'],
                           "genero": user['-GEN-']} 

                           json.dump(usuarios, u)
                           os.makedirs(BASE_PATH+'/src/users-data/prof_pictures', exist_ok = True)
                           Image1 = Image.open(ruta_foto)

                           #hago una copia de la imagen así
                           # la original no se ve afectada
                           Image1copy = Image1.copy()
                           Image2 = Image.open(ruta_foto)
                           Image2copy = Image2.copy()
     
                           # pego la imagen dando dimensiones
                           Image1copy.paste(Image2copy, (0, 0))
     
                           # guardo la imagen
                           Image1copy.save(BASE_PATH+'/src/users-data/prof_pictures/'+ user['-NICK-']+ '.png')
                           perfil = user['-NICK-']
                           window.close()
                           u.close()
                           return perfil
                           
                        break
                        
        if event == '-CANCEL-' or  event == sg.WIN_CLOSED :
            break
            
    window.close()

if __name__ == '__main__':
    ventana_nuevoperfil()
