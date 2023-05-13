import PySimpleGUI as sg
from src.default.setup import *


def layout_ayuda():
    layout =[[sg.Submit('Sobre la aplicación', key = '-APP-', **text_format10)],
            [sg.Submit('Sobre perfiles', key = '-PERFIL-', **text_format10)],
            [sg.Submit('Sobre configuración', key = '-CONF-', **text_format10)],
            [sg.Submit('Sobre creación de collage/memes', key = '-CREAR-', **text_format10)],
            [sg.Submit('Sobre etiquetado', key = '-TAG-', **text_format10)],
            [sg.Text('',**text_format10)],
            [sg.Text('¡Creá tu usuario y empezá a divertirte!',**text_format10)],
            [sg.Button("Volver", key='-VOLVER-', **text_format10)]]                    
    return layout

####################################################################
def layout_app():
    layout =[[sg.Text('''UNLPImage 5-2023

Este software es un manipulador de imágenes.
Permite la creación de perfiles para distintos usuarios.
El usuario podrá generar collages de imágenes o crear memes a partir de imágenes que guarden en un repositorio determinado por él.
Además brinda la opción de etiquetar éstas imagenes para que su búsqueda al momento de utilizar las funcionalidades del software sea más sencilla.

Versión de muestra. Actualmente sólo permite el etiquetado de imagenes, elección de los directorios sobre los que se trabajará y creación, selección y edición de perfiles. 

Liberías utilizadas: 

PySimpleGUI v 4.60.4
https://github.com/PySimpleGUI/PySimpleGUI

Pillow v 9.5.0
https://python-pillow.org''',**text_format10)],
            
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
            [sg.Text('En el botón de seleccionar imagen, te mandará al directorio que elegiste como Repositorio de imagenes (para más información, ver la ventanada de ayuda-configuración).',**text_format10)],
            [sg.Text('Elegís la imagen requerida, y presionás seleccionar.',**text_format10)],
            [sg.Text('Luego, debés escribir la frase que querés agregarle a tu meme.',**text_format10)],
            [sg.Text('Al presionar el botón Generar, el meme será generado y almacenado en la carpeta Directorio de memes.',**text_format10)],
            [sg.Text('',**text_format10)],
            [sg.Text('Crear collage',**text_format15)],
            [sg.Text('En el botón de seleccionar imagen, te mandará al directorio que elegiste como Repositorio de imagenes (para más información, ver la ventanada de ayuda-configuración).',**text_format10)],
            [sg.Text('Elegís la imagen requerida, y presionás Seleccionar. Puedes hacerlo tantas veces como imágenes quieras elegir.',**text_format10)],
            [sg.Text('Al finalizar la selección, presiona Finalizar. Las imagenes elegidas aparecerán escritas en pantalla.',**text_format10)],
            [sg.Text('Finalmente, elige el template entre los disponibles dados por la propia aplicación.',**text_format10)],
            [sg.Text('Debes tener en cuenta que no podrás generar templates nuevos.',**text_format10)],
            [sg.Text('Al presionar el botón Generar, el collage será generado y almacenado en la carpeta Directorio de memes.',**text_format10)],
            [sg.Text('',**text_format15)],
            [sg.Text('Nota: Si tenés duda respecto a las carpetas de guardado, ver la ventanada de ayuda-configuración).',**text_format10)],
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
