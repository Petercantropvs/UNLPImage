import PySimpleGUI as sg

text_format1 = {'font' : ('latin modern sansquotation', 15)}
text_format2 = {'font' : ('latin modern sansquotation', 10)}

def layout_ayuda():
    layout =[[sg.Text('Esta aplicación permite que crees tus propios memes y collages a partir de iamgenes guardadas en tu PC',**text_format2)],
            [sg.Text('y luego etiquetarlas para encontrarlas con mayor facilidad.',**text_format2)],
            [sg.Text('',**text_format2)],
            [sg.Submit('Sobre la aplicación', key = '-APP-', **text_format2)],
            [sg.Submit('Sobre perfiles', key = '-PERFIL-', **text_format2)],
            [sg.Submit('Sobre configuración', key = '-CONF-', **text_format2)],
            [sg.Submit('Sobre creación de collage/memes', key = '-CREAR-', **text_format2)],
            [sg.Submit('Sobre etiquetado', key = '-TAG-', **text_format2)],
            [sg.Text('',**text_format2)],
            [sg.Text('¡Crea tu usuario y empieza a divertirte!',**text_format2)],
            [sg.Button("Volver", key='-VOLVER-', **text_format2)]]                    
    return layout

####################################################################
def layout_app():
    layout =[[sg.Text('Esta aplicación permite que crees tus propios memes y collages a partir de iamgenes guardadas en tu PC',**text_format2)],
            [sg.Text('y luego etiquetarlas para encontrarlas con mayor facilidad.',**text_format2)],
            [sg.Button("Volver", key='-VOLVER-', **text_format2)]]                    
    return layout

  ###   NOTAR QUE ACÀ DICE LO MISMO QUE AFUERA. SUPONGO Q ABRIA Q PONER ALGO DE COMO CORRER LA APLICACION EN REAIDAD.  

####################################################################
def layout_perfil():
    layout =[[sg.Text('Al abrir la aplicación te encontrarás con los perfiles ya creados. Con el botón Ver más podrás acceder a los demás prefiles.',**text_format2)],
            [sg.Text('En caso de no tener perfil, clickea el signo + que te llevará a la creación de uno nuevo.',**text_format2)],
            [sg.Text('',**text_format2)],
            [sg.Text('Nuevo perfil',**text_format1)],
            [sg.Text('Completa la grilla con tus datos: nickname, nombre, edad y genero.',**text_format2)],
            [sg.Text('Debés tener en cuenta que el nickname no podrá ser modificado en la posterioridad.',**text_format2)],
            [sg.Text('',**text_format2)],
            [sg.Text('Editar perfil',**text_format1)],
            [sg.Text('Dentro de la ventana de inicio encontrarás la opción Editar perfil. ',**text_format2)],
            [sg.Text('Para editarlo debés clickear este botón o la foto con tu perfil. ',**text_format2)],
            [sg.Text('Debés tener en cuenta que el nickname no podrá ser modificado en la posterioridad.',**text_format2)],
            [sg.Button("Volver", key='-VOLVER-', **text_format2)]]                    
    return layout


####################################################################
def layout_conf():
    layout =[[sg.Text('La ventana de configuración te permitirá elegir tus carpetas de preferencia para la busqueda y creación de im.',**text_format2)],
            [sg.Text('',**text_format2)],
            [sg.Text('El botón Repositorio de imagenes, te permite elegir la carpeta inicial de la cual quieres elegir imagenenes para crear memes o collage.',**text_format2)],
            [sg.Text('Solo debés elegir la carpeta y presionar el botón Seleccionar.',**text_format2)],
            [sg.Text('',**text_format2)],
            [sg.Text('El botón Directorio de memes, te permite elegir la carpeta donde quieres guardar tus memes ya creados.',**text_format2)],
            [sg.Text('Solo debés elegir la carpeta y presionar el botón Seleccionar.',**text_format2)],
            [sg.Text('',**text_format2)],
            [sg.Text('El botón Directorio de collages, te permite elegir la carpeta donde quieres guardar tus collage ya creados.',**text_format2)],
            [sg.Text('Solo debés elegir la carpeta y presionar el botón Seleccionar.',**text_format2)],
            [sg.Text('',**text_format2)],
            [sg.Text('En todos los casos, al presionar Guardar, se guardaran tus cambios, y podrás usarlo cada vez que quieras usar la aplicación.',**text_format2)],
            [sg.Text('De igual forma, al presionar Cancelar, se cancelan los cambios elegidos, quedando guardada la última configuración.',**text_format2)],
            [sg.Button("Volver", key='-VOLVER-', **text_format2)]]                    
    return layout


