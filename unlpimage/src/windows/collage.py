#Genedor de collage:
import PySimpleGUI as sg
import os
from src.windows.generar_etiquetas import ventana_etiquetas
from src.windows.crear_collage import creacion_collage
from src.default.pathing import templates_path
from src.default.setup import text_format15, text_format10
from src import function_registo

def layout_collage():
    templates_1, templates_2 = [[sg.Image(source = os.path.join(templates_path,'template-'+str(i)+'.png'), subsample=2,enable_events=True, key='-L'+str(i)+'-') for i in range(j,j+3)] for j in [1,4]]
    
    layout = [[sg.Text('Seleccioná el diseño de tu collage:', font = text_format15), sg.Push(), sg.Button('⬅ Volver', font = text_format15, key = '-VOLVER-')],
              [sg.Column([templates_1, templates_2], justification='center')],
              [sg.VPush()],[sg.Text('⚠ Recordá que las imágenes deben estar etiquetadas para añadirlas al collage!', font=text_format10)],
              [sg.Button('Ir a etiquetado 🏷', key = '-ETIQUETAS-')]]
    return layout

def seleccion_collage(perfil):
    """
    Esta función permite crear tus propios collages, eligiendo varias imágenes y cierto template de collage.
    Las imagenes a seleccionar se encuentran en el Resositorio de Imágenes (elegido en la ventana de Configuración),
    y los templates en la carpeta de default (proximamente....). 
    Los collages creados por los usuarios se guardarán en Directorio de collages.
    """
    window = sg.Window('Seleccioná tu template!', layout_collage(), resizable= True, grab_anywhere= True, finalize=True)
    window.set_min_size((600,550))
    while True:
        event, values = window.read()
        match event:
            case '-L1-' | '-L2-' | '-L3-' | '-L4-' | '-L5-' | '-L6-':
                window.Hide()
                creacion_collage(event, perfil)
                window.UnHide()
            case '-ETIQUETAS-':
                window.hide()
                accion = ventana_etiquetas(perfil)
                window.un_hide()
        if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
             window.close()
             break
    window.close()


if __name__ == '__main__':
    seleccion_collage('testrun')

