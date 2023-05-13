# Etiquetas

import PySimpleGUI as sg
from PIL import Image, ImageTk, UnidentifiedImageError
import os, io, csv, mimetypes
from src.default.pathing import BASE_PATH

treedata = sg.TreeData()
img_default = os.path.join(BASE_PATH,'src','default','FileNotFoundErr.png')
ETIQUETAS = [sg.Text('Tags:'), sg.Text(background_color=sg.theme_button_color()[1], key = '-OUTPUT-')]

# Función para construir el treedata (carpetas, subcarpetas y archivos)
def arbol(parent, directorio):
    '''Esta función construye el objeto treedata que contiene la estructura del tree del directorio seleccionado en configuración
    como repositorio de imágenes para que el Tree Element de PySimpleGUI pueda leerlo e interpretarlo.'''

    folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

    for archivo in os.listdir(directorio):
        ruta = os.path.join(directorio, archivo)
        
        if os.path.isdir(ruta):    # Si es carpeta
            treedata.Insert(parent, ruta, archivo, values=[], icon=folder_icon)
            arbol(ruta, ruta)
        else:                         # Acá el values hay que completarlo con los tags
            treedata.Insert(parent, ruta, archivo, values=[os.stat(ruta).st_size], icon=file_icon)

def layout(photo_path, metadata=None):
    '''Función que corresponde al layout de ventana_etiquetas(). photo_path es la ruta del repositorio que deseamos visualizar
    en el tree.
    frame layout corresponde a la configuración de botones y pestañas dentro del marco que corresponde a la columna derecha.
    layout_l y _r corresponden a las columnas izquierda y derecha respectivamente.'''

    arbol('',photo_path)
    img_def, metadata = get_img_data(img_default, first=True)

    frame_layout = [[sg.Image(data = img_def, size = (400,300), key = '-VISUALIZADOR-')],
                    [sg.Column([[sg.VerticalSeparator(), sg.Text(metadata['mimetype'], k='-META1-'), 
                                sg.VerticalSeparator(), sg.Text(metadata['size'], k='-META2-'), 
                                sg.VerticalSeparator(), sg.Text(str(metadata['resolution'][0])+'X'+str(metadata['resolution'][1]), k='-META3-'), 
                                sg.VerticalSeparator()]],
                                key='-META-',expand_x=True, element_justification='center', visible=False)],
                    ETIQUETAS,
                    [sg.Text('Descripción:')],
                    [sg.Text(expand_y=True, background_color=sg.theme_button_color()[1], key = '-DESCRIPOUT-')]]

    layout_l = sg.Column([[sg.Tree(data = treedata, headings = ['Tags',], auto_size_columns=True,
                                   expand_x = True, expand_y = True, enable_events = True, key = '-TREE-')],
                        [sg.Text('Tag')],
                        [sg.Input('', size=(50,1), key = '-NEWTAG-', disabled=True, enable_events=True),
                         sg.Button('Agregar', key='-B1-', disabled=True)],
                        [sg.Text('Texto descriptivo')],
                        [sg.Multiline('', size=(50,4), key = '-DESCRIP-', disabled=True, enable_events=True, no_scrollbar=True),
                         sg.Button('Agregar', key = '-B2-', disabled=True)]],
                        expand_y = True, justification = 'left', pad = ((0,20),(0,0)))

    layout_r = sg.Column([[sg.Frame('Seleccione una imagen para visualizar',
                                    frame_layout, 
                                    background_color=sg.theme_button_color()[1], 
                                    size=(300,400),
                                    expand_x = True,
                                    expand_y = True,
                                    key = '-FRAME-')]], 
                                    background_color=None,
                                    expand_x= True, expand_y= True)   
                       
    layout = [[sg.Text('Seleccione la imagen que desee etiquetar:'), sg.Push(), sg.Button('Volver', key = '-VOLVER-')],
              [layout_l, layout_r], 
              [sg.Push(), sg.Button('Guardar', disabled=True)]]
    return layout

