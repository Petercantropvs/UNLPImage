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
from src.windows.funciones_memes import tam_box, entra, calcular_tam_fuente, boxes_2, boxes_3

#archivo_memes = open('template_meme.json', 'r')
#datos = json.load(archivo_memes)
             
ruta_repositorio, ruta_collages, ruta_memes = read_config()
datos = read_memes()
templates_path = templates_memes_path


##############################################################################################

def layout_memes_prueba():
    ruta_repositorio, ruta_collages, ruta_memes = read_config()
    layout = [[sg.Text('Seleccioná el tempate de tu meme:', font = text_format15), sg.Button('⬅ Volver', font = text_format15, key = '-VOLVER-')], 
            [sg.Image(os.path.join('src', 'default','todos_templates_prueba.png'))],
            [sg.Button('Seleccionar', key='-GENERAR-')]]
    return layout


############################################################################################### 
def layout_crear_2box():
    col_1 = [
            [sg.Text("Elegir tipografía"), sg.FileBrowse("Elegir tipografía",key='-FUENTE-', initial_folder=ruta_repositorio, file_types=(("TTF Files", "*.ttf"),))],
            [sg.Text("Cuadro de texto 1")],
            [sg.InputText(key='-TEXTO1-')],
            [sg.Text("Cuadro de texto 2")],
            [sg.InputText(key='-TEXTO2-')],
            [sg.Button("Generar", key='-TEXTOSI_2box-'), sg.Button("Cancelar", key='-TEXTONO-'),]
            ]
        
    col_2 = [ 
            [sg.Button('Volver', key='-VOLVER-')],            
            [sg.Image((os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','imagen_con_cuadros_de_texto.png')), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ]
            ]

    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout

############################################################################################### 
def layout_crear_3box():
    col_1 = [
            [sg.Text("Elegir tipografía"), sg.FileBrowse("Elegir tipografía",key='-FUENTE-', initial_folder=ruta_repositorio, file_types=(("TTF Files", "*.ttf"),))],
            [sg.Text("Cuadro de texto 1")],
            [sg.InputText(key='-TEXTO1-')],
            [sg.Text("Cuadro de texto 2")],
            [sg.InputText(key='-TEXTO2-')],
            [sg.Text("Cuadro de texto 3")],
            [sg.InputText(key='-TEXTO3-')],
            [sg.Button("Generar", key='-TEXTOSI_3box-'), sg.Button("Cancelar", key='-TEXTONO-'),]
            ]
        
    col_2 = [ 
            [sg.Button('Volver', key='-VOLVER-')],            
            [sg.Image((os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','imagen_con_cuadros_de_texto.png')), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ]
            ]

    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout
###############################################################################################

def layout_mostrar():
    layout = [[sg.Image((os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','meme_final.png')), key='-MEME-')],
             [sg.Button('Guardar y salir', key='-GUARDARMEME-'), sg.Button('Volver', key='-VOLVER2-')] ]          
    return layout


##############################################################################################
def ventana_meme():
    """ 
    Esta función abre una ventana de Generación de memes. A partir de un template seleccionado, 
    se le permitirá escribir textos en los cuadros de texto marcados en la pantalla 2.
    Una vez presionado Generar, se guardará el meme nuevo.
   
    """
    window = sg.Window('Generador de memes',layout_memes_prueba())
    while True:
        event1, values1 = window.read()
        if event1 == sg.WINDOW_CLOSED or event1 == '-VOLVER-':
            break
        if event1 == '-GENERAR-':
            folder_path = 'BASE_PATH'
            file_types = [('Imagen', '*.png'), ('Imagen', '*.jpg')]
            file_path = sg.popup_get_file('Seleccionar imagen', initial_folder=ruta_repositorio, file_types=file_types)
            if file_path:
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

            elif image_name == "novio_mira_otra_mujer.png":
                resultado_funcion1 = boxes_3(draw, meme_cuadrados,2)
                window_boxes = sg.Window('Generar memes', layout_crear_3box())    

            meme_final = meme_original.copy()
            draw = ImageDraw.Draw(meme_final)
            
            while True:
                event2, values2 = window_boxes.read()
                if event2 == sg.WINDOW_CLOSED or event2 == '-VOLVER-' or event2 == '-TEXTONO-':
                    break    
            
                elif event2 == '-TEXTOSI_2box-':
                    fuente_elegida = values2['-FUENTE-']
                    texto1 = values2['-TEXTO1-']
                    texto2 = values2['-TEXTO2-']
                    print(texto1, texto2)
                    
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
                
                elif event2 == '-TEXTOSI_3box-':
                    fuente_elegida = values2['-FUENTE-']
                    texto1 = values2['-TEXTO1-']
                    texto2 = values2['-TEXTO2-']
                    texto3 = values2['-TEXTO3-']
                    print(texto1, texto2, texto3)
            

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
            
                meme_final.save(os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','meme_final.png'))
                Image.open(os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','meme_final.png'))
            
                window_mostrar = sg.Window('Meme final', layout_mostrar())
                #window_boxes.hide()

                while True:
                    event3, values3 = window_mostrar.read()
                    if event3 == sg.WINDOW_CLOSED or event3 == '-VOLVER2-':
                        break
                        #window_boxes.Unhide()
                    elif event3 == '-GUARDARMEME-':
                        confirm = sg.popup_yes_no('¿Desea guardar la imagen?', title='Guardar imagen')
                        if confirm == 'Yes':
                            filename = sg.popup_get_text('Ingrese el nombre de archivo:', title='Guardar imagen')
                            if filename:
                         # Aquí puedes escribir la lógica para guardar la imagen con el nombre de archivo ingresado
                                print('Imagen guardada con el nombre:', filename)
                                meme_final.save(os.path.join(BASE_PATH, 'src', 'Repositorio_prueba', filename + '.png'))

                                Action = 'Generó un meme'
                                Values = image_name

                                if image_name == "novio_mira_otra_mujer.png":
                                    Texts = texto1, texto2, texto3
                                else:
                                    Texts = texto1, texto2

                        break


                   #window_boxes.UnHide()
                window_mostrar.close()
                os.remove(os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','meme_final.png'))
                os.remove(os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','imagen_con_cuadros_de_texto.png'))
            window_boxes.close()
        window.close()
    
    #window.close()
    return Action, Values, Texts


#
#############################################################################

if __name__ == "__main__":
       ventana_meme()


