import PySimpleGUI as sg
from PIL import UnidentifiedImageError
import os
from datetime import datetime
from src.default.pathing import BASE_PATH, img_default, folder_icon, file_icon
from src.default.data import get_img_data_tags as get_img_data
from src.default.data import read_config, dict_lector, crear_clave_imagen, tagger
from src import function_registo
from functools import reduce

# Función para construir el treedata (carpetas, subcarpetas y archivos)
def arbol(parent, directorio, treedata, metadata, tagged_only=False):
    """arbol construye el objeto treedata que contiene la estructura del tree del directorio seleccionado en configuración
    como repositorio de imágenes para que el Tree Element de PySimpleGUI pueda leerlo e interpretarlo.

    Args:
        parent (_type_): _description_
        directorio (_type_): _description_
        treedata (_type_): _description_
        metadata (_type_): _description_
        tagged_only (bool, optional): Si es True, completa el tree con únicamente los objetos que fueron taggeados en metadata. Por defecto este valor es False.
    """
    if tagged_only:
        def tiene_tags(f):
            return (metadata[os.path.join(directorio, f)]['tags']!=[] if os.path.join(directorio, f) in metadata.keys() else False)
        
        archivos = filter(lambda f: (os.path.isdir(os.path.join(directorio, f)) or tiene_tags(f)), os.listdir(directorio))
    else:
        archivos = os.listdir(directorio)

    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        
        if os.path.isdir(ruta):    # Si es carpeta
            treedata.Insert(parent, ruta, archivo, values=[], icon=folder_icon)
            arbol(ruta, ruta, treedata, metadata, tagged_only = tagged_only)
        else:
            if ruta in metadata.keys():
                tags = '#'+ ', #'.join(tag for tag in metadata[ruta]['tags'])
            else:
                tags = ''
            treedata.Insert(parent, ruta, archivo, values=[tags], icon=file_icon)

