import PySimpleGUI as sg
import os
import json
from src.default.pathing import BASE_PATH, templates_memes_path
from src.default.data import read_config
from src.default.data import read_memes 
from src.default.data import get_img_data_profiles as get_img_data
from PIL import Image, ImageTk, ImageFont, ImageDraw, ImageFont
from src.default.setup import *
from src.default.funciones_memes import tam_box, entra, calcular_tam_fuente, boxes_2, boxes_3
from src import function_registo


##############################################################################################

def layout_memes_templates():
    ruta_repositorio, ruta_collages, ruta_memes = read_config()
    col_1 =[
            [sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src', 'default','memes-templates', 'Batman_golpea_robin.png'), first = True), key='Batman_golpea_robin.png', enable_events=True, metadata=0 ),
             sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','default','memes-templates','hide_the_pain_harold.png'), first = True), key='hide_the_pain_harold.png', enable_events=True, metadata=0 ) ]
            ]
    
    
#images column
    col_2 = [
            [sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','default','memes-templates', 'novio_mira_otra_mujer.png'), first = True), key='novio_mira_otra_mujer.png', enable_events=True, metadata=0 ),
             sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','default','memes-templates','seguro_esta_pensando_en_otra.png'), first = True), key='seguro_esta_pensando_en_otra.png', enable_events=True, metadata=0 ) ]
            ]
    
    layout = [[sg.Text("Seleccione un template para crear un meme.", **text_format15)],[sg.Column(col_1)], [sg.Column(col_2)],[sg.Button('Volver', key='-VOLVER-')]]

    return layout

############################################################################################### 

def layout_crear_2box():
    col_1 = [
            #[sg.Text("Elegir tipografía"), sg.FileBrowse("Elegir tipografía",key='-FUENTE-', initial_folder=ruta_repositorio, file_types=(("TTF Files", "*.ttf"),))],
            [sg.Button("Elegir tipografía", key='-FUENTE-')],
            [sg.Text("Cuadro de texto 1")],
            [sg.InputText(key='-TEXTO1-')],
            [sg.Text("Cuadro de texto 2")],
            [sg.InputText(key='-TEXTO2-')],
            [sg.Button("Generar", key='-TEXTOSI_2box-'), sg.Button("Cancelar", key='-TEXTONO-')]
            ]
        
    col_2 = [ 
            
            [sg.Image((os.path.join(BASE_PATH,'src','default','memes-templates', 'imagen_con_cuadros_de_texto.png')), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ]
            ]

    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout

############################################################################################### 

def layout_crear_3box():
    col_1 = [
            [sg.Button("Elegir tipografía", key='-FUENTE-')],
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
            [sg.Image((os.path.join(BASE_PATH,'src','default','memes-templates', 'imagen_con_cuadros_de_texto.png')), key='-PIC-', enable_events=True, metadata=0, pad = (50,0,0,0) ) ]
            ]

    layout = [[sg.Column(col_1), sg.Column(col_2)]]
    return layout

def layout_fuentes():
    col_1 =[
            [sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src', 'default','flavor_sans.png'), first = True), key='-flavor-', enable_events=True, metadata=0 ),
             sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','default','hawaianas.png'), first = True), key='-hawaianas-', enable_events=True, metadata=0 ) ]
            ]
    
    
#images column
    col_2 = [
            [sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','default','invisible.png'), first = True), key='-invisible-', enable_events=True, metadata=0 ),
             sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','default','tommy.png'), first = True), key='-tommy-', enable_events=True, metadata=0 ) ]
            ]
    
    layout = [[sg.Text("Seleccione una fuente para crear el meme.", **text_format15)],[sg.Column(col_1)], [sg.Column(col_2)],[sg.Button('Volver', key='-VOLVER-')]]

    return layout

###############################################################################################

def layout_mostrar():
    layout = [[sg.Image((os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','meme_final.png')), key='-MEME-')],
             [sg.Button('Guardar y salir', key='-GUARDARMEME-'), sg.Button('Volver', key='-VOLVER2-')] ]          
    return layout


##############################################################################################
def ventana_meme(perfil):
    """ 
    Esta función abre una ventana de Generación de memes. A partir de un template seleccionado, 
    se le permitirá escribir textos en los cuadros de texto marcados en la pantalla 2.
    Una vez presionado Generar, se guardará el meme nuevo.
   
    """
    ruta_repositorio, ruta_collages, ruta_memes = read_config()
    datos = read_memes()
    templates_path = templates_memes_path

    confirm = ''
    window = sg.Window('Generador de memes',layout_memes_templates())
    while True:
        event1, values1 = window.read()
        if event1 == sg.WINDOW_CLOSED or event1 == '-VOLVER-':
            window.close()
            break
        if event1 == 'Batman_golpea_robin.png' or event1 == 'hide_the_pain_harold.png' or event1 == 'novio_mira_otra_mujer.png' or event1 == 'seguro_esta_pensando_en_otra.png':

            file_path = os.path.join(BASE_PATH,'src', 'default','memes-templates', event1)
            image_name = event1
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
                window_boxes = sg.Window('Generar memes', layout_crear_2box())

            elif image_name == "novio_mira_otra_mujer.png":
                resultado_funcion1 = boxes_3(draw, meme_cuadrados,2)
                window_boxes = sg.Window('Generar memes', layout_crear_3box())    

            meme_final = meme_original.copy()
            draw = ImageDraw.Draw(meme_final)
            

            while True:
                if confirm == 'No':
                    window.close()
                    break
                window.Hide()
                event2, values2 = window_boxes.read()
                if event2 == sg.WINDOW_CLOSED or event2 == '-VOLVER-' or event2 == '-TEXTONO-':
                    window_boxes.close()
                    window.UnHide()
                    break  
                if event2 == '-FUENTE-':
                    window_fuente = sg.Window('Seleccionar fuente', layout_fuentes())
                    while True:
                        event_f,values_f = window_fuente.read()
                        match event_f:
                            case('-flavor-'):
                                fuente_elegida = os.path.join(BASE_PATH,'src', 'default','memes-templates','fuentes','Flavor_sans.ttf')
                                window_fuente.close()
                                break
                            case('-hawaianas-'):
                                fuente_elegida = os.path.join(BASE_PATH,'src', 'default','memes-templates','fuentes','Hawainas.ttf')
                                window_fuente.close()
                                break
                            case('-invisible-'):
                                fuente_elegida = os.path.join(BASE_PATH,'src', 'default','memes-templates','fuentes','Invisible.ttf')
                                window_fuente.close()
                                break
                            case('-tommy-'):
                                fuente_elegida = os.path.join(BASE_PATH,'src', 'default','memes-templates','fuentes','Tommy.ttf')
                                window_fuente.close()
                                break
                        if event_f == sg.WINDOW_CLOSED or event_f == '-VOLVER-':
                                window_fuente.close()
                                break
            
                if event2 == '-TEXTOSI_2box-':
                   # fuente_elegida = values2['-FUENTE-']
                    texto1 = values2['-TEXTO1-']
                    texto2 = values2['-TEXTO2-']
                    print(texto1, texto2)
                    
                    try:
                        fuente = ImageFont.truetype(fuente_elegida, 200) #el tamaño
                    except UnboundLocalError:
                        fuente_elegida = os.path.join(BASE_PATH,'src', 'default','memes-templates','fuentes','Flavor_sans.ttf')
                        fuente = ImageFont.truetype(fuente_elegida, 200)

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
                
                if event2 == '-TEXTOSI_3box-':
                    #fuente_elegida = values2['-FUENTE-']
                    texto1 = values2['-TEXTO1-']
                    texto2 = values2['-TEXTO2-']
                    texto3 = values2['-TEXTO3-']
                    print(texto1, texto2, texto3)

                    try:
                        fuente = ImageFont.truetype(fuente_elegida, 200) #el tamaño
                    except UnboundLocalError:
                        fuente_elegida = os.path.join(BASE_PATH,'src', 'default','memes-templates','fuentes','Flavor_sans.ttf')
                        fuente = ImageFont.truetype(fuente_elegida, 200)  
               
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
                if event2 == '-TEXTOSI_2box-' or event2 == '-TEXTOSI_3box-':
                    while True:
                        window_boxes.Hide()
                        event3, values3 = window_mostrar.read()
                        if event3 == sg.WINDOW_CLOSED or event3 == '-VOLVER2-':
                            window_mostrar.close()
                            window_boxes.UnHide()
                            os.remove(os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','meme_final.png'))
                            texto1=None
                            texto2=None
                            texto3=None
                            meme_final = meme_original.copy()
                            draw = ImageDraw.Draw(meme_final)
                            break
                        elif event3 == '-GUARDARMEME-':
                            confirm = sg.popup_yes_no('¿Desea guardar la imagen?', title='Guardar imagen')
                            if confirm == 'No':
                                window_mostrar.close()
                                window_boxes.UnHide()
                                texto1=None
                                texto2=None
                                texto3=None
                                meme_final = meme_original.copy()
                                draw = ImageDraw.Draw(meme_final)
                                break
                            if confirm == 'Yes':
                                filename = sg.popup_get_text('Ingrese el nombre de archivo:', title='Guardar imagen')
    
                                if filename:
                             # Aquí puedes escribir la lógica para guardar la imagen con el nombre de archivo ingresado
                                    print('Imagen guardada con el nombre:', filename)
                                    meme_final.save(os.path.join(BASE_PATH, 'src', 'Repositorio_prueba', filename + '.png'))
    
                                    Action = 'Generó un meme'
                                    Values = [image_name]
                                    
                                    if image_name == "novio_mira_otra_mujer.png":
                                        Texts = texto1+' '+texto2+' '+texto3
                                    else:
                                        Texts = texto1+' '+texto2
                                    function_registo(perfil, Action, Values, Texts)
                                    confirm = sg.popup_yes_no('¿Desea seguir generando memes?', title='Crear memes')
                                    if confirm == 'Yes':
                                        window_mostrar.close()
                                        window_boxes.close()
                                        window.UnHide()
                                        os.remove(os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','meme_final.png'))
                                        os.remove(os.path.join(BASE_PATH,'src','default','memes-templates', 'imagen_con_cuadros_de_texto.png'))
                                        
                                    if confirm == 'No':
                                        window_mostrar.close()
                                        window_boxes.close()
                                        #window.close()
                                        os.remove(os.path.join(BASE_PATH, 'src', 'Repositorio_prueba','meme_final.png'))
                                        os.remove(os.path.join(BASE_PATH,'src','default','memes-templates', 'imagen_con_cuadros_de_texto.png'))
                                        

                                    break
    

#
#############################################################################

if __name__ == "__main__":
       ventana_meme()


