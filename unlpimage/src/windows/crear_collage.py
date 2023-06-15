import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageOps, ImageDraw, UnidentifiedImageError
import os
from src.default.pathing import BASE_PATH, toload, tosave
from src.default.data import read_config, dict_lector
from src.default.setup import text_format15, text_format10, IMG_SIZE, DESIGNS
from src.windows.generar_etiquetas import arbol
# directorio_collages = read_config()[1]
# relpath = os.path.relpath(os.path.join(dir_imagenes, archivo), start = BASE_PATH)

# def imagenes_etiquetadas(parent, imagenes, metadata):
    
#     dir_imagenes = read_config()[0]
#     for archivo in os.listdir(dir_imagenes):
#         print(archivo)
#         imagenes.Insert(parent, key = archivo, text = archivo, values=[])
#     return imagenes

def collage(template:str, pos:int, img_path, titulo='', collage = None):
    """collage
    Crea la imagen collage utilizando los templates predefinidos.
    - Args:
        - template (str): Las opciones válidas son '-L1-', '-L2-', '-L3-', '-L4-', '-L5-' y '-L6-'.
        - foto (str): path or filename de la imagen.
        - pos (int): posición de la imagen en el collage. Dependiendo del template, puede tomar valores entre 1 y 5
        - titulo (str): Texto a colocar sobre el collage.
        - collage (img): Versión previa del collage si ya se le había cargado información
    """
    if not collage:
        collage = Image.new('RGB', IMG_SIZE)
        print('no había collage')
    
    foto = Image.open(img_path)
    img = ImageOps.fit(foto, DESIGNS[template][pos]['size'])
    collage.paste(img, DESIGNS[template][pos]['coords'])
    # match template:
    #     case '-L1-':
    #         img = ImageOps.fit(foto, (300,200))
    #         match pos:
    #             case 1:
    #                 collage.paste(img, (0,0))
    #             case 2:
    #                 collage.paste(img, (0,200))
    
    if titulo:
        collage_copia = collage.copy()
        draw = ImageDraw.Draw(collage_copia)
        draw.text((10,380), titulo)
        return collage_copia
    
    return collage

def cant_botones(num:int) -> list | dict:
    '''Genera la cantidad de botones necesaria para completar el collage y el layout.
    botones está definido de la siguiente manera, según la recomendación de PySimpleGUI:
    - el símbolo & determina que el siguiente caracter es el keyboard shortcut de la opción en el menú.
    - la cadena :: determina que lo que le sigue será la key de ese botón.
    - El primer elemento de la lista se corresponde con una especie de header que no utilizaremos.
    '''
    botones = ['',[]]
    for n in range(1, num+1):
        botones[1].append('Imagen &'+str(n)+'::'+str(n))
        # botones[1].append('---')
    return botones

def layout(template, photo_path, metadata):
    match template:
        case '-L1-' | '-L2-':
            botones = cant_botones(2)
            tiene_img = {clave: False for clave in range(1,3)}
        case '-L3-' | '-L5-':
            botones = cant_botones(3)
            tiene_img = {clave: False for clave in range(1,4)}
        case '-L4-':
            botones = cant_botones(4)
            tiene_img = {clave: False for clave in range(1,5)}
        case '-L6-':
            botones = cant_botones(5)
            tiene_img = {clave: False for clave in range(1,6)}
    
    treedata = sg.TreeData()
    arbol('', photo_path, treedata, metadata, tagged_only=True)
    left_col = [[sg.ButtonMenu('Seleccionar imágenes', botones,expand_x = True, key='-BOTONES-')],
                [sg.Tree(data = treedata,headings= ['Tags'], auto_size_columns=True, enable_events=True, visible=False, expand_x=True, expand_y= True, key='-TREE-')],
                [sg.Text('Título:', font = text_format15)],
                [sg.Input('', enable_events= True, key = '-TITULO-')]]

    right_col = [[sg.Image(size = IMG_SIZE, background_color = sg.theme_button_color()[1], key = '-PREVIEW-')]]

    layout = [[sg.Text('Generar collage', font = text_format15), sg.Push(), sg.Button('⬅ Volver', font = text_format15, key = '-VOLVER-')],
              [sg.Column(left_col, vertical_alignment='top'), sg.Column(right_col)],
              [sg.Push(), sg.Button('💾 Guardar', font = text_format15, key = '-GUARDAR-')]]

    return layout, tiene_img
    
def creacion_collage(template):
    metadata = dict_lector() # Cargo la info en tags.csv
    photo_path = read_config()[0]
    layout_win, tiene_img = layout(template, photo_path, metadata)
    img = None
    window = sg.Window('Creá tu collage!', layout_win, resizable= True, finalize=True, enable_close_attempted_event= True)

    while True:
        event, values = window.read()

        match event:
            case  '-BOTONES-':
                posicion = int(values['-BOTONES-'][-1:]) # Manejo la key para poder utilizarla
                print('clickeó ', values[event])
                match posicion:
                    case 1|2|3|4|5:
                        tiene_img[posicion] = False
                        window['-TREE-'].update(visible=True)
            case '-TREE-':
                ruta_img = toload(values['-TREE-'][0])

                if img:#not tiene_img[posicion] and True in tiene_img.values():
                    try:
                        collage(template, posicion, ruta_img, collage=img) # DAR VUELTA TRY
                        tiene_img[posicion] = True
                    except (PermissionError, UnidentifiedImageError):
                        print('entré')
                else:
                    try:
                        img = collage(template, posicion, ruta_img)
                        tiene_img[posicion] = True
                    except (PermissionError, UnidentifiedImageError):
                        pass
                
                if img:
                    window['-PREVIEW-'].update(data = ImageTk.PhotoImage(img), size=IMG_SIZE)
                    tiene_img[posicion] = True
            case '-TITULO-':
                if img:#not tiene_img[posicion] and True in tiene_img.values():
                    try:
                        img2 = collage(template, posicion, ruta_img, collage=img, titulo=values['-TITULO-'])
                    except (PermissionError, UnidentifiedImageError):
                        print('entré')
                    window['-PREVIEW-'].update(data = ImageTk.PhotoImage(img2), size=IMG_SIZE)
            case '-GUARDAR-':
                pass
        
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, '-VOLVER-'):
            if sg.popup_yes_no('Desea salir sin guardar?') == 'Yes':
                    window.close()
                    break

if __name__ == '__main__':
    creacion_collage('-L1-')

