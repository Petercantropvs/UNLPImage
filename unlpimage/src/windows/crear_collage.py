import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageOps, ImageDraw, UnidentifiedImageError
import os
from functools import reduce
from src.default.pathing import BASE_PATH, toload, tosave
from src.default.data import read_config, dict_lector
from src.default.setup import text_format15, text_format10, IMG_SIZE, DESIGNS
from src.windows.generar_etiquetas import arbol
from src.windows.configuracion import ventana_configuracion
from src import function_registo

def collage(template: str, pos: int, img_path, titulo='', collage=None):
    """Crea la imagen collage utilizando los templates predefinidos.
    - Args:
        - template (str): Las opciones válidas son '-L1-', '-L2-', '-L3-', '-L4-', '-L5-' y '-L6-'.
        - foto (str): path or filename de la imagen.
        - pos (int): posición de la imagen en el collage. Dependiendo del template, puede tomar valores entre 1 y 5
        - titulo (str): Texto a colocar sobre el collage.
        - collage (img): Versión previa del collage si ya se le había cargado información
    """
    if not collage:
        collage = Image.new('RGB', IMG_SIZE)

    foto = Image.open(img_path)
    img = ImageOps.fit(foto, DESIGNS[template][pos]['size'])
    collage.paste(img, DESIGNS[template][pos]['coords'])

    if titulo:
        collage_copia = collage.copy()
        draw = ImageDraw.Draw(collage_copia)
        draw.text((10, 380), titulo)
        return collage_copia

    return collage


def guardar_collage(imagen, carpeta_collages):
    """Obtiene el nombre que se le desea poner al archivo collage y lo guarda con formato png.
    Args:
        - imagen (PIL.Image): Collage que se desea guardar
        - carpeta_collages (dir o os.path()): Directorio donde se guarda el collage.
    """
    filename = sg.popup_get_text('Con qué nombre desea guardar el collage?',
                                 default_text='Ingrese el nombre del archivo', title='💾')
    if filename:
        try:
            imagen.save(os.path.join(carpeta_collages,
                        filename+'.png'), format='png')
        except OSError:
            imagen.save(os.path.join(carpeta_collages,
                        filename+'(1)'+'.png'), format='png')
        finally:
            sg.SystemTray.notify('Collage guardado exitosamente!', 'Podés ir a verlo en tu carpeta de collages :)')


def cant_botones(num: int) -> list | dict:
    '''Genera la cantidad de botones necesaria para completar el collage y el layout.
    botones está definido de la siguiente manera, según la recomendación de PySimpleGUI:
    - el símbolo & determina que el siguiente caracter es el keyboard shortcut de la opción en el menú.
    - la cadena :: determina que lo que le sigue será la key de ese botón.
    - El primer elemento de la lista se corresponde con una especie de header que no utilizaremos.
    Args:
        num (int): cantidad de imágenes dentro del template a utilizar.
    Returns:
        list | dict | list: botones del ButtonMenu, diccionario de booleanos para las posiciones en el collage elegido. El diccionario es utilizado luego para saber si el collage fue completado.
    '''
    botones = ['', []]
    for n in range(1, num+1):
        botones[1].append('Imagen &'+str(n)+'::'+str(n))
    tiene_img = {clave: False for clave in range(1, n+1)}
    imgs_en_collage = [None for img in range(n)]

    return botones, tiene_img, imgs_en_collage


def layout(template:str, photo_path:str, metadata: dict) -> list | dict:
    """Layout de la ventana de creación de collages. 

    Args:
        template (str): template elegido en la ventana collage.py. Toma valores entre '-L1-' y '-L6- y define la cantidad de botones en el buttonmenu y de claves en tiene_img.
        photo_path (str): dir o path al repositorio de imágenes.
        metadata (dict): Diccionario que aloja la información de las imágenes etiquetadas, obtenida a partir de tags.csv.

    Returns:
        list | dict: layout de la ventana y diccionario de booleanos para las posiciones en el collage elegido. El diccionario es utilizado luego para saber si el collage fue completado.
    """    
    match template:
        case '-L1-' | '-L2-':
            botones, tiene_img, imgs_en_collage = cant_botones(2)
        case '-L3-' | '-L5-':
            botones, tiene_img, imgs_en_collage = cant_botones(3)
        case '-L4-':
            botones, tiene_img, imgs_en_collage = cant_botones(4)
        case '-L6-':
            botones, tiene_img, imgs_en_collage = cant_botones(5)

    treedata = sg.TreeData()
    arbol('', photo_path, treedata, metadata, tagged_only=True)
    left_col = [[sg.ButtonMenu('Seleccionar imágenes', botones, expand_x=True, key='-BOTONES-')],
                [sg.Tree(data=treedata, headings=['Tags'], auto_size_columns=True, enable_events=True,
                         visible=False, expand_x=True, expand_y=True, key='-TREE-')],
                [sg.Text('Título:', font=text_format15)],
                [sg.Input('', enable_events=True, key='-TITULO-')]]

    right_col = [[sg.Image(size=IMG_SIZE, background_color=sg.theme_button_color()[1], 
                           key='-PREVIEW-')]]

    layout = [[sg.Text('Generar collage', font=text_format15), sg.Push(), sg.Button('⬅ Volver', font=text_format15, key='-VOLVER-')],
              [sg.Column(left_col, vertical_alignment='top'),
               sg.Column(right_col)],
              [sg.Push(), sg.Button('💾 Guardar', font=text_format15, key='-GUARDAR-')]]

    return layout, tiene_img, imgs_en_collage


