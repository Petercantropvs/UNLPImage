import PySimpleGUI as sg
from src.default.setup import *


def layout_ayuda():
    layout =[[sg.Submit('Sobre la aplicación', key = '-APP-', **text_format10, size = (40,1))],
            [sg.Submit('Sobre perfiles', key = '-PERFIL-', **text_format10, size = (40,1))],
            [sg.Submit('Sobre configuración', key = '-CONF-', **text_format10, size = (40,1))],
            [sg.Submit('Sobre creación de collage/memes', key = '-CREAR-', **text_format10, size = (40,1))],
            [sg.Submit('Sobre etiquetado', key = '-TAG-', **text_format10, size = (40,1))],
            [sg.Text('\n¡Creá tu usuario y empezá a divertirte!\n',**text_format10,expand_x=True, justification='center')],
            [sg.Push(), sg.Button("Volver", key='-VOLVER-', **text_format10), sg.Push()]]                    
    return layout

####################################################################
def layout_app():
    layout =[[sg.Text('''UNLPImage Jun-2023

Este software es un manipulador de imágenes.
Permite la creación de perfiles para distintos usuarios.
El usuario podrá generar collages de imágenes o crear memes a partir de imágenes que guarden en un repositorio determinado por él.
Además brinda la opción de etiquetar éstas imagenes para que su búsqueda al momento de utilizar las funcionalidades del software sea más sencilla.

Requerimientos: 

Python v 3.11.x

Jupyter core packages

PySimpleGUI v 4.60.4
https://github.com/PySimpleGUI/PySimpleGUI

Pillow v 9.5.0
https://python-pillow.org

numpy v 1.24.3
https://www.numpy.org

matplotlib v 3.7.1
https://matplotlib.org

pandas v 2.0.2
https://pandas.pydata.org

wordcloud v 1.9.2
https://github.com/amueller/word_cloud''',**text_format10)],
            
            [sg.Button("Volver", key='-VOLVER-', **text_format10)]]                    
    return layout

####################################################################
def layout_perfil():
    layout =[[sg.Text('Al abrir la aplicación te encontrarás con los perfiles ya creados. Con el botón Ver más podrás acceder a los demás prefiles.',**text_format10)],
            [sg.Text('En caso de no tener perfil, clickea el signo + que te llevará a la creación de uno nuevo.',**text_format10)],
            [sg.Text('',**text_format10)],
            [sg.Text('Nuevo perfil',**text_format15)],
            [sg.Text('Completa la grilla con tus datos: nickname, nombre, edad y genero.',**text_format10)],
            [sg.Text('Debés tener en cuenta que el nickname no podrá ser modificado en la posterioridad.',**text_format10)],
            [sg.Text('',**text_format10)],
            [sg.Text('Editar perfil',**text_format15)],
            [sg.Text('Dentro de la ventana de inicio encontrarás la opción Editar perfil. ',**text_format10)],
            [sg.Text('Para editarlo debés clickear este botón o la foto con tu perfil. ',**text_format10)],
            [sg.Button("Volver", key='-VOLVER-', **text_format10)]]                    
    return layout


####################################################################
def layout_conf():
    layout =[[sg.Text('La ventana de configuración te permitirá elegir tus carpetas de preferencia para la busqueda y creación de imagenes.',**text_format10)],
            [sg.Text('',**text_format10)],
            [sg.Text('El botón Repositorio de imagenes, te permite elegir la carpeta inicial de la cual quieres elegir imagenenes para crear memes o collage.',**text_format10)],
            [sg.Text('Solo debés elegir la carpeta y presionar el botón Seleccionar.',**text_format10)],
            [sg.Text('',**text_format10)],
            [sg.Text('El botón Directorio de memes, te permite elegir la carpeta donde quieres guardar tus memes ya creados.',**text_format10)],
            [sg.Text('Solo debés elegir la carpeta y presionar el botón Seleccionar.',**text_format10)],
            [sg.Text('',**text_format10)],
            [sg.Text('El botón Directorio de collages, te permite elegir la carpeta donde quieres guardar tus collage ya creados.',**text_format10)],
            [sg.Text('Solo debés elegir la carpeta y presionar el botón Seleccionar.',**text_format10)],
            [sg.Text('',**text_format10)],
            [sg.Text('En todos los casos, al presionar Guardar, se guardaran tus cambios, y podrás usarlo cada vez que quieras usar la aplicación.',**text_format10)],
            [sg.Text('De igual forma, al presionar Cancelar, se cancelan los cambios elegidos, quedando guardada la última configuración.',**text_format10)],
            [sg.Button("Volver", key='-VOLVER-', **text_format10)]]                    
    return layout


