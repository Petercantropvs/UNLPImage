#from generar_etiquetas import generar_etiquetas
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

archivo = open('../nuevo_perfil/users.json', 'r')
datos = json.load(archivo)
print(datos)
print(len(datos))
print(next(iter(datos[0])))
print(next(iter(datos[1])))
i=0
perfiles = []

for k in range(len(datos)):
    perfiles.append(next(iter(datos[k])))
def layout_inicio():

	layout_inicio = [[sg.Text('UNLPImage', font = ('latin modern sansquotation', 25), pad = (0,0,50,0))], [sg.Image(data=get_img_data('nuevo_perfil/prof_pictures/'+perfiles[i]+'.png', first=True), enable_events=True, key=perfiles[i]), 
	sg.Image(data=get_img_data('nuevo_perfil/prof_pictures/'+perfiles[i+1]+'.png', first=True), enable_events=True, key=perfiles[i+1]), 
	sg.Image(data=get_img_data('nuevo_perfil/prof_pictures/'+perfiles[i+2]+'.png', first=True), enable_events=True, key=perfiles[i+2]), sg.Image(data=get_img_data('mas.png', first=True), enable_events=True, key = '-CREAR-')] 
    ]
	return layout_inicio

def ventana_eleccionperfil():
	window = sg.Window('UNLPImage', layout_inicio())
	
	while True:
		event, a = window.read()
		if event == '-CREAR-':
			try:
				nuevoperfil.ventana_nuevoperfil().read()
			except AttributeError:
				continue
		if event == sg.WIN_CLOSED:
			window.close()
			break
#generar_etiquetas.ventana_etiquetas()