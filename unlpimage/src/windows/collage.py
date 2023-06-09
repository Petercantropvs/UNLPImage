#Genedor de collage:
import PySimpleGUI as sg
import json
import os
from src.windows.generar_etiquetas import ventana_etiquetas
from src.default.pathing import BASE_PATH, templates_path
from src.default.data import read_config
from src.default.setup import text_format15, text_format10

# [sg.Input(), sg.FilesBrowse("Seleccionar imagen", key='-SELECCIONAR-IMAGEN-',font = ('latin modern sansquotation', 10), initial_folder=ruta_repositorio, file_types=(("ALL Files", "*.*"),)), sg.Button('Finalizar',key='-FINSELECCION-',font = ('latin modern sansquotation', 10)) ],
#              [sg.Text('Selecciona el template para el nuevo collage',font = ('latin modern sansquotation', 10))],
#              [sg.Input(), sg.FilesBrowse("Seleccionar template",font = ('latin modern sansquotation', 10)) ],
            #Una vez generados los templates, hacemos la ruta, pues falta crear esta carpeta
            #[sg.Input(), sg.FilesBrowse(initial_folder=template_ruta, file_types=('*.png', '*.jpg'),)],

def layout_collage():
    ruta_repositorio, ruta_collages, ruta_memes = read_config()
    # breakpoint()
    layout = [[sg.Text('Seleccioná el diseño de tu collage:', font = text_format15), sg.Push(), sg.Button('⬅ Volver', font = text_format15, key = '-VOLVER-')],
              [sg.Column([[sg.Image(source = os.path.join(templates_path,'template-1.png'), subsample=2,enable_events=True, tooltip='Quiero este!', key='-L1-'), 
                           sg.Image(source = os.path.join(templates_path,'template-2.png'), subsample=2,enable_events=True, tooltip='Quiero este!', key='-L2-'), 
                           sg.Image(source = os.path.join(templates_path,'template-3.png'), subsample=2,enable_events=True, tooltip='Quiero este!', key='-L3-')],
                          [sg.Image(source = os.path.join(templates_path,'template-4.png'), subsample=2,enable_events=True, tooltip='Quiero este!', key='-L4-'), 
                           sg.Image(source = os.path.join(templates_path,'template-5.png'), subsample=2,enable_events=True, tooltip='Quiero este!', key='-L4-'), 
                           sg.Image(source = os.path.join(templates_path,'template-6.png'), subsample=2,enable_events=True, tooltip='Quiero este!', key='-L6-')]], 
                          justification='center')],
              [sg.Text('Recordá que las imágenes deben estar etiquetadas para añadirlas al collage!', font=text_format10)],
              [sg.VPush()],[sg.Button('Ir a etiquetado 🏷', key = '-ETIQUETAS-')]]
    return layout

def seleccion_collage(perfil):
    """
    Esta función permite crear tus propios collages, eligiendo varias imágenes y cierto template de collage.
    Las imagenes a seleccionar se encuentran en el Resositorio de Imágenes (elegido en la ventana de Configuración),
    y los templates en la carpeta de default (proximamente....). 
    Los collages creados por los usuarios se guardarán en Directorio de collages.
    """
    window = sg.Window('Crea tu collage', layout_collage(), resizable= True, grab_anywhere= True, finalize=True)
    window.set_min_size((580,550))
    while True:
        event, values = window.read()
        match event:
            case ['-L1-', '-L2-', '-L3-', '-L4-', '-L5-', '-L6-']:
                print('tomo el evento')
                print('seleccionó el template '+ event)
                # print(accion)
                pass
            case '-ETIQUETAS-':
                window.hide()
                accion = ventana_etiquetas(perfil)
                window.un_hide()
        if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
             accion = "Entró a generar un collage, pero no lo generó. "
             break
    window.close()
    return accion


if __name__ == '__main__':
    seleccion_collage('testrun')

