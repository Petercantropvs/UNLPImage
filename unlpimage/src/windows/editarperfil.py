import io
import os
import PySimpleGUI as sg
from PIL import Image, ImageTk
import json
from src.default.pathing import BASE_PATH
from src.default.data import read_users
from src.default.data import get_img_data_profiles as get_img_data
from src.default.setup import *
from src import function_registo
    


def layout(perfil):
    datos=read_users() 

    col_1 =[
            [sg.Text('Editar Perfil', **text_format25)],
            [sg.Text('Nick o alias:', **text_format15)],
            [sg.Input(perfil, key = '-NICK-', **text_format15, size = (20,10), disabled = True )],
            [sg.Text('Nombre:', **text_format15)],
            [sg.Input(datos[perfil]['nombre'], key = '-NAME-' ,**text_format15, size = (20,10) )],
            [sg.Text('Edad:', **text_format15)],
            [sg.Input(datos[perfil]['edad'], key = '-AGE-' ,**text_format15, size = (20,10))],
            [sg.Text('Género autopercibido:', **text_format15)],
            [sg.OptionMenu(default_value= datos[perfil]['genero'], values = (' ','Masculino', 'Femenino', 'No Binarix', 'Trans', 'Prefiero no decirlo'), key = '-GEN-')],
            [sg.Checkbox('Otro', key = '-OTRO-', enable_events=True, **text_format15, size = (10,10))],
            [sg.Input('', key = '-NEW-',font = ('latin modern sansquotation', 10), size = (31,15), disabled = True)],
            [sg.Ok(**text_format15, key = '-OK-'), (sg.Cancel('Cancelar', **text_format15, key = '-CANCEL-' )) ]
            ]
    
    
#images column
    col_2 = [
            [sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','users-data','prof_pictures',perfil+'.png'), first = True), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ],
            [sg.Text('Seleccione su foto de perfil ⤴',**text_format15, expand_x=True, justification='center')],
            ]
    
    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout

def ventana_editarperfil(perfil):
    print(perfil)
    """ 
    Esta función permite editar un perfil ya creado anteriormente, pudiendo cambiar nombre, edad, género y la foto de perfil.
    Recordar que el nickname no podrá ser modificado.
    Los datos se actualizarán en el archivo a partir de la función lectura (importada), y la imagen seleccionada cambiará de rutas.
    """
    ruta_foto = os.path.join(BASE_PATH,'src','users-data','prof_pictures',perfil+'.png')
    accion = "El usuario editó su perfil."
    window = sg.Window('UNLPimage - Editar Perfil', layout(perfil), margins=(150, 100))
     
    i=0
    while True:
        event, user = window.read()
        
        usuarios = read_users()
        i= i+1

        if event == '-PIC-':
            ruta_foto = sg.PopupGetFile('Seleccione la imagen de perfil')
            try:
                window['-PIC-'].update(data=get_img_data(ruta_foto, first = True))
            except AttributeError:
                ruta_foto = os.path.join(BASE_PATH,'src','users-data','prof_pictures',perfil+'.png')
                
        if event == '-OTRO-' :
            window['-NEW-'].update(value = 'Complete el género', disabled = False, select = True, move_cursor_to = "end")
        if event == '-OK-':
            if (user['-NICK-'] == '') or (user['-NAME-'] == '') or (user['-AGE-'] == '' ) or (user['-OTRO-'] == False and user['-GEN-'] == '') or (user['-OTRO-'] == True and user['-NEW-'] == ''):      
                sg.popup_ok('Todos los campos son obligatorios', title='Error!')
     
            else:

                try:
                    age=int(user['-AGE-'])
                except ValueError:
                    sg.popup_ok('Ingrese un número para la edad', title='Error!')   
                else:
                    with open(os.path.join(BASE_PATH, 'src', 'users-data', 'users.json'), 'w') as u:
                        if user['-OTRO-']:

                           usuarios[user['-NICK-']]['nombre'] = user['-NAME-']
                           usuarios[user['-NICK-']]['edad'] = user['-AGE-']
                           usuarios[user['-NICK-']]['genero'] = user['-NEW-']

                           
                           json.dump(usuarios, u)
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
                           Image1copy.save( os.path.join(BASE_PATH,'src','users-data','prof_pictures', user['-NICK-']+ '.png'))
                           window.close()
                           function_registo(perfil, accion)
                          # return accion
    
    
                        else:
                           usuarios[user['-NICK-']]['nombre'] = user['-NAME-']
                           usuarios[user['-NICK-']]['edad'] = user['-AGE-']
                           usuarios[user['-NICK-']]['genero'] = user['-GEN-']

                           #datos.append(usuarios)
                           #json.dump(datos, u)
                           json.dump(usuarios, u)
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
                           Image1copy.save( os.path.join(BASE_PATH,'src','users-data','prof_pictures', user['-NICK-']+ '.png'))
                           window.close()
                           function_registo(perfil, accion)
                           #return accion
                        break
        if event == '-CANCEL-' or  event == sg.WIN_CLOSED :
          #  accion = "El usuario entro a editar perfil pero no lo editó."
            window.close()
            #return accion
            break
            
    window.close()

if __name__ == '__main__':
    ventana_editarperfil(perfil)