def creacion_collage(template:str, perfil:str):
    """Función que ejecuta la ventana de creación de collages.

    Args:
        - template (str): Template elegido en la ventana collage.py. Puede tomar valores entre '-L1-' y '-L6-'.
        - perfil (str): Usuario que accede a la ventana.
    """

    metadata = dict_lector()  # Cargo la info presente en tags.csv
    photo_path, carpeta_collages, _ = read_config()
    layout_win, tiene_img, imgs_en_collage = layout(template, photo_path, metadata)
    img, img2 = None, None
    guardo = False

    window = sg.Window('Creá tu collage!', layout_win, resizable=True,
                       finalize=True, enable_close_attempted_event=True)
    
    if not os.path.isdir(carpeta_collages):
        seleccion = None
        while seleccion != '⚙ Ir a configuración':
            seleccion = sg.popup('No tenés configurada una carpeta donde guardar tus collages!', title = None, custom_text='⚙ Ir a configuración')
            if seleccion == '⚙ Ir a configuración':
                ventana_configuracion(perfil)
    
    while True:
        event, values = window.read()
        collage_completo = reduce(lambda x, y: x and y, tiene_img.values())

        match event:
            case  '-BOTONES-':
                # Manejo la key para poder utilizarla:
                posicion = int(values['-BOTONES-'][-1:])
                match posicion:
                    case 1 | 2 | 3 | 4 | 5:
                        window['-TREE-'].update(visible=True)
            case '-TREE-':
                ruta_img = toload(values['-TREE-'][0])
                try:
                    if img:
                        collage(template, posicion, ruta_img, collage=img)
                        tiene_img[posicion] = True
                        imgs_en_collage[posicion-1] = tosave(ruta_img).split('/')[-1]
                    else:
                        img = collage(template, posicion, ruta_img)
                        tiene_img[posicion] = True
                        imgs_en_collage[posicion-1] = tosave(ruta_img).split('/')[-1]
                except (PermissionError, UnidentifiedImageError):
                    pass

                if img:
                    window['-PREVIEW-'].update(
                        data=ImageTk.PhotoImage(img), size=IMG_SIZE)
            case '-TITULO-':
                if collage_completo:
                    try:
                        img2 = collage(template, posicion, ruta_img,
                                       collage=img, titulo=values['-TITULO-'])
                    except (PermissionError, UnidentifiedImageError):
                        pass
                    window['-PREVIEW-'].update(data=ImageTk.PhotoImage(img2), size=IMG_SIZE)
                else:
                    window['-TITULO-'].update('')
                    sg.SystemTray.notify('Collage Incompleto!', 'Debes terminar de elegir imágenes para tu collage antes de añadir un título.', icon=sg.SYSTEM_TRAY_MESSAGE_ICON_CRITICAL)
            case '-GUARDAR-':
                if collage_completo:
                    accion = 'Creó un collage'
                    if img2:
                        guardar_collage(img2, carpeta_collages)
                        function_registo(perfil, accion, values = imgs_en_collage, texts = values['-TITULO-'])
                        guardo = True
                        
                    elif img:
                        sin_titulo = sg.popup_ok_cancel('No has ingresado un título a tu collage.\nDeseas continuar?', title='⚠')
                        if sin_titulo == 'OK':
                            guardar_collage(img, carpeta_collages)
                            function_registo(perfil, accion, values = imgs_en_collage, texts = '')
                            guardo = True
                else:
                    sg.SystemTray.notify('Collage Incompleto!', 'Debes terminar de elegir imágenes para tu collage antes de guardar.', icon=sg.SYSTEM_TRAY_MESSAGE_ICON_CRITICAL)

        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, '-VOLVER-'):
            if True in tiene_img.values() and not guardo:
                if sg.popup_yes_no('Seguro que desea salir? Perderá los cambios', title = None) == 'Yes':
                    accion = "Entró a generar un collage pero no lo guardó."
                    function_registo(perfil, accion)
                    window.close()
                    break
            else:
                window.close()
                break


if __name__ == '__main__':
    creacion_collage('-L1-', 'testrun')
