import io
import os
import PySimpleGUI as sg
from PIL import Image, ImageTk
import json
from src.default.pathing import BASE_PATH
from src.default.data import read_users, check_campos
from src.default.data import get_img_data_profiles as get_img_data
from src.default.setup import *


def layout(): 

    col_1 =[
            [sg.Text('Nuevo Perfil', **text_format25)],
            [sg.Text('Nick o alias:', **text_format15)],
            [sg.Text('(Elija con cuidado, no podrá ser cambiado posteriormente)', font = ('latin modern sansquotation', 8))],
            [sg.Input('', key = '-NICK-', **text_format15, size = (20,10), )],
            [sg.Text('Nombre:', font = ('latin modern sansquotation', 15))],
            [sg.Input('', key = '-NAME-' ,**text_format15, size = (20,10) )],
            [sg.Text('Edad:', font = ('latin modern sansquotation', 15))],
            [sg.Input('', key = '-AGE-' ,**text_format15, size = (20,10))],
            [sg.Text('Género autopercibido:', **text_format15)],
            [sg.OptionMenu(values = (' ','Masculino', 'Femenino', 'No Binarix', 'Trans', 'Prefiero no decirlo'), key = '-GEN-')],
            [sg.Checkbox('Otro', key = '-OTRO-', enable_events=True, **text_format15, size = (20,10))],
            [sg.Input('', key = '-NEW-',**text_format10, size = (31,15), disabled = True)],
            [sg.Ok(font = ('latin modern sansquotation', 15), key = '-OK-'), (sg.Cancel('Cancelar', **text_format15, key = '-CANCEL-' )) ]
            ]
    
    
#images column
    col_2 = [
            [sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','default','perfil_vacio.png'), first = True), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ],
            [sg.Text('Seleccione su foto de perfil ⤴', font = ('latin modern sansquotation', 15), expand_x=True, justification='center')],
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
    ruta_foto = os.path.join(BASE_PATH,'src','default','perfil_vacio.png')
    accion = 'Creo nuevo perfil.'
    window = sg.Window("UNLPImage", layout(), margins=(150, 100))
     
    while True:
        event, user = window.read()
        
        usuarios = read_users()
        match event:
            case '-PIC-':
                ruta_foto = sg.PopupGetFile('Seleccione la imagen de perfil')
                try:
                    window['-PIC-'].update(data=get_img_data(ruta_foto, first = True))
                except AttributeError:
                    ruta_foto = os.path.join(BASE_PATH,'src','default','perfil_vacio.png')
                
            case '-OTRO-' :
                window['-NEW-'].update(value = 'Complete el género', disabled = False, select = True, move_cursor_to = "end")
            case '-OK-':

                ok = check_campos(user,usuarios)
           
                if ok :
                    confirm = sg.popup_yes_no('¿Desea crear el nuevo perfil? Recuerde que el Nick o alias NO podrá ser modificado posteriormente.', title='Guardar imagen')
                    if confirm == 'Yes':
                        with open(os.path.join(BASE_PATH, 'src', 'users-data', 'users.json'), 'w', encoding='utf-8') as u:
                            if user['-OTRO-']:
                                usuarios[user['-NICK-']] = {
                                "nombre": user['-NAME-'],
                                "edad": user['-AGE-'],
                                "genero": user['-NEW-']} 
        
                                json.dump(usuarios, u, ensure_ascii=False)
                                os.makedirs(os.path.join(BASE_PATH,'src','users-data','prof_pictures'), exist_ok = True)
                                Image1 = Image.open(ruta_foto)
    
                                # hago una copia de la imagen así
                                # la original no se ve afectada
                                Image1copy = Image1.copy()
                                Image2 = Image.open(ruta_foto)
                                Image2copy = Image2.copy()
        
                                # pego la imagen dando dimensiones
                                Image1copy.paste(Image2copy, (0, 0))
        
                                # guardo la imagen
                                Image1copy.save(os.path.join(BASE_PATH,'src','users-data','prof_pictures', user['-NICK-']+ '.png'))
                                perfil = user['-NICK-']
                                window.close()
                                u.close()
                                return perfil, accion
                           
        
        
                            else:
                                usuarios[user['-NICK-']] = {
                                "nombre": user['-NAME-'],
                                "edad": user['-AGE-'],
                                "genero": user['-GEN-']} 
    
                                json.dump(usuarios, u)
                                os.makedirs(os.path.join(BASE_PATH,'src','users-data','prof_pictures'), exist_ok = True)
                                Image1 = Image.open(ruta_foto)
    
                                #hago una copia de la imagen así
                                # la original no se ve afectada
                                Image1copy = Image1.copy()
                                Image2 = Image.open(ruta_foto)
                                Image2copy = Image2.copy()
        
                                # pego la imagen dando dimensiones
                                Image1copy.paste(Image2copy, (0, 0))
        
                                # guardo la imagen
                                Image1copy.save(os.path.join(BASE_PATH,'src','users-data','prof_pictures', user['-NICK-']+ '.png'))
                                perfil = user['-NICK-']
                                window.close()
                                u.close()
                                return perfil, accion
                               
                            break
                    if confirm == 'No':
                        continue
                        
        if event == '-CANCEL-' or  event == sg.WIN_CLOSED :
            accion = None
            perfil = None
            window.close()
            return perfil, accion
            break
            
    window.close()

if __name__ == '__main__':
    ventana_nuevoperfil()
