import json
from src.default.pathing import BASE_PATH, img_default, tags_path
from src.default.setup import tags_header
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
        #  with open(os.path.abspath(os.path.join(BASE_PATH,'src','users-data','tags.csv')), 'r') as archivo_csv:
        #         lector_csv = csv.reader(archivo_csv)
        #         _, actividades_anteriores = next(lector_csv), list(lector_csv)
         _, actividades_anteriores = manejador_csv(tags_path, modo='r')
    except FileNotFoundError: 
        with open(os.path.join(tags_path), 'x', newline='') as archivo_csv: #for exclusive creation, failing if the file already exists
            writer = csv.writer(archivo_csv)
            writer.writerow(tags_header)
        print('No se encontró tags.csv. Creado archivo nuevo.')
        return metadata
    except IndexError:
        print('El csv está vacío. Se devuelve diccionario vacío.')
        return metadata
    
    for img_data in actividades_anteriores:
        if img_data:
            path_img = img_data[0]
            metadata[path_img] = dict(zip(tags_header, img_data))
            # metadata[path_img] = {}
            # metadata[path_img]['path'] = img_data[0]
            # metadata[path_img]['descrip'] = img_data[1]
            metadata[path_img]['resolution'] = tuple(img_data[2].strip('\"()').split(', '))
            # metadata[path_img]['size'] = img_data[3]
            # metadata[path_img]['mimetype'] = img_data[4]
            metadata[path_img]['tags'] = [str(tag).strip('\'') for tag in img_data[5].strip('\"[]').split(', ')]
            metadata[path_img]['Agrega tag'], metadata[path_img]['Agrega descripción'] = True, True
            # metadata[path_img]['last_edit'] = img_data[6]
            # metadata[path_img]['last_edit_time'] = img_data[7]
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
    data['Agrega tag'] = False
    data['Agrega descripción'] = False
    return data

def tagger(metadata, guardar=False):
    '''Es la función encargada de escribir el archivo tags.csv.'''
    sobreescritura = [] #{}
    # data_ya_en_csv = dict_lector()
    # for imagen in metadata.keys():
    #     if (metadata[imagen]['Agrega tag'] or metadata[imagen]['Agrega descripción']):
    #         # sobreescritura = sobreescritura | metadata[imagen] # Agrego la info de la img
    #         data_imagen = [metadata[imagen][clave] for clave in tags_header]
    #         sobreescritura.append(data_imagen)
        
    for imagen in metadata.values():
        if (imagen['Agrega tag'] or imagen['Agrega descripción']):
            # sobreescritura = sobreescritura | metadata[imagen] # Agrego la info de la img
            data_imagen = [imagen[clave] for clave in tags_header]
            sobreescritura.append(data_imagen)
        
    if guardar:
        # Escribir todas las actividades en el archivo csv
        with open(tags_path, 'w', newline='') as archivo_csv:
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

def manejador_csv(ruta_archivo, modo = None, data = None):    
    '''#### lector_csv:
    - Descripción:\n
    Se encarga de procesar todos los csv utilizados en el programa.\n
    ruta_archivo: str(), ruta absoluta\n
    modo: str(). Valores= 'w', 'r', 'x'.\n
    data : any. Información a guardar cuando modo = 'w','a','x'.'''
    with open(ruta_archivo, modo) as archivo_csv:
        match modo:
            case 'r':
                reader_csv = csv.reader(archivo_csv)
                header, data = next(reader_csv), list(reader_csv)
                return header, data
            case 'w','a', 'x':
                writer_csv = csv.writer(archivo_csv, newline='')
                writer_csv.writerow([linea for linea in data])
        # lector_csv = csv.reader(archivo_csv)