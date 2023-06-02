import json
from src.default.pathing import BASE_PATH, img_default
from PIL import Image, ImageTk, UnidentifiedImageError
import os, mimetypes, io, csv

def read_users():
    '''Lee la información de los usuarios registrados presente en el archivo users.json'''
    try:
       archivo = open(os.path.join(BASE_PATH, 'src', 'users-data', 'users.json'), 'r')
       datos = json.load(archivo)
       archivo.close()
    except FileNotFoundError:
       datos = {}
    return datos

def read_config():
    '''Lee las rutas a los repositorios elegidas por los usuarios'''
    try:
        with open(os.path.join(BASE_PATH,'src', 'users-data','archivo_config.json'), 'r') as config:

            datos = json.load(config)    
            ruta_repositorio = datos[0]["ruta"]    #--> Ruta de lo que el usuario haya guardado como repositorio de imagenes
            ruta_collages = datos[1]["ruta"]
            ruta_memes = datos[2]["ruta"]          #--> Ruta de lo que el usuario haya guardado como direcotrio de memes para guardar los memes ya hechos
    except FileNotFoundError:
         ruta_repositorio, ruta_collages, ruta_memes = '', '', ''
         with open(os.path.join(BASE_PATH,'src', 'users-data','archivo_config.json'), 'w') as config:
              config_datos = [{"nombre": "Repositorio", "ruta": ruta_repositorio}, 
                              {"nombre": "Collage", "ruta": ruta_collages}, 
                              {"nombre": "Memes", "ruta": ruta_memes}]
              json.dump(config_datos, config)
         
    return ruta_repositorio, ruta_collages, ruta_memes

def dict_lector():
    '''Es la función encargada de leer el archivo tags.csv y generar el diccionario con sus valores.'''
    metadata = {}
    try:
         with open(os.path.abspath(os.path.join(BASE_PATH,'src','users-data','tags.csv')), 'r') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                _, actividades_anteriores = next(lector_csv), list(lector_csv)
                for img_data in actividades_anteriores:
                    metadata[img_data[0]] = {}
                    metadata[img_data[0]]['path'] = img_data[0]
                    metadata[img_data[0]]['descrip'] = img_data[1]
                    metadata[img_data[0]]['resolution'] = tuple(img_data[2].strip('"'))
                    metadata[img_data[0]]['size'] = img_data[3]
                    metadata[img_data[0]]['mimetype'] = img_data[4]
                    metadata[img_data[0]]['tags'] = [str(tag).strip() for tag in img_data[5].strip("").split(', ')]
                    metadata[img_data[0]]['last_edit'] = img_data[6]
                    metadata[img_data[0]]['last_edit_time'] = img_data[7]
                return metadata
    except FileNotFoundError: 
        with open(os.path.join(BASE_PATH,'src','users-data','tags.csv'), 'x') as archivo_csv: #for exclusive creation, failing if the file already exists
            writer = csv.writer(archivo_csv)
            writer.writerow(['path','description','resolution','size','mimetype','tags','last user','last edit time'])
        print('No se encontró tags.csv. Creado archivo nuevo.')
        return metadata
    except IndexError:
        print('El csv está vacío. Se devuelve diccionario vacío.')
        return metadata

def crear_clave_imagen():
    '''Esta función únicamente se encarga de generar la estructura en el diccionario
    cuando se elige una imagen que no fue registrada anteriormente. Sus valores por defecto son vacíos.'''
    data = {}
    data['path'] = ''
    data['descrip'] = ''
    data['tags'] = list()
    data['last_edit'] = ''
    data['last_edit_time'] = ''
    data['Agrega tag'] = False
    data['Agrega descripción'] = False
    return data

def tagger(metadata, guardar=False):
    '''Es la función encargada de escribir el archivo tags.csv.'''
    header = ['path','descrip','resolution','size','mimetype','tags','last_edit','last_edit_time']
    nueva_actividad = []
    for imagen in metadata.keys():
        data_imagen = [metadata[imagen][clave] for clave in header]
        nueva_actividad.append(data_imagen)

    print('nueva act:', nueva_actividad)
    if guardar:
        # Escribir todas las actividades en el archivo csv
        with open(os.path.join(BASE_PATH,'src','users-data','tags.csv'), 'a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(nueva_actividad)

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
        data['path'] =  os.path.abspath(f)
        data['resolution'] = img.size 
        data['size'] = size
        data['mimetype'] =mimetypes.guess_type(f)[0]
        
        img = img.resize((400,300), Image.ANTIALIAS) #las deforma
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