def layout(photo_path, metadata):
    '''Función que corresponde al layout de ventana_etiquetas(). photo_path es la ruta del repositorio que deseamos visualizar
    en el tree.
    frame layout corresponde a la configuración de botones y pestañas dentro del marco que corresponde a la columna derecha.
    layout_l y _r corresponden a las columnas izquierda y derecha respectivamente.'''
    treedata = sg.TreeData()

    arbol('',photo_path, treedata, metadata)
    frame_layout = [[sg.Image(size = (400,300), key = '-VISUALIZADOR-')],
                    [sg.Column([[sg.VerticalSeparator(), sg.Text(k='-META1-'),
                                sg.VerticalSeparator(), sg.Text(k='-META2-'),
                                sg.VerticalSeparator(), sg.Text(k='-META3-'),
                                sg.VerticalSeparator()]],
                                key='-META-',expand_x=True, element_justification='center', visible=False)],
                    [sg.Text('Tags:'), sg.Text(auto_size_text= True ,background_color=sg.theme_button_color()[1], key = '-OUTPUT-')], #' ,'.join(metadata[os.path.abspath(img_default)]['tags']), ETIQUETAS,
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

def ventana_etiquetas(perfil):
    ''' La ventana de creación de etiquetas permite a partir de una ventana con dos pantallas: una a la izquierda mostrando el arbol de archivos del repositorio de imagenes elegido
    y otra a la derecha visualizando la imagen que se haya seleccionado en la pantalla de la izquierda. En esta ventana se crean las etiquetas que facilitarán la búsqueda de imagenes
    posteriormente.'''
    accion = 'Abrió la ventana de etiquetas pero no generó etiquetas'
    realiza_cambios, guardo = False, False
    photo_path = read_config()[0]
    metadata = dict_lector() # Cargo lo que ya estaba registrado en el csv

    if not photo_path:
        photo_path = os.path.join(BASE_PATH, 'src', 'default', 'tree-empty')
        if not os.path.exists(os.path.abspath(photo_path)):
            os.makedirs(os.path.abspath(photo_path))
    
    window = sg.Window('Etiquetar imágenes', layout(photo_path, metadata), resizable=True, finalize=True, enable_close_attempted_event=True)
    window.set_min_size((400,600))
    while True:
        event, values = window.read()
        match event:
            case '-TREE-':

                ruta_relativa = os.path.relpath(str(values['-TREE-']).strip('\'[]'), start = photo_path)
                ruta_completa = os.path.abspath(os.path.join(photo_path, ruta_relativa))
                if ruta_completa not in metadata.keys():
                    # Completo el diccionario de la imagen con valores por defecto:
                    metadata[ruta_completa] = crear_clave_imagen()
                
                if not os.path.isdir(ruta_completa): # Se actualiza la imagen cuando no se selecciona un directorio
                    try:
                        img, data = get_img_data(ruta_completa, first=True)
                        window['-VISUALIZADOR-'].update(data = img, size = (400,300))
                    except UnidentifiedImageError:
                        img, data = get_img_data(ruta_completa, first=True)
                        window['-VISUALIZADOR-'].update(data = get_img_data(img_default, first=True), size = (400,300))
                    
                    metadata[ruta_completa] = metadata[ruta_completa] | data # mergeo los diccionarios para no pisarlos
                    window['-FRAME-'].update(ruta_relativa)

                    window['-META-'].update(visible=True)
                    window['-META1-'].update(metadata[ruta_completa]['mimetype'])
                    window['-META2-'].update(metadata[ruta_completa]['size'])
                    window['-META3-'].update(str(metadata[ruta_completa]['resolution'][0])+'X'+str(metadata[ruta_completa]['resolution'][1]))
                    window['-OUTPUT-'].update(('#'+ ', #'.join(tag for tag in metadata[ruta_completa]['tags'])) if metadata[ruta_completa]['tags'] != [] else '')
                    window['-DESCRIPOUT-'].update(metadata[ruta_completa]['description'])

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
                tags = '#'+ ', #'.join(tag for tag in metadata[ruta_completa]['tags'])
                window['-OUTPUT-'].update(tags)
                window['-TREE-'].update(key=ruta_completa, value=tags)
                window['-NEWTAG-'].update('')
                window['-B1-'].update(disabled=True)
                window['Guardar'].update(disabled=False)
                metadata[ruta_completa]['tags'].append(values['-NEWTAG-'])
                metadata[ruta_completa]['last user'] = str(perfil)
                metadata[ruta_completa]['last edit time'] = datetime.now().strftime('%d-%m-%y %H:%M:%S')
                metadata[ruta_completa]['tiene tag'] = True
                realiza_cambios = True

            case '-B2-':
                window['-DESCRIPOUT-'].update(values['-DESCRIP-'])
                window['-DESCRIP-'].update('')
                window['-B2-'].update(disabled=True)
                window['Guardar'].update(disabled=False)
                
                metadata[ruta_completa]['description'] = values['-DESCRIP-']
                metadata[ruta_completa]['last user'] = str(perfil)
                metadata[ruta_completa]['last edit time'] = datetime.now().strftime('%d-%m-%y %H:%M:%S')
                metadata[ruta_completa]['tiene descripción'] = True

                realiza_cambios = True

            case 'Guardar':
                respuesta = sg.popup_yes_no('Seguro que desea guardar?', title = '💾')
                if respuesta =='Yes':

                    manejo_del_evento(perfil, metadata)
                    metadata = {ruta: metadata[ruta] for ruta in metadata.keys()}
                    tagger(metadata)
                    guardo = True
                    window['-B1-'].update(disabled=True)
                    window['-B2-'].update(disabled=True)
                    window['Guardar'].update(disabled=True)
                    sg.SystemTray.notify('Se ha guardado exitosamente!', 'Ya puedes utilizar estas imágenes para crear collages ;)')
                    
        
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, '-VOLVER-'):
            if realiza_cambios and not guardo:
                if sg.popup_yes_no('Desea salir sin guardar?', title=None) == 'Yes':
                    window.close()
                    #accion = 'Abrió la ventana de etiquetas pero no generó etiquetas'
                    #function_registo(perfil, accion)
                    break
            else:
                window.close()
                break

       
    window.close()

def manejo_del_evento(perfil:str, metadata:dict) -> None:
    """Determina a partir de los booleanos img['tiene tag'], img['tiene descripción'] y img['imagen nueva'] si de todas las imágenes que han sido etiquetadas en esta sesión hay alguna que no haya sido clasificada previamente.

    Args:
        perfil (str): Nickname del usuario que ejecuta el programa
        metadata (dict): Diccionario que contiene los booleanos a utilizar.
    """
    
    imagenes_etiquetadas = filter(lambda img: (img['tiene tag'] or img['tiene descripción']), metadata.values())
    try:
        hay_imgs_nuevas = reduce(lambda x,y : x or y, (img['imagen nueva'] for img in imagenes_etiquetadas))
    except TypeError:
        # El csv estaba vacío, por ende metadata también y el objeto reduce no puede iterar sobre un objeto vacío
        hay_imgs_nuevas = True

    if hay_imgs_nuevas:
        accion = 'Guardó información nueva en las imágenes del directorio'
    else:
        accion = 'Modificó información en las imágenes del directorio'
    function_registo(perfil, accion)


if __name__ == '__main__':
    photo_path = sg.PopupGetFolder('Por favor, seleccione la carpeta de imágenes')
    ventana_etiquetas('testrun')