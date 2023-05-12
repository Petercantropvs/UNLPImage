import io
import os
import json
import PySimpleGUI as sg
from PIL import Image, ImageTk
import sys
from src.windows import nuevoperfil
from src.default.pathing import BASE_PATH
from src.default.data import lectura

def get_img_data(f, first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img = img.resize((100,100), Image.ANTIALIAS)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)

#try:
#    archivo = open(BASE_PATH+'/src/users-data/users.json', 'r')
#    datos = json.load(archivo)
#    archivo.close()
#except FileNotFoundError:
#    datos = {}

datos = lectura()
#nombres = []
perfiles = []

#for k in range(len(datos)):
#    perfiles.append(next(iter(datos[k])))

perfiles = list(datos.keys())


def layout_inicio():

	imagenes = []
	if len(datos) <= 2:
		for i, imagen in enumerate(perfiles):
			imagenes.append(sg.Image(data=get_img_data(BASE_PATH+'/src/users-data/prof_pictures/'+imagen+'.png', first=True), enable_events=True, k= i))#, key=perfiles[k]))
			#nombres.append([sg.Text(perfiles[k], font = ('latin modern sansquotation', 10), pad = (0,0,50,0))])
	else:	
		for k in range(3):
			imagenes.append(sg.Image(data=get_img_data(BASE_PATH+'/src/users-data/prof_pictures/'+perfiles[k]+'.png', first=True), enable_events=True, k= k))#, key=perfiles[k]))
			#nombres.append(sg.Text(perfiles[k], font = ('latin modern sansquotation', 10), pad = (0,0,50,0)))
	imagenes.append(sg.Image(data=get_img_data(BASE_PATH+'/src/default/mas.png', first=True), enable_events=True, key = '-CREAR-'))
	layout_inicio = [[sg.Text('UNLPImage', font = ('latin modern sansquotation', 25), pad = (0,0,50,0))], 
	[imagenes],
	[sg.Text('Ver más >', font = ('latin modern sansquotation', 20), enable_events = True, key = '-MAS-')]
	]
	return layout_inicio

def ventana_seleccionperfil():
	""" 
    La función de selección de perfil tiene varias cosas incorporadas: 
    1) Muestra imágenes de perfiles ya creados, para poder seleccionar el propio; y a partir de eso continuar al Menú principal de la app.
    2) El botón ver más muestra otros perfiles ya creados anterioremente.
    3) Permite generar un nuevo perfil, al clickear la imágen con el signo "+". Este botón, llamará a la funcion nuevoperfil, dentro del progra nuevoperfil.py.
    """
	window = sg.Window('UNLPImage', layout_inicio())
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
		#print(event)
		#print(j)
		if j > 2 and len(perfiles)>3:
			j=0
		if j >= 2 and len(perfiles)<=3:
			j=0
		if i >= len(perfiles):
			i=0

		if event == '-CREAR-':
			try:
				window.Hide()

				perfil = nuevoperfil.ventana_nuevoperfil() 
				event_seleccion = event
				
				window.UnHide()
				window.close()
				break
			except AttributeError:
				print('Hola')
				perfil = None
				event_seleccion = event
	
				window.UnHide()
				continue
			finally:
				return perfil, event_seleccion
		if event == '-MAS-':
			if len(perfiles)>3:
				window[j].update(data=get_img_data(BASE_PATH+'/src/users-data/prof_pictures/'+perfiles[i]+'.png', first = True))
				cuadro[j] = perfiles[i]
				i = i+1
				j = j+1
			else:
				sg.popup_ok('No hay más perfiles para mostrar', title='UNLPImage')  
		if event == sg.WIN_CLOSED :
			perfil = None
			event_seleccion = event
			return perfil, event_seleccion
			break
		if event == 0:
			perfil = cuadro[0]
			event_seleccion = event
			window.close()
			return perfil, event_seleccion
			
			break
		if event == 1:
			perfil = cuadro[1]
			event_seleccion = event
			window.close()
			return perfil, event_seleccion

			break
		if event == 2:
			perfil = cuadro[2]
			event_seleccion = event
			window.close()
			return perfil, event_seleccion

			break
	window.close()

if __name__ == '__main__':
    ventana_eleccionperfil()
