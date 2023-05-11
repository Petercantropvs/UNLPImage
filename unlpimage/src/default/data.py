import json
from src.default.pathing import BASE_PATH

def lectura():
	try:
		archivo = open(BASE_PATH+'/src/users-data/users.json', 'r')
		datos = json.load(archivo)
		archivo.close()
	except FileNotFoundError:
		datos = {}
	return datos