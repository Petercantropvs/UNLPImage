import io
import os
import PySimpleGUI as sg
from PIL import Image, ImageTk
import json
from src.default.pathing import BASE_PATH
from src.default.data import lectura


def get_img_data(f, first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img = img.resize((200,200), Image.ANTIALIAS)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)


#datos = json.load(u)
#print(datos)
    
#load images into elements

def layout(perfil):
    datos=lectura() #img 1 attributes list
    #image_elem1 = sg.Image(data=get_img_data(os.getcwd()+'/../nuevo_perfil/prof_pictures/perfil_vacio.png', first=True))
    col_1 =[
            [sg.Text('Editar Perfil', font = ('latin modern sansquotation', 25))],
            [sg.Text('Nick o alias', font = ('latin modern sansquotation', 15))],
            [sg.Input(perfil, key = '-NICK-', font = ('latin modern sansquotation', 15), size = (10,10), disabled = True )],
            [sg.Text('Nombre', font = ('latin modern sansquotation', 15))],
            [sg.Input(datos[perfil]['nombre'], key = '-NAME-' ,font = ('latin modern sansquotation', 15), size = (10,10) )],
            [sg.Text('Edad', font = ('latin modern sansquotation', 15))],
            [sg.Input(datos[perfil]['edad'], key = '-AGE-' ,font = ('latin modern sansquotation', 15), size = (10,10))],
            [sg.Text('Género autopercibido', font = ('latin modern sansquotation', 15))],
            [sg.OptionMenu(default_value= datos[perfil]['genero'], values = (' ','Masculino', 'Femenino', 'No Binarix', 'Trans', 'Prefiero no decirlo'), key = '-GEN-')],
            [sg.Checkbox('Otro', key = '-OTRO-', enable_events=True, font = ('latin modern sansquotation', 15), size = (10,10))],
            [sg.Input('', key = '-NEW-',font = ('latin modern sansquotation', 10), size = (18,15), disabled = True)],
            [sg.Ok(font = ('latin modern sansquotation', 15), key = '-OK-'), (sg.Cancel('Cancelar', font = ('latin modern sansquotation', 15), key = '-CANCEL-' )) ]
            ]
    
    
#images column
    col_2 = [
            [sg.Image(data=get_img_data(BASE_PATH+'/src/users-data/prof_pictures/'+perfil+'.png', first = True), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ],
            [sg.Text('Seleccione su foto de perfil', font = ('latin modern sansquotation', 15))],
            ]
    
    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout

def ventana_editarperfil(perfil):
    print(perfil)
    ruta_foto = BASE_PATH+'/src/users-data/prof_pictures/'+perfil+'.png'
    
    window = sg.Window("UNLPImage", layout(perfil), margins=(150, 100))
     
    i=0
    while True:
        event, user = window.read()
        
        usuarios = lectura()
        i= i+1
        print(i)
        print(event)
        if event == '-PIC-':
            ruta_foto = sg.PopupGetFile('Seleccione la imagen de perfil')
            try:
                window['-PIC-'].update(data=get_img_data(ruta_foto, first = True))
            except AttributeError:
                ruta_foto = BASE_PATH+'/src/users-data/prof_pictures/'+perfil+'.png'
                
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
                    with open(BASE_PATH+'/src/users-data/users.json', 'w') as u:
                        if user['-OTRO-']:

                           usuarios[user['-NICK-']]['nombre'] = user['-NAME-']
                           usuarios[user['-NICK-']]['edad'] = user['-AGE-']
                           usuarios[user['-NICK-']]['genero'] = user['-NEW-']

                           #datos= usuarios
                           #json.dump(datos, u)
                           json.dump(usuarios, u)
                           os.makedirs( BASE_PATH+'/src/users-data/prof_pictures', exist_ok = True)
                           Image1 = Image.open(ruta_foto)
                           # make a copy the image so that the
                           # original image does not get affected
                           Image1copy = Image1.copy()
                           Image2 = Image.open(ruta_foto)
                           Image2copy = Image2.copy()
     
                           # paste image giving dimensions
                           Image1copy.paste(Image2copy, (0, 0))
     
                           # save the image
                           Image1copy.save( BASE_PATH+'/src/users-data/prof_pictures/'+ user['-NICK-']+ '.png')
    
    
                        else:
                           usuarios[user['-NICK-']]['nombre'] = user['-NAME-']
                           usuarios[user['-NICK-']]['edad'] = user['-AGE-']
                           usuarios[user['-NICK-']]['genero'] = user['-GEN-']

                           #datos.append(usuarios)
                           #json.dump(datos, u)
                           json.dump(usuarios, u)
                           os.makedirs( BASE_PATH+'/src/users-data/prof_pictures', exist_ok = True)
                           Image1 = Image.open(ruta_foto)
                           # make a copy the image so that the
                           # original image does not get affected
                           Image1copy = Image1.copy()
                           Image2 = Image.open(ruta_foto)
                           Image2copy = Image2.copy()
     
                           # paste image giving dimensions
                           Image1copy.paste(Image2copy, (0, 0))
     
                           # save the image
                           Image1copy.save( BASE_PATH+'/src/users-data/prof_pictures/'+ user['-NICK-']+ '.png')
                        break
        if event == '-CANCEL-' or  event == sg.WIN_CLOSED :
            break
            
    window.close()

if __name__ == '__main__':
    ventana_editarperfil(perfil)
