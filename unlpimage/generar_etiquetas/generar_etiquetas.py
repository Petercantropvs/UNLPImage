# Etiquetas

import PySimpleGUI as sg
import sys
import os

treedata = sg.TreeData()
photo_path = sg.PopupGetFolder('Seleccione la carpeta de imágenes')
# os.path.join('C:\\','Users','Usuario','Documents','Pedro','Origami')

# Función para construir el treedata (carpetas, subcarpetas y archivos)
def arbol(parent, directorio):
    folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

    for archivo in os.listdir(directorio):
        ruta = os.path.join(directorio, archivo)
        
        if os.path.isdir(ruta):    # Si es carpeta
            treedata.Insert(parent, ruta, archivo, values=[], icon=folder_icon)
            arbol(ruta, ruta)
        else:                         # Acá el values hay que completarlo con los tags
            treedata.Insert(parent, ruta, archivo, values=[os.stat(ruta).st_size], icon=file_icon)

def layout():
    arbol('',photo_path)
    frame_layout = [[sg.Image(size = (200,400), key = '-VISUALIZADOR-')],
                    [sg.Text('Tags:')],[sg.Text('', key = '-OUTPUT-')]]

    layout_l = sg.Column([[sg.Tree(data = treedata, headings = ['Tags',], auto_size_columns=True,
                    expand_x = True, expand_y = True, enable_events = True, key = '-TREE-')],
                        [sg.Text('Tag')],
                        [sg.Input(size=(50,1), key = '-NEWTAG-'),sg.Button('Agregar')],
                        [sg.Text('Texto descriptivo')],
                        [sg.Input(size=(50,1), key = '-ALGO-'),sg.Button('Agregar')]])

    layout_r = sg.Column([[sg.Push(), sg.Button('Volver', key = '-VOLVER-')],
                        [sg.Frame('Seleccione una imagen para visualizar',
                                    frame_layout, 
                                    background_color=sg.theme_button_color()[1], 
                                    size=(300,400),
                                    expand_x = True,
                                    expand_y = True,
                                    key = '-FRAME-')]])   
                       
    layout = [[sg.Text('Seleccione la imagen que desee etiquetar:')],
              [layout_l, layout_r], 
              [sg.Push(), sg.Button('Guardar')]]
    return layout

def ventana_etiquetas():
    window = sg.Window('Etiquetar imágenes', layout(), resizable=True, finalize=True)
    while True:
        event, values = window.read()
        
        ruta_imagen_sel = os.path.relpath(str(values['-TREE-']).strip('\'[]'), start = photo_path)
        
        window['-OUTPUT-'].update(values['-NEWTAG-'])
        window['-FRAME-'].update(ruta_imagen_sel)
        if not os.path.isdir(os.path.join(photo_path, ruta_imagen_sel)):
            window['-VISUALIZADOR-'].update(os.path.join(photo_path, ruta_imagen_sel))

        print(event, values)
        if event == sg.WIN_CLOSED or event == '-VOLVER-':
            break
            
    window.close()

if __name__ == '__main__':
    ventana_etiquetas()