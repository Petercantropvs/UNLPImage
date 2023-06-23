import json
from src.default.pathing import BASE_PATH, img_default, tags_path, tosave, toload
from src.default.setup import tags_header
from PIL import Image, ImageTk, ImageOps, UnidentifiedImageError
import os, mimetypes, io, csv
import PySimpleGUI as sg

def abrir_json(path):
    '''Me permite abrir cualquier archivo.json, a partir de mandarle la ruta correspondiente'''
    archivo = open(path, 'r')
    datos = json.load(archivo)
    archivo.close()
    return datos

def read_users():
    '''Lee la información de los usuarios registrados presente en el archivo users.json'''
    try:
        datos = abrir_json(os.path.join(BASE_PATH, 'src', 'users-data', 'users.json'))
    except FileNotFoundError:
       datos = {}
    return datos

def check_campos(user,usuarios,edit=False):
    ok=True
    if edit == False:  
        if str(user['-NICK-']).lower() in str(usuarios).lower():
            if user['-NICK-'] != '':
                sg.popup_ok('El nick o alias ya está utilizado', title='Error!')  
                ok= False 
    if (user['-NICK-'] == '') or (user['-NAME-'] == '') or (user['-AGE-'] == '' ) or (user['-OTRO-'] == False and user['-GEN-'] == '') or (user['-OTRO-'] == True and user['-NEW-'] == ''):      
        sg.popup_ok('Todos los campos son obligatorios', title='Error!')
        ok= False
    
    else:

        try:
            age=int(user['-AGE-'])
        except ValueError:
            sg.popup_ok('Ingrese un número para la edad', title='Error!')   
            ok= False
    return ok

def read_config():
    '''Lee las rutas a los repositorios elegidas por los usuarios'''
    try:
        datos = abrir_json(os.path.join(BASE_PATH,'src', 'users-data','archivo_config.json'))
        ruta_repositorio = toload(datos[0]["ruta"])    #--> Ruta de lo que el usuario haya guardado como repositorio de imagenes
        ruta_collages = toload(datos[1]["ruta"])
        ruta_memes = toload(datos[2]["ruta"])          #--> Ruta de lo que el usuario haya guardado como direcotrio de memes para guardar los memes ya hechos
    except FileNotFoundError:
         ruta_repositorio, ruta_collages, ruta_memes = '', '', ''
         with open(os.path.join(BASE_PATH,'src', 'users-data','archivo_config.json'), 'w', encoding='utf-8') as config:
              config_datos = [{"nombre": "Repositorio", "ruta": ruta_repositorio}, 
                              {"nombre": "Collage", "ruta": ruta_collages}, 
                              {"nombre": "Memes", "ruta": ruta_memes}]
              json.dump(config_datos, config, ensure_ascii = False)    
    return ruta_repositorio, ruta_collages, ruta_memes

def dict_lector():
    '''Es la función encargada de leer el archivo tags.csv y generar el diccionario con sus valores.'''
    metadata = {}
    try:
         _, actividades_anteriores = manejador_csv(tags_path, modo='r')
    except FileNotFoundError: 
        with open(tags_path, 'x', encoding='utf-8', newline='') as archivo_csv: #for exclusive creation, failing if the file already exists
            writer = csv.writer(archivo_csv)
            writer.writerow(tags_header)
        # No se encontró tags.csv. Creado archivo nuevo.
        return metadata
    except IndexError:
        # 'El csv está vacío. Se devuelve diccionario vacío.
        return metadata
    
    for img_data in actividades_anteriores:
        if img_data:
            path_img = toload(img_data[0])
            metadata[path_img] = dict(zip(tags_header, img_data))
            metadata[path_img]['path'] = path_img
            metadata[path_img]['resolution'] = tuple(img_data[2].strip('\"()').split(', '))
            metadata[path_img]['tags'] = [str(tag).strip('\'') for tag in img_data[5].strip('\"[]').split(', ')]
            metadata[path_img]['tiene tag'], metadata[path_img]['tiene descripción'] = True, True
            metadata[path_img]['imagen nueva'] = False
    return metadata

