import PySimpleGUI as sg
import os
from src.default.pathing import BASE_PATH, templates_path
from src.default.data import read_config, dict_lector
from src.default.setup import text_format15, text_format10
from src.windows.generar_etiquetas import arbol
# directorio_collages = read_config()[1]
# relpath = os.path.relpath(os.path.join(dir_imagenes, archivo), start = BASE_PATH)

def imagenes_etiquetadas(parent, imagenes, metadata):
    
    dir_imagenes = read_config()[0]
    for archivo in os.listdir(dir_imagenes):
        imagenes.Insert(parent, key = archivo, text = archivo, values=[])
    return imagenes

def cant_botones(num):
    botones = []
    for n in range(1, num+1):
        botones.append(sg.Button('Seleccionar imagen '+str(n), font = text_format10, key = '-IMG'+str(n)+'-'))
    return botones

def layout(template, photo_path, metadata):
    match template:
        case '-L1-' | '-L2-':
            botones = cant_botones(2)
        case '-L3-' | '-L5-':
            botones = cant_botones(3)
        case '-L4-':
            botones = cant_botones(4)
        case '-L6-':
            botones = cant_botones(5)
    
    treedata = sg.TreeData()
    arbol('', photo_path, treedata, metadata)
    left_col = [[sg.Tree(data = treedata,headings= [], auto_size_columns=True, enable_events=True, visible=True, key='-TREE-')],
                botones,
                [sg.Text('Título:', font = text_format15)],
                [sg.Input('', enable_events= True, key = '-TITULO-')]]

    right_col = [[sg.Image(key = '-PREVIEW-')]]

    layout = [[sg.Text('Generar collage', font = text_format15), sg.Push(), sg.Button('⬅ Volver', font = text_format15, key = '-VOLVER-')],
              [sg.Column(left_col), sg.Column(right_col)],
              [sg.Push(), sg.Button('💾 Guardar', font = text_format15, key = '-GUARDAR-')]]

    return layout
    
def creacion_collage(template):
    metadata = dict_lector() # Cargo la info en tags.csv
    photo_path = read_config()[0]
    window = sg.Window('Creá tu collage!', layout(template, photo_path, metadata), resizable= True, finalize=True, enable_close_attempted_event= True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, '-VOLVER-'):
            if sg.popup_yes_no('Desea salir sin guardar?') == 'Yes':
                    window.close()
                    break

if __name__ == '__main__':
    creacion_collage('-L1-')

