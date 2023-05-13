import json
from src.default.pathing import BASE_PATH
from PIL import Image, ImageTk
import os, mimetypes, io

def read_users():
	try:
		archivo = open(os.path.join(BASE_PATH, 'src', 'users-data', 'users.json'), 'r')
		datos = json.load(archivo)
		archivo.close()
	except FileNotFoundError:
		datos = {}
	return datos

def read_config():
	with open(os.path.join(BASE_PATH,'src', 'users-data','archivo_config.json'), 'r') as config:

		datos = json.load(config)    
		ruta_repositorio = datos[0]["ruta"]    #--> Ruta de lo que el usuario haya guardado como repositorio de imagenes
		ruta_collages = datos[1]["ruta"]
		ruta_memes = datos[2]["ruta"]          #--> Ruta de lo que el usuario haya guardado como direcotrio de memes para guardar los memes ya hechos
	return ruta_repositorio, ruta_collages, ruta_memes


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

def get_img_data_profiles(f, first=False):
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