def crear_clave_imagen():
    '''Esta función únicamente se encarga de generar la estructura en el diccionario
    cuando se elige una imagen que no fue registrada anteriormente. Sus valores por defecto son vacíos.'''
    data = {}
    data['path'] = ''
    data['description'] = ''
    data['tags'] = list()
    data['last user'] = ''
    data['last edit time'] = ''
    data['tiene tag'] = False
    data['tiene descripción'] = False
    data['imagen nueva'] = True
    return data

def tagger(metadata):
    '''Es la función encargada de escribir el archivo tags.csv.'''
    sobreescritura = []
        
    for imagen in metadata.values():
        if (imagen['tiene tag'] or imagen['tiene descripción']):
            #data_imagen = [str(imagen[clave]).replace('\'', '').replace('\"','') for clave in tags_header]
            data_imagen = [str(imagen[clave]).replace('\'', '').replace('\"','').replace('[', '').replace(']', '') for clave in tags_header]
            data_imagen[0] = tosave(data_imagen[0])
            sobreescritura.append(data_imagen)
    sobreescritura.sort(key= lambda x: x[7])

    # Escribe todas las actividades en el archivo csv
    with open(tags_path, 'w', encoding='utf-8', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(tags_header)
        escritor_csv.writerows(sobreescritura)

def get_img_data_tags(f, first=False):
    """Genera los datos de la imagen para poder visualizarlo en la ventana.
    Guarda algunos metadatos de la misma en metadata."""
    try:
        img = Image.open(f)
    except (FileNotFoundError, UnidentifiedImageError):
        img = Image.open(img_default)
    finally:    
        size = os.path.getsize(f)*(9.537e-7)
        if size < 1.0:
            size = str(round(os.path.getsize(f)/1024., 1)) + ' KB'
        else:
            size = str(round(os.path.getsize(f)*(9.537e-7), 1)) + ' MB'
        data = {}
        data['path'] =  os.path.abspath(f) #toload(f) #os.path.abspath(f)
        data['resolution'] = img.size 
        data['size'] = size
        data['mimetype'] =mimetypes.guess_type(f)[0]
        
        img = ImageOps.fit(img, (400,300), Image.ANTIALIAS) #las deforma
        # img = img.transform((400,300), Image.Transform.AFFINE) #Image.BICUBIC)
        if first:                     # tkinter is inactive the first time
            bio = io.BytesIO()
            img.save(bio, format="PNG")
            del img
            return bio.getvalue(), data
    return ImageTk.PhotoImage(img), data

def get_img_data_profiles(f, first=False):
    """Genera los datos de la imagen usando PIL
    """
    img = Image.open(f)
    img = img.resize((200,200), Image.ANTIALIAS)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)

def manejador_csv(ruta_archivo, modo = None, data = None):    
    '''#### lector_csv:
    - Descripción:\n
    Se encarga de procesar todos los csv utilizados en el programa.\n
    ruta_archivo: str(), ruta absoluta\n
    modo: str(). Valores= 'w', 'r', 'x'.\n
    data : any. Información a guardar cuando modo = 'w','a','x'.'''
    with open(ruta_archivo, modo, encoding='utf-8', newline='') as archivo_csv:
        match modo:
            case 'r':
                reader_csv = csv.reader(archivo_csv)
                header, data = next(reader_csv), list(reader_csv)
                return header, data
            case 'w','a', 'x':
                writer_csv = csv.writer(archivo_csv, newline='')
                writer_csv.writerow([linea for linea in data])
        # lector_csv = csv.reader(archivo_csv)


def read_memes():
    '''Lee la información de los template de memes registrados en template-memes.json'''
    try:
        datos = abrir_json(os.path.join(BASE_PATH,'src', 'users-data','template_meme.json'))
    except FileNotFoundError:
       datos = {}
    return datos  


