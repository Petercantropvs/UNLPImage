import PySimpleGUI as sg
import configuracion
import memes
import collage
import ayuda
import json
import generar_etiquetas
import os

#Defino los colores de las ventanas
sg.theme('light green 3')

#Defino las fuentes de lsa ventandas
text_format1 = {'font' : ('latin modern sansquotation', 15)}
text_format2 = {'font' : ('latin modern sansquotation', 10)}

# Defino el tamaño de lsa ventanas
#window_size = (600, 700)
window_margins = (150, 100)

#Import todas las necesarias de crear/editar perfeil, etiquetar imàgenes, etc.

# Definir el diseño de la ventana principal
def layout_menuprincipal():
    text_format1 = {'font' : ('latin modern sansquotation', 15)}
    text_format2 = {'font' : ('latin modern sansquotation', 10)}

    # Defino el tamaño de lsa ventanas
    #window_size = (600, 700)
    layout = [[sg.Button('*',key='-CONFIGURACION-',**text_format1), sg.Button('?',key='-AYUDA-',**text_format1)],
                           [sg.Button('Etiquetar imágenes',key='-ETIQUETAR_IM-',**text_format2)],
                           [sg.Button('Generar meme',key='-CREAR_MEME-', **text_format2)],
                           [sg.Button('Generar collage',key='-CREAR_COL-', **text_format2)],
                           [sg.Button("Salir",key='-SALIR-',**text_format1)]]        
    return layout

def ventana_menuprincipal():
    # Crear la ventana principal
    #window_margins = (150, 100)

    window_menuprincipal = sg.Window('Menú', layout_menuprincipal()) #,margins=window_margins) #size=window_size, 

    # Event Loop de la ventana principal
    while True:
        event_principal, values_principal = window_menuprincipal.read()

        if event_principal == sg.WINDOW_CLOSED or event_principal == '-SALIR-':
            break

        if event_principal == '-CONFIGURACION-':
            configuracion.ventana_configuracion()

        if event_principal == '-AYUDA-':
            ayuda.ventana_ayuda()
            #ayuda.ventana_ayuda(window_size, window_margins, text_format)

        if event_principal == '-ETIQUETAR_IM-':
            generar_etiquetas.ventana_etiquetas()
       
        if event_principal == '-CREAR_MEME-':
            memes.ventana_meme()

#       if event_principal == '-CREAR_COLc-':
#            memes.ventana_()
        window_menuprincipal.close()


if __name__ == "__main__":
       ventana_menuprincipal()