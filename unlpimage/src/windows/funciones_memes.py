#Segunda natalla de memes
import PySimpleGUI as sg
import os
import json
from src.default.pathing import BASE_PATH, templates_memes_path
from src.default.data import read_config
from src.default.data import read_memes 
from PIL import Image, ImageTk, ImageFont, ImageDraw, ImageFont

             
ruta_repositorio, ruta_collages, ruta_memes = read_config()
datos = read_memes()
templates_path = templates_memes_path

##########################################################################################################
#Funciones auxliliares: 

def tam_box(x1,y1,x2,y2):
    """Esta función calcula el tamaño del box de texto, siendo sus argumentos:
        x1, y1= valores de arriba a la izquiera del rectángulo
        x2 y2= valores de abajo a la derecha del rectángulo
        Devuelve: ancho=x2-x1, alto=y2-y1
     """
    return(x2-x1,y2-y1)

##########################################################################################################
def entra(contenedor, contenido):
    """
    Defino lo que es el contenedor = cuadro de texto, y el contenido = texto.
    Y chequea si el tamaño de uno entra dentr del otro.
    """
    return contenido[0] <= contenedor[0] and contenido[1] <= contenedor[1]

##########################################################################################################
def calcular_tam_fuente(draw, texto, path_fuente, box):
    """
    Calcula que el tamaño de la tipografía entre en el cuadro de texto, usando la funcion anterior.
    Para la fuente elegida, la va moviendo de 5 en 5, hasta que encaje en el tamaño de la caja de texto.
    Iterará hasta encontrar el tamaño máximo que pueda entrar.
    Una vez encontrado el valor, me devuelve la fuente de ese tamaño. 
    """
    tam_contenedor = tam_box(*box)

    for tam in range (200, 20, -5):
        fuente = ImageFont.truetype(path_fuente, tam)
        box_texto = draw.textbbox((0,0), texto, font=fuente)
        tam_box_texto = tam_box(*box_texto)
        if entra(tam_contenedor, tam_box_texto):
            return fuente
    return fuente

##########################################################################################################
def boxes_2(draw, meme_texto, datos_list):
    """
    Esta funcion asigna los valores de las coordenadas del cuadrado de texto leídos a travez del archivo json,
    en el caso de tener solo dos cuadros de textos.
    datos tiene guardada la lista de diccionarios
    [datos_list] => asigna el valor de la lsita de disccionarios según el template elegido: 0, 1,2,3.

    x1, y1= valores de arriba a la izquiera del rectángulo, primer tupla de coordenadas (índice 0)
    x2 y2= valores de abajo a la derecha del rectángulo, primer tupla de coordenadas (índice 0)
    x3, y3= valores de arriba a la izquiera del rectángulo,  segunda tupla de coordenadas(índice 1)
    x4 y4= valores de abajo a la derecha del rectángulo, segunda tupla de coordenadas (índice 1)

    Luego, crea y guarda una imagen con los cuadros de textos.
    Devuelve, las tuplas de coordenadas nombradas antes.
    """
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
    meme_texto.save(os.path.join(BASE_PATH,'src','default','memes-templates', 'imagen_con_cuadros_de_texto.png'))
    Image.open(os.path.join(BASE_PATH,'src','default','memes-templates', 'imagen_con_cuadros_de_texto.png'))
    return (x1, y1, x2, y2), (x3, y3, x4, y4)

def boxes_3(draw,meme_texto, datos_list):
    """
    sta funcion asigna los valores de las coordenadas del cuadrado de texto leídos a travez del archivo json,
    en el caso de tener tres cuadros de textos.
    datos tiene guardada la lista de diccionarios
    [datos_list] => asigna el valor de la lsita de disccionarios según el template elegido: 0, 1,2,3.

    x1,y1 = valores de arriba a la izquiera del rectángulo, primer tupla de coordenadas (índice 0)
    x2 y2 = valores de abajo a la derecha del rectángulo, primer tupla de coordenadas (índice 0)
    x3,y3 = valores de arriba a la izquiera del rectángulo,  segunda tupla de coordenadas(índice 1)
    x4 y4 = valores de abajo a la derecha del rectángulo, segunda tupla de coordenadas (índice 1)
    x5,y5 = valores de arriba a la izquiera del rectángulo,  segunda tupla de coordenadas(índice 2)
    x6,y6= valores de abajo a la derecha del rectángulo, segunda tupla de coordenadas (índice 2)

    Luego, crea y guarda una imagen con los cuadros de textos.
    Devuelve, las tuplas de coordenadas nombradas antes.
    """
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
    meme_texto.save(os.path.join(BASE_PATH,'src','default','memes-templates', 'imagen_con_cuadros_de_texto.png'))
    Image.open(os.path.join(BASE_PATH,'src','default','memes-templates', 'imagen_con_cuadros_de_texto.png'))
    return (x1, y1, x2, y2), (x3, y3, x4, y4), (x5, y5, x6, y6)

##########################################################################################################
def divide_text(text, width, font):
    words = text.split()
    lines = []
    current_line = words[0]
    for word in words[1:]:
        if font.getsize(current_line + ' ' + word)[0] <= width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

