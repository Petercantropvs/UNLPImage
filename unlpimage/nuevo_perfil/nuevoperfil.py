import io
import os
import PySimpleGUI as sg
from PIL import Image, ImageTk
import json


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
try:
    archivo = open('users.json', 'r')
    datos = json.load(archivo)
except json.decoder.JSONDecodeError:
    datos = []
print(datos)


#datos = json.load(u)
#print(datos)
    
#load images into elements

def layout(): #img 1 attributes list
    image_elem1 = sg.Image(data=get_img_data('perfil_vacio.png', first=True))
    col_1 =[
            [sg.Text('Nuevo Perfil', font = ('latin modern sansquotation', 25))],
            [sg.Text('Nick o alias', font = ('latin modern sansquotation', 15))],
            [sg.Input('', key = '-NICK-', font = ('latin modern sansquotation', 15), size = (10,10), )],
            [sg.Text('Nombre', font = ('latin modern sansquotation', 15))],
            [sg.Input('', key = '-NAME-' ,font = ('latin modern sansquotation', 15), size = (10,10) )],
            [sg.Text('Edad', font = ('latin modern sansquotation', 15))],
            [sg.Input('', key = '-AGE-' ,font = ('latin modern sansquotation', 15), size = (10,10))],
            [sg.Text('Género autopercibido', font = ('latin modern sansquotation', 15))],
            [sg.OptionMenu(values = (' ','Masculino', 'Femenino', 'No Binarix', 'Trans', 'Prefiero no decirlo'), key = '-GEN-')],
            [sg.Checkbox('Otro', key = '-OTRO-', enable_events=True, font = ('latin modern sansquotation', 15), size = (10,10))],
            [sg.Input('', key = '-NEW-',font = ('latin modern sansquotation', 10), size = (18,15), disabled = True)],
            [sg.Ok(font = ('latin modern sansquotation', 15), key = '-OK-'), (sg.Cancel('Cancelar', font = ('latin modern sansquotation', 15), key = '-CANCEL-' )) ]
            ]
    
    
#images column
    col_2 = [
            [sg.Image(data=get_img_data('perfil_vacio.png', first = True), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ],
            [sg.Text('Seleccione su foto de perfil', font = ('latin modern sansquotation', 15))],
            ]
    
    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout

def ventana_nuevoperfil():
    window = sg.Window("UNLPImage", layout(), margins=(150, 100))
     
    i=0
    while True:
        event, user = window.read()
        i= i+1
        print(i)
        print(event)
        if event == '-PIC-':
            ruta_foto = sg.PopupGetFile('Seleccione la imagen de perfil')
            try:
                window['-PIC-'].update(data=get_img_data(ruta_foto, first = True))
            except AttributeError:
                ruta_foto = 'perfil_vacio.png'
    
        if event == '-OTRO-' :
            window['-NEW-'].update(value = 'Complete el género', disabled = False, select = True, move_cursor_to = "end")
        if event == '-OK-':
            if (user['-NICK-'] == '') or (user['-NAME-'] == '') or (user['-AGE-'] == '' ) or (user['-OTRO-'] == False and user['-GEN-'] == '') or (user['-OTRO-'] == True and user['-NEW-'] == ''):      
                sg.popup_ok('Todos los campos son obligatorios', title='Error!')
    
            #for i in range(len(datos)):
            #    if datos[i][0] == user['-NICK-']:
            #        sg.popup_ok('Todos los campos son obligatorios', title='Error!')
            else:
                try:
                    age=int(user['-AGE-'])
                except ValueError:
                    sg.popup_ok('Ingrese un número para la edad', title='Error!')   
                else:
                    with open('users.json', 'w') as u:
                        if user['-OTRO-']:
                           newuser = {user['-NICK-']: {
                           "nombre": user['-NAME-'],
                           "edad": user['-AGE-'],
                           "genero": user['-NEW-']} }
                           datos.append(newuser)
                           json.dump(datos, u)
    
                           os.makedirs('prof_pictures', exist_ok = True)
                           Image1 = Image.open(ruta_foto)
                           # make a copy the image so that the
                           # original image does not get affected
                           Image1copy = Image1.copy()
                           Image2 = Image.open(ruta_foto)
                           Image2copy = Image2.copy()
     
                           # paste image giving dimensions
                           Image1copy.paste(Image2copy, (0, 0))
     
                           # save the image
                           Image1copy.save('prof_pictures/'+ user['-NICK-']+ '.png')
    
    
                        else:
                           newuser = {user['-NICK-']: {
                           "nombre": user['-NAME-'],
                           "edad": user['-AGE-'],
                           "genero": user['-GEN-']} }
                           datos.append(newuser)
                           json.dump(datos, u)
                           os.makedirs('prof_pictures', exist_ok = True)
                           Image1 = Image.open(ruta_foto)
                           # make a copy the image so that the
                           # original image does not get affected
                           Image1copy = Image1.copy()
                           Image2 = Image.open(ruta_foto)
                           Image2copy = Image2.copy()
     
                           # paste image giving dimensions
                           Image1copy.paste(Image2copy, (0, 0))
     
                           # save the image
                           Image1copy.save('prof_pictures/'+ user['-NICK-']+ '.png')
                        break
        if event == '-CANCEL-' or  event == sg.WIN_CLOSED :
            break
            
    window.close()

if __name__ == '__main__':
    ventana_nuevoperfil()
