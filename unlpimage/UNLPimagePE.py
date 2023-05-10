import PySimpleGUI as sg
import configuracion
import memes
import collage
import ayuda
import menuprincipal
import generar_etiquetas
import json
import os

#Primer pantalla: (A - Inicio), solicitará que se seleccione su perfil de una lista ya o que registre uno nuevo en caso de no existir.

#ACá iria la parte de marquitos:
#while True:
#    event_perfil, values_perfil = window_perfil.read()
#window_perfil.close()

#Para el caso en que se quiera agregar un nuevo perfil por primera vez se mostrará la pantalla de carga de los mismos (B - Nuevo perfil).

#______________________________________________________________________________________________-
#Una vez que se selecciona el perfil en la aplicación se accede al menú principal de la aplicación (C - Menú principal)
# donde se pueden visualizar las opciones de la aplicación.

menuprincipal.ventana_menuprincipal()

    



