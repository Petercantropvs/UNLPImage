import PySimpleGUI as sg

text_format1 = {'font' : ('latin modern sansquotation', 15)}
text_format2 = {'font' : ('latin modern sansquotation', 10)}

def layout_ayuda():
    layout = [[sg.Text('Esta aplicación permite que crees tus propios memes y collages a partir de iamgenes guardadas en tu PC',**text_format2)],
             [sg.Text('y luego etiquetarlas para encontrarlas con mayor facilidad.',**text_format2)],
             [sg.Text('',**text_format2)],
             [sg.Text('Para elegir las carpetas donde guardar tus nuevas imágenes ingresa al menú de Configuración', **text_format2)],
             [sg.Text('',**text_format2)],
             [sg.Text('Crea tu usuario y empieza a divertirte',**text_format2)],
             [sg.Button("Volver", key='-VOLVER-', **text_format2)]]                    
    return layout

#El repositorio de imágenes será la carpeta de donde elegiremos las imagenes para hacer los memes y collages.
#Los directorios es elegir la carpeta a donde queremos los guarde.

def ventana_ayuda():
    window = sg.Window('Ayuda',layout_ayuda())
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
            break
    
    window.close()
 
if __name__ == "__main__":
       ventana_ayuda()
