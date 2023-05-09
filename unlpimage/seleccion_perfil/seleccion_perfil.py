import nuevoperfil
import io
import os
import json
import PySimpleGUI as sg
from PIL import Image, ImageTk

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

try:
    archivo = open('users.json', 'r')
    datos = json.load(archivo)
except json.decoder.JSONDecodeError:
    datos = {}

archivo.close()

perfiles = []

#for k in range(len(datos)):
#    perfiles.append(next(iter(datos[k])))

perfiles = list(datos.keys())


def layout_inicio():

	imagenes = []
	if len(datos) <= 2:
		for k in range(len(datos)):
			imagenes.append(sg.Image(data=get_img_data('prof_pictures/'+perfiles[k]+'.png', first=True), enable_events=True, k= k))#, key=perfiles[k]))
	else:	
		for k in range(3):
			imagenes.append(sg.Image(data=get_img_data('prof_pictures/'+perfiles[k]+'.png', first=True), enable_events=True, k= k))#, key=perfiles[k]))
			print(k)
	imagenes.append(sg.Image(data=get_img_data('mas.png', first=True), enable_events=True, key = '-CREAR-'))
	layout_inicio = [[sg.Text('UNLPImage', font = ('latin modern sansquotation', 25), pad = (0,0,50,0))], 
	[imagenes],
	[sg.Text('Ver más >', font = ('latin modern sansquotation', 20), enable_events = True, key = '-MAS-')]
	]
	return layout_inicio

def ventana_eleccionperfil():
	window = sg.Window('UNLPImage', layout_inicio())
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
		print(event)
		#print(j)
		if j > 2 and len(perfiles)>3:
			j=0
		if j >= 2 and len(perfiles)<3:
			j=0
		if i >= len(perfiles):
			i=0

		if event == '-CREAR-':
			try:
				window.Hide()
				nuevoperfil.ventana_nuevoperfil()
				window.UnHide()
				window.close()
				break
			except AttributeError:
				print(event1)
				window.UnHide()
				continue
			#finally:
			#	window.UnHide()
		if event == '-MAS-':
			window[j].update(data=get_img_data('prof_pictures/'+perfiles[i]+'.png', first = True))
			cuadro[j] = perfiles[i]
			i = i+1
			j = j+1
		if event == sg.WIN_CLOSED:
			window.close()
			break
		if event == 0:
			print(cuadro[0])
		if event == 1:
			print(cuadro[1])
		if event == 2:
			print(cuadro[2])


if __name__ == '__main__':
    ventana_eleccionperfil()