####################################################################
def layout_crear():
    layout =[[sg.Text('Dentro de la ventana de Inicio, podrás elegir entre crear memes y crear collages',**text_format2)],
            [sg.Text('',**text_format2)],
            [sg.Text('Crear memes',**text_format1)],
            [sg.Text('En el botón de seleccionar imagen, te mandará al directorio que elegiste como Repositorio de imagenes (para más información, ver la ventanada de ayuda-configuración).',**text_format2)],
            [sg.Text('Elegís la imagen requerida, y presionás seleccionar.',**text_format2)],
            [sg.Text('Luego, debés escribir la frase que querés agregarle a tu meme.',**text_format2)],
            [sg.Text('Al presionar el botón Generar, el meme será generado y almacenado en la carpeta Directorio de memes.',**text_format2)],
            [sg.Text('',**text_format2)],
            [sg.Text('Crear collage',**text_format1)],
            [sg.Text('En el botón de seleccionar imagen, te mandará al directorio que elegiste como Repositorio de imagenes (para más información, ver la ventanada de ayuda-configuración).',**text_format2)],
            [sg.Text('Elegís la imagen requerida, y presionás Seleccionar. Puedes hacerlo tantas veces como imágenes quieras elegir.',**text_format2)],
            [sg.Text('Al finalizar la selección, presiona Finalizar. Las imagenes elegidas aparecerán escritas en pantalla.',**text_format2)],
            [sg.Text('Finalmente, elige el template entre los disponibles dados por la propia aplicación.',**text_format2)],
            [sg.Text('Debes tener en cuenta que no podrás generar templates nuevos.',**text_format2)],
            [sg.Text('Al presionar el botón Generar, el collage será generado y almacenado en la carpeta Directorio de memes.',**text_format2)],
            [sg.Text('',**text_format1)],
            [sg.Text('Nota: Si tenés duda respecto a las carpetas de guardado, ver la ventanada de ayuda-configuración).',**text_format2)],
            [sg.Button("Volver", key='-VOLVER-', **text_format2)]]                    
    return layout


####################################################################

#ACÁ VA EL LAYPUT DE TAG

####################################################################
def ventana_ayuda():
    #accion = "Entró a ventana de ayuda"
    window = sg.Window('Ayuda',layout_ayuda())
    while True:
        event, values = window.read()
        if event == '-APP-':
            accion = "Entró a ventana de Ayuda --> Ayuda sobre la app"
            window_app = sg.Window('Ayuda: Sobre la aplicación',layout_app())
            while True:
                event, values = window_app.read()
                if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
                    break
                window_app.close()

        if event == '-PERFIL-':
            accion = "Entró a ventana de Ayuda --> Ayuda sobre perfiles"
            window_perfil = sg.Window('Ayuda: Sobre perfiles',layout_perfil())
            while True:
                event, values = window_perfil.read()
                if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
                    break
                window_perfil.close()

        if event == '-CONF-':
            accion = "Entró a ventana de Ayuda --> Ayuda sobre configuración"
            window_conf = sg.Window('Ayuda: Sobre configuración',layout_conf())
            while True:
                event, values = window_conf.read()
                if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
                    break
                window_conf.close()     

        if event == '-CREAR-':
            accion = "Entró a ventana de Ayuda --> Ayuda sobre creación de memes y collage"
            window_crear = sg.Window('Ayuda: Sobre creación de memes/collages',layout_crear())
            while True:
                event, values = window_crear.read()
                if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
                    break
                window_crear.close()    


        if event == '-TAG-':
            accion = "Entró a ventana de Ayuda --> Ayuda sobre etiquetado de imágenes"
            window_tag = sg.Window('Ayuda: Sobrobre etiquetado de imágenes',layout_tag())
            while True:
                event, values = window_tag.read()
                if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
                    break
                window_tag.close()    

        if event == sg.WINDOW_CLOSED or event == '-VOLVER-':
            break


    window.close()
    return accion
    
 
if __name__ == "__main__":
       ventana_ayuda()