def ventana_etiquetas(photo_path=None):
    ''' Añadir lo que hace'''
    if not photo_path:
        photo_path = os.path.join(BASE_PATH, 'src', 'default', 'tree-empty')
    
    window = sg.Window('Etiquetar imágenes', layout(photo_path), resizable=True, finalize=True)

    while True:
        event, values = window.read()
        Agrega_tag = False
        Agrega_descrip = False

        match event:
            case '-TREE-':
                ruta_imagen_sel = os.path.relpath(str(values['-TREE-']).strip('\'[]'), start = photo_path)
                ruta_completa = os.path.join(photo_path, ruta_imagen_sel)
                if not os.path.isdir(ruta_completa): #Se actualiza la imagen cuando no se selecciona un directorio
                    try:
                        img, metadata = get_img_data(ruta_completa, first=True)
                        window['-VISUALIZADOR-'].update(data = img, size = (400,300))
                    except UnidentifiedImageError:
                        _, metadata = get_img_data(ruta_completa, first=True)
                        window['-VISUALIZADOR-'].update(data = get_img_data(img_default, first=True), size = (400,300))
                    
                    window['-FRAME-'].update(ruta_imagen_sel)

                    window['-META-'].update(visible=True)
                    window['-META1-'].update(metadata['mimetype'])
                    window['-META2-'].update(metadata['size'])
                    window['-META3-'].update(str(metadata['resolution'][0])+'X'+str(metadata['resolution'][1]))

                    window['-NEWTAG-'].update(disabled=False)
                    window['-DESCRIP-'].update(disabled=False)                                              
                else:
                    window['-NEWTAG-'].update(disabled=True)
                    window['-DESCRIP-'].update(disabled=True)
                    window['-FRAME-'].update('Seleccione una imagen para visualizar')
                    window['-B1-'].update(disabled=True)
                    window['-B2-'].update(disabled=True)
            case '-NEWTAG-':
                window['-B1-'].update(disabled=False)  
            case '-DESCRIP-':
                window['-B2-'].update(disabled=False)
            case '-B1-':
                window['-OUTPUT-'].update(values['-NEWTAG-'])
                window['-OUTPUT-'].bind('bind_string', key_modifier=None)
                ETIQUETAS.append(sg.Text(background_color=sg.theme_button_color()[1], key = '-OUTPUT-'))
                window['-NEWTAG-'].update('')
                window['-B1-'].update(disabled=True)
                window['Guardar'].update(disabled=False)
                accion, Agrega_tag = 'Agregó un tag', True
            case '-B2-':
                window['-DESCRIPOUT-'].update(values['-DESCRIP-'])
                window['-DESCRIP-'].update('')
                window['-B2-'].update(disabled=True)
                window['Guardar'].update(disabled=False)
                accion, Agrega_descrip = 'Agregó una descripción', True
            case '-GUARDAR-':
                    # tagger(metadata)
                    accion = 'Guardó información en las imágenes del directorio'
                    window['-B1-'].update(disabled=True)
                    window['-B2-'].update(disabled=True)
                    window['Guardar'].update(disabled=True)


        print(event, values)
        if event == sg.WIN_CLOSED or event == '-VOLVER-':
            accion = 'Abrió la ventana de etiquetas'
            break

    window.close()
    return accion

def get_img_data(f, first=False):
    """Genera los datos de la imagen para poder visualizarlo en la ventana.
    Guarda algunos metadatos de la misma en metadata."""
    img = Image.open(f)
    size = os.path.getsize(f)*(9.537e-7)
    if size < 1.0:
        size = str(round(os.path.getsize(f)/1024., 1)) + ' KB'
    else:
        size = str(round(os.path.getsize(f)*(9.537e-7), 1)) + ' MB'

    metadata = {'path': os.path.abspath(f), 
                'resolution': img.size, 
                'size' : size,
                'mimetype' : mimetypes.guess_type(f)[0]}
    
    img = img.resize((400,300), Image.ANTIALIAS) #las deforma
    # img = img.transform((400,300), Image.Transform.AFFINE) #Image.BICUBIC)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue(), metadata
    return ImageTk.PhotoImage(img), metadata

# def tagger(metadata):
#     '''Es la función encargada de leer y escribir el archivo tags.csv.'''
#     actividades_anteriores = []
#     try:
#         with open(os.path.join(BASE_PATH,'src','users-data','tags.csv'), 'r') as archivo_csv:
#             lector_csv = csv.reader(archivo_csv)
#             actividades_anteriores = list(lector_csv)
#     except FileNotFoundError:
#         pass

#     nueva_actividad = [path, descrip, res, size, mimetype, tags, last_edit, last_edit_t]
#     actividades_anteriores.append(nueva_actividad)


#     # Escribir todas las actividades en el archivo CSV
#     with open(os.path.join(BASE_PATH,'src','users-data','tags.csv'), 'w', newline='') as archivo_csv:
#         escritor_csv = csv.writer(archivo_csv)
#         escritor_csv.writerows(actividades_anteriores)

if __name__ == '__main__':
    photo_path = sg.PopupGetFolder('Por favor, seleccione la carpeta de imágenes')
    BASE_PATH = os.path.join('C:','Users','Usuario','Documents','Pedro','Facultad','Seminario Python','Prácticas','Trabajo Final','unlpimage')
    ventana_etiquetas(photo_path=photo_path)