import io
import os
import json
import PySimpleGUI as sg
from PIL import Image, ImageTk
import sys
from src.windows import nuevoperfil
from src.default.pathing import BASE_PATH
from src.default.data import read_users
from src.default.data import get_img_data_profiles as get_img_data
from src.default.setup import *


def layout_inicio(datos,perfiles):

	imagenes = []
	
	if len(datos) <= 2:
		for i, imagen in enumerate(perfiles):
			imagenes.append(sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','users-data','prof_pictures',imagen+'.png'), first=True), enable_events=True, k= i))

	else:	
		for k in range(3):
			imagenes.append(sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','users-data','prof_pictures',perfiles[k]+'.png'), first=True), enable_events=True, k= k))
			
	imagenes.append(sg.Image(data=get_img_data(os.path.join(BASE_PATH,'src','default','mas.png'), first=True), enable_events=True, key = '-CREAR-'))
	layout_inicio = [[sg.Text('UNLPImage', **text_format25, pad = (0,0,50,0))], 
	[imagenes],
	[sg.Text('Ver más >', **text_format20, enable_events = True, key = '-MAS-')]
	]
	return layout_inicio

def ventana_seleccionperfil():
	""" 
    La función de selección de perfil tiene varias cosas incorporadas: 
    1) Muestra imágenes de perfiles ya creados, para poder seleccionar el propio; y a partir de eso continuar al Menú principal de la app.
    2) El botón ver más muestra otros perfiles ya creados anterioremente.
    3) Permite generar un nuevo perfil, al clickear la imágen con el signo "+". Este botón, llamará a la funcion nuevoperfil, dentro del progra nuevoperfil.py.
    """

	datos = read_users()
	perfiles = []
	
	perfiles = list(datos.keys())

	window = sg.Window('UNLPImage', layout_inicio(datos,perfiles))
	accion = 'Inició sesión.'

	cuadro = []

	if len(perfiles) > 2:
		cuadro.append(perfiles[0])
		cuadro.append(perfiles[1])
		cuadro.append(perfiles[2])
	if len(perfiles) == 2:
		cuadro.append(perfiles[0])
		cuadro.append(perfiles[1])
	if len(perfiles) == 1:
		cuadro.append(perfiles[0])


	j= 0
	if len(perfiles) <= 2:
		i = len(perfiles)+1
	else:
		i = 3
	while True:
		event, a = window.read()

		if j > 2 and len(perfiles)>3:
			j=0
		if j >= 2 and len(perfiles)<=3:
			j=0
		if i >= len(perfiles):
			i=0

		if event == '-CREAR-':
			try:
				window.Hide()
				perfil, accion = nuevoperfil.ventana_nuevoperfil() 
				event_seleccion = event
				window.UnHide()
				window.close()
				break
			except AttributeError:
				print('Hola')
				perfil = None
				event_seleccion = event
				accion = None
				window.UnHide()
				continue
			finally:
				return perfil, event_seleccion, accion
		if event == '-MAS-':
			if len(perfiles)>3:
				window[j].update(data=get_img_data(os.path.join(BASE_PATH,'src','users-data','prof_pictures',perfiles[i]+'.png'), first = True))
				cuadro[j] = perfiles[i]
				i = i+1
				j = j+1
			else:
				sg.popup_ok('No hay más perfiles para mostrar', title='UNLPImage')  
		if event == sg.WIN_CLOSED :
			perfil = None
			event_seleccion = event
			accion = None
			return perfil, event_seleccion, accion
			break
		if event == 0:
			perfil = cuadro[0]
			event_seleccion = event
			window.close()
			return perfil, event_seleccion, accion
			
			break
		if event == 1:
			perfil = cuadro[1]
			event_seleccion = event
			window.close()
			return perfil, event_seleccion, accion

			break
		if event == 2:
			perfil = cuadro[2]
			event_seleccion = event
			window.close()
			return perfil, event_seleccion, accion

			break
	window.close()

if __name__ == '__main__':
    ventana_eleccionperfil()
