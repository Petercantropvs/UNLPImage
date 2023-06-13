#Segunda natalla de memes
import PySimpleGUI as sg
import os
import json
from src.default.pathing import BASE_PATH, templates_memes_path
from src.default.data import read_config
from src.default.data import read_memes 
#from generar_etiquetas import arbol
#from src.windows import generar_etiquetas
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
    meme_texto.save('imagen_con_cuadros_de_texto.png')
    Image.open('imagen_con_cuadros_de_texto.png')
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
    meme_texto.save(ruta_memes/'imagen_con_cuadros_de_texto.png')
    Image.open(ruta_memes/'imagen_con_cuadros_de_texto.png')
    return (x1, y1, x2, y2), (x3, y3, x4, y4), (x5, y5, x6, y6)


#BASE_PATH, 'src', 'users-data', 'users.json'
##############################################################################################
#def layout_memes1():
#    col_1 = [
#            [sg.Button('Selecciona un template', key='-TEMPLATE-', initial_folder= ruta_repositorio)],
#            ]   
#    col_2 = [
#            [sg.Button('Volver', key='-VOLVER-')],
#            [sg.Text('Previsualización:')],
#            [sg.Image(key='-IMAGE-', size=(150, 150))],
#            [sg.Button('Generar', key='-GENERAR-')]
#            ]
#    layout = [[sg.Column(col_1), sg.Column(col_2)]]
#    return layout


def layout_memes_prueba():
    ruta_repositorio, ruta_collages, ruta_memes = read_config()
    layout = [[sg.Text('Seleccioná el tempate de tu meme:', font = text_format15), sg.Button('⬅ Volver', font = text_format15, key = '-VOLVER-')], 
            [sg.Image(source = os.path.join(templates_memes_path,'todos_templates_prueba.png'))],
            [sg.Button('Seleccionar', key='-GENERAR-')]]
    return layout


############################################################################################### 
def layout_crear_2box():
    col_1 = [
            [sg.Text("Elegir tipografía"), sg.FileBrowse("Elegir tipografía",key='-FUENTE-', initial_folder=ruta_repositorio, file_types=(("TTF Files", "*.ttf"),))],
            [sg.Button("Aceptar", key='-OKFUENTE-'), sg.Button("Cancelar")],
            [sg.Text("Cuadro de texto 1")],
            [sg.InputText(key='-TEXTO1-')],
            [sg.Text("Cuadro de texto 2")],
            [sg.InputText(key='-TEXTO2-')],
            [sg.Button("Generar", key='-TEXTOSI-'), sg.Button("Cancelar", key='-TEXTONO-'),]
            ]
        
    col_2 = [ 
            [sg.Button('Volver', key='-VOLVER-')],            
            [sg.Image(('imagen_con_cuadros_de_texto.png'), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ]
            ]

    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout

############################################################################################### 
def layout_crear_3box():
    col_1 = [
            [sg.Text("Elegir tipografía"), sg.FileBrowse("Elegir tipografía",key='-FUENTE-', initial_folder=ruta_repositorio, file_types=(("TTF Files", "*.ttf"),))],
            [sg.Button("Aceptar", key='-OKFUENTE-'), sg.Button("Cancelar")],
            [sg.Text("Cuadro de texto 1")],
            [sg.InputText(key='-TEXTO1-')],
            [sg.Text("Cuadro de texto 2")],
            [sg.InputText(key='-TEXTO2-')],
            [sg.Text("Cuadro de texto 3")],
            [sg.InputText(key='-TEXTO3-')],
            [sg.Button("Generar", key='-TEXTOSI-'), sg.Button("Cancelar", key='-TEXTONO-'),]
            ]
        
    col_2 = [ 
            [sg.Button('Volver', key='-VOLVER-')],            
            [sg.Image(('imagen_con_cuadros_de_texto.png'), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ]
            ]

    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout
###############################################################################################
def layout_mostrar():
    layout = [[sg.Image(('meme_final.png'), key='-MEME-', enable_events=True, metadata=0, pad = (50,0,0,0) )],
             [sg.Button('Guardar y salir', key='-GUARDARMEME-'), sg.Button('Volver', key='-VOLVER2-')] ]          
    return layout


##############################################################################################
def ventana_meme():
    """ 
    Esta función abre una ventana de Generación de memes. A partir de un template seleccionado, 
    se le permitirá escribir textos en los cuadros de texto marcados en la pantalla 2.
    Una vez presionado Generar, se guardará el meme nuevo.
   
    """
#   accion = "Entró a ventana de memes"
    window = sg.Window('Generador de memes',layout_memes_prueba())
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
            accion = "Entró a generar un meme y no lo generó."
            break
        if event == '-GENERAR-':
            folder_path = 'BASE_PATH'
            file_types = [('Imagen', '*.png'), ('Imagen', '*.jpg')]
            file_path = sg.popup_get_file('Seleccionar imagen', initial_folder=ruta_repositorio, file_types=file_types)
            if file_path:
                #window['-IMAGE-'].update(filename=file_path)
                image_name = os.path.basename(file_path)
                print("Imagen seleccionada:", image_name)
    
            color_relleno = (0, 0, 0)  # (R, G, B)
            meme_original = Image.open(file_path) 
            meme_cuadrados = meme_original.copy()
            draw = ImageDraw.Draw(meme_cuadrados)
            if image_name == "Batman_golpea_robin.png":
                resultado_funcion1 = boxes_2(draw, meme_cuadrados, 0)
                window_boxes = sg.Window('Generar memes', layout_crear_2box())

            elif image_name == "hide_the_pain_harold.png":
                resultado_funcion1 = boxes_2(draw, meme_cuadrados, 1)
                window_boxes = sg.Window('Generar memes', layout_crear_2box())

            elif image_name == "seguro_esta_pensando_en_otra.png":
                resultado_funcion1 = boxes_2(draw,meme_cuadrados, 3)
                window = sg.Window('Generar memes', layout_crear_2box())

            while True:
                event, values = window_boxes.read()
                if event == sg.WINDOW_CLOSED or event == '-VOLVER-' or event== '-TEXTONO-':
                    #accion = "algo"
                    break    
            
                elif event == '-TEXTOSI-':
                    fuente_elegida = values['-FUENTE-']
                    texto1 = values['-TEXTO1-']
                    texto2 = values['-TEXTO2-']
                    print(texto1, texto2)
        
                    meme_final = meme_original.copy()
                    draw = ImageDraw.Draw(meme_final)
                    fuente = ImageFont.truetype(fuente_elegida, 200) #el tamaño
        
                    x1, y1, x2, y2 = resultado_funcion1[0]
                    x3, y3, x4, y4 = resultado_funcion1[1]
        
                    tam_box(x1, y1, x2, y2)
                    tam_box(x3, y3, x4, y4)
        
                    draw.textbbox((x1,y1), texto1, font=fuente)
                    draw.textbbox((x3,y3), texto2, font=fuente)
        
                    fuente_ajustada_1 = calcular_tam_fuente(draw, texto1, fuente_elegida, (x1,y1,x2,y2),)
                    fuente_ajustada_2 = calcular_tam_fuente(draw, texto2, fuente_elegida, (x3,y3,x4,y4),)
        
                    draw.text((x1,y1), texto1, font=fuente_ajustada_1,fill=color_relleno)
                    draw.text((x3,y3), texto2, font=fuente_ajustada_2,fill=color_relleno)
        
                    meme_final.save(ruta_memes/'meme_final.png')
                    Image.open(ruta_memes/'meme_final.png')           
        
                    window_mostrar = sg.Window('Meme final', layout_mostrar())
                    #window_boxes.hide()
                    while True:
                        event2, values2 = window_mostrar.read()
                        if event2 == sg.WINDOW_CLOSED or event2 == '-VOLVER2-':
                            os.remove(ruta_memes/'meme_final.png')
                            break
                        elif event2 == '-GUARDARMEME-':
                            sg.popup('Imagen guardada con éxito')
                            window_boxes.close()
                            break
                    os.remove(ruta_memes/'imagen_con_cuadros_de_texto.png')
                    window_mostrar.close()
            window.close()

            
            if image_name == "novio_mira_otra_mujer.png":
                resultado_funcion1 = boxes_3(draw, meme_cuadrados,2)
                window_boxes = sg.Window('Generar memes', layout_crear_3box())
        
                while True:
                    event, values = window_boxes.read()
                    if event == sg.WINDOW_CLOSED or event == '-VOLVER-' or event== '-TEXTONO-':
                        #accion = "algo"
                        break    
                
                    elif event == '-TEXTOSI-':
                        fuente_elegida = values['-FUENTE-']
                        texto1 = values['-TEXTO1-']
                        texto2 = values['-TEXTO2-']
                        texto3 = values['-TEXTO3-']
                        print(texto1, texto2, texto3)
            
                        #meme_original = Image.open(image_name)  #Cambiarlo por camino
                        meme_final = meme_original.copy()
                        draw = ImageDraw.Draw(meme_final)
                        fuente = ImageFont.truetype(fuente_elegida, 200) #el tamaño    
               
                        x1, y1, x2, y2 = resultado_funcion1[0]
                        x3, y3, x4, y4 = resultado_funcion1[1] 
                        x5, y5, x6, y6 = resultado_funcion1[2] 
            
                        tam_box(x1, y1, x2, y2)
                        tam_box(x3, y3, x4, y4)
                        tam_box(x5, y5, x6, y6)
            
                        draw.textbbox((x1,y1), texto1, font=fuente)
                        draw.textbbox((x3,y3), texto2, font=fuente)
                        draw.textbbox((x5,y5), texto3, font=fuente)
            
                        fuente_ajustada_1 = calcular_tam_fuente(draw, texto1, fuente_elegida, (x1,y1,x2,y2),)
                        fuente_ajustada_2 = calcular_tam_fuente(draw, texto2, fuente_elegida, (x3,y3,x4,y4),)
                        fuente_ajustada_3 = calcular_tam_fuente(draw, texto3, fuente_elegida, (x5,y5,x6,y6),)
            
                        draw.text((x1,y1), texto1, font=fuente_ajustada_1,fill=color_relleno)
                        draw.text((x3,y3), texto2, font=fuente_ajustada_2,fill=color_relleno)
                        draw.text((x5,y5), texto3, font=fuente_ajustada_3,fill=color_relleno)
            
                        meme_final.save('meme_final.png')
                        Image.open('meme_final.png')           
            
                        window_mostrar = sg.Window('Meme final', layout_mostrar())
                        window_boxes.hide()
                        while True:
                            event2, values2 = window_mostrar.read()
                            if event2 == sg.WINDOW_CLOSED or event2 == '-VOLVER2-':
                                os.remove(BASE_PATH, 'src', 'memes', 'meme_final.png')
                                break
                            elif event2 == '-GUARDARMEME-':
                                sg.popup('Imagen guardada con éxito')
                                window_boxes.close()
                                break

                        #window_boxes.UnHide()
                        os.remove('imagen_con_cuadros_de_texto.png')
                        window_mostrar.close()
                window.close()
    
    window.close()
    return


 #   return texto2, texto1, image_name, fuente_elegida
#
#############################################################################

if __name__ == "__main__":
       ventana_meme()




