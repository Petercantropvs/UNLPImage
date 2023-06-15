#Segunda natalla de memes
import PySimpleGUI as sg
import os
import json
from src.default.pathing import BASE_PATH, templates_memes_path
from src.default.data import read_config
from src.default.data import read_memes 

from PIL import Image, ImageTk, ImageFont, ImageDraw, ImageFont
from src.default.setup import text_format15, text_format10

#archivo_memes = open('template_meme.json', 'r')
#datos = json.load(archivo_memes)
             
ruta_repositorio, ruta_collages, ruta_memes = read_config()
datos = read_memes()
templates_path = templates_memes_path

##########################################################################################################
#Funciones auxliliares: 
#1)Calculo el tamaño del box: ancho=x2-x1, alto=y2-y1
def tam_box(x1,y1,x2,y2):
    return(x2-x1,y2-y1)

#3) Veo si entra o no, el texto contenido en el contenedor
def entra(contenedor, contenido):
    return contenido[0] <= contenedor[0] and contenido[1] <= contenedor[1]


#4) Calculo la tipografía a ver si entra:
def calcular_tam_fuente(draw, texto, path_fuente, box):
    tam_contenedor = tam_box(*box)

    for tam in range (200, 20, -5):
        fuente = ImageFont.truetype(path_fuente, tam)
        box_texto = draw.textbbox((0,0), texto, font=fuente)
        tam_box_texto = tam_box(*box_texto)
        if entra(tam_contenedor, tam_box_texto):
            return fuente
    return fuente


#5) cant_boxes = 2
def boxes_2(draw, meme_texto, datos_list):
    
    x1 = datos[datos_list]["text_boxes"][0]["top_left_x"]
    y1 = datos[datos_list]["text_boxes"][0]["top_left_y"]
    x2 = datos[datos_list]["text_boxes"][0]["bottom_right_x"]
    y2 = datos[datos_list]["text_boxes"][0]["bottom_right_y"]
    draw.rectangle([(x1, y1), (x2, y2)],  outline=None)

    x3 = datos[datos_list]["text_boxes"][1]["top_left_x"]
    y3 = datos[datos_list]["text_boxes"][1]["top_left_y"]
    x4 = datos[datos_list]["text_boxes"][1]["bottom_right_x"]
    y4 = datos[datos_list]["text_boxes"][1]["bottom_right_y"]
    draw.rectangle([(x3, y3), (x4, y4)],  outline=None)

    #Guardado de nueva imagen e impresión
    meme_texto.save(os.path.join('src','Repositorio_prueba', 'imagen_con_cuadros_de_texto.png'))
    Image.open(os.path.join('src','Repositorio_prueba','imagen_con_cuadros_de_texto.png'))
    return (x1, y1, x2, y2), (x3, y3, x4, y4)

def boxes_3(draw,meme_texto, datos_list):
    x1 = datos[datos_list]["text_boxes"][0]["top_left_x"]
    y1 = datos[datos_list]["text_boxes"][0]["top_left_y"]
    x2 = datos[datos_list]["text_boxes"][0]["bottom_right_x"]
    y2 = datos[datos_list]["text_boxes"][0]["bottom_right_y"]
    draw.rectangle([(x1, y1), (x2, y2)],  outline=None)

    x3 = datos[datos_list]["text_boxes"][1]["top_left_x"]
    y3 = datos[datos_list]["text_boxes"][1]["top_left_y"]
    x4 = datos[datos_list]["text_boxes"][1]["bottom_right_x"]
    y4 = datos[datos_list]["text_boxes"][1]["bottom_right_y"]
    draw.rectangle([(x3, y3), (x4, y4)],  outline=None)

    x5 = datos[datos_list]["text_boxes"][2]["top_left_x"]
    y5 = datos[datos_list]["text_boxes"][2]["top_left_y"]
    x6 = datos[datos_list]["text_boxes"][2]["bottom_right_x"]
    y6 = datos[datos_list]["text_boxes"][2]["bottom_right_y"]
    draw.rectangle([(x5, y5), (x6, y6)],  outline=None)

    #Guardado de nueva imagen e impresión
    meme_texto.save(os.path.join('src', 'Repositorio_prueba' ,'imagen_con_cuadros_de_texto.png'))
    Image.open(os.path.join('src', 'Repositorio_prueba' ,'imagen_con_cuadros_de_texto.png'))
    return (x1, y1, x2, y2), (x3, y3, x4, y4), (x5, y5, x6, y6)