####################################################################
def layout_crear():
    layout =[[sg.Text('Dentro de la ventana de Inicio, podrás elegir entre crear memes y crear collages',**text_format10)],
            [sg.Text('',**text_format10)],
            [sg.Text('Crear memes',**text_format15)],
            [sg.Text('En el menú de creación de memes, lo primero que deberás hacer es seleccionar la plantilla para el meme que deseas utilizar.',**text_format10)],
            [sg.Text('Tras seleccionar una plantilla, tendrás la opción de elegir una tipografía para tu texto, y deberás completar los cuadros de texto con lo que desees.',**text_format10)],
            [sg.Text('Luego, presiona el botón \'generar\' y tendrás una pestaña de previsualización de tu meme.',**text_format10)],
            [sg.Text('Presiona \'Guardar y salir\' si deseas conservarlo!',**text_format10)],
            [sg.Text('',**text_format10)],
            [sg.Text('Crear collage',**text_format15)],
            [sg.Text('En el menú de creación de collage, podrás elegir uno de entre los seis templates predefinidos para crear tu collage.',**text_format10)],
            [sg.Text('Tras elegir un template, deberás seleccionar en el menú \'seleccionar imágenes\' la posición de la imagen que deseas insertar en tu collage.',**text_format10)],
            [sg.Text('Para esto, deberás recordar que para poder hacer un collage con tus fotos primero deberás etiquetarlas a todas en \'generar etiquetas\'.',**text_format10)],
            [sg.Text('Con las imágenes ya etiquetadas, vé añadiendo tantas imágenes como te permita tu template a tu nuevo collage y añádele un título.',**text_format10)],
            [sg.Text('Precaución! No podrás añadir un título ni guardar tu collage si el template no está completo! Cargá todas las imágenes primero ;)',**text_format10)],
            [sg.Text('Para finalizar, presiona el botón \'Guardar\'. Listo! Ya podés ir a ver tu collage a la carpeta elegida :D',**text_format10)],
            [sg.Text('',**text_format15)],
            [sg.Text('Nota: Si tenés duda respecto a las carpetas de guardado, ver la ventanada de ayuda-configuración ;)',**text_format10)],
            [sg.Button("Volver", key='-VOLVER-', **text_format10)]]                    
    return layout


####################################################################

def layout_tag():
    layout =[[sg.Text('La ventana de creación de etiquetas te permitirá agregar etiquetas a las imagenes que tengas en el directorio elegido como repositorio de imagenes.',**text_format10)],
            [sg.Text('Si no tenés elegido un directorio como repositorio, deberás hacerlo en la ventana de configuración antes de empezar a etiquetar tus imagenes.',**text_format10)],
            [sg.Text('Estas etiquetas te facilitarán la búsqueda de imagenes para crear tus memes o collages.',**text_format10)],
            [sg.Text('Para ayudarte decidir cómo etiquetar tus imagenes favoritas, te mostramos información de la imagen',**text_format10)],
            [sg.Text('que creemos puede resultarte útil.',**text_format10)],
            [sg.Text('Tanto para visualizar la imagen como para ver información sobre ella sólo deberás hacer click en ella en la pantalla de la izquierda.',**text_format10)],
            [sg.Text('Una vez finalizado, presioná \'aceptar\' para guardar',**text_format10)],
            [sg.Button("Volver", key='-VOLVER-', **text_format10)]]      
    return layout

####################################################################
def ventana_ayuda():
    """ 
    Esta función abre una ventana de Ayuda para el usuario en la ejecución de la aplicación.
    Según el botón que apriete, recibirá mayor información respecto a un tema específico: 
    como ser Sobre la aplicación, Perfiles, Configuración, Generación de memes/collage y 
    etiquetado de imágenes.
    """
    accion = "Entró a ventana de Ayuda"
    window = sg.Window('Ayuda',layout_ayuda())
    while True:
        event, values = window.read()
        if event == '-APP-':
            accion = "Entró a ventana de Ayuda --> Ayuda sobre la app"
            window_app = sg.Window('Ayuda: Sobre la aplicación',layout_app())
            window.hide()
            while True:
                event1, values1 = window_app.read()
                if event1 == sg.WINDOW_CLOSED or event1 == '-VOLVER-':
                    break

            window_app.close()
            window.UnHide()
        if event == '-PERFIL-':
            accion = "Entró a ventana de Ayuda --> Ayuda sobre perfiles"
            window_perfil = sg.Window('Ayuda: Sobre perfiles',layout_perfil())
            window.hide()
            while True:
                event2, values2 = window_perfil.read()
                if event2 == sg.WINDOW_CLOSED or event2 == '-VOLVER-':
                    break
            window.UnHide()
            window_perfil.close()

        if event == '-CONF-':
            accion = "Entró a ventana de Ayuda --> Ayuda sobre configuración"
            window_conf = sg.Window('Ayuda: Sobre configuración',layout_conf())
            window.hide()
            while True:
                event3, values3 = window_conf.read()
                if event3 == sg.WINDOW_CLOSED or event3 == '-VOLVER-':
                    break
            window_conf.close()
            window.UnHide()     

        if event == '-CREAR-':
            accion = "Entró a ventana de Ayuda --> Ayuda sobre creación de memes y collage"
            window_crear = sg.Window('Ayuda: Sobre creación de memes/collages',layout_crear())
            window.hide()
            while True:
                event4, values = window_crear.read()
                if event4 == sg.WINDOW_CLOSED or event4 == '-VOLVER-':
                    break
            window.UnHide() 
            window_crear.close()    


        if event == '-TAG-':
            accion = "Entró a ventana de Ayuda --> Ayuda sobre etiquetado de imágenes"
            window_tag = sg.Window('Ayuda: Sobrobre etiquetado de imágenes',layout_tag())
            window.hide()
            while True:
                event5, values5 = window_tag.read()
                if event5 == sg.WINDOW_CLOSED or event5 == '-VOLVER-':
                    break
            window.UnHide() 
            window_tag.close()    

        if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
            break
    window.close()
    return accion
    
 
if __name__ == "__main__":
       ventana_ayuda()
