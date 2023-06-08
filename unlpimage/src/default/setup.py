import PySimpleGUI as sg

sg.theme('light green 3')

#Defino las fuentes de las ventanas
text_format8 = {'font' : ('latin modern sansquotation', 8)}
text_format10 = {'font' : ('latin modern sansquotation', 10)}
text_format15 = {'font' : ('latin modern sansquotation', 15)}
text_format25 = {'font' : ('latin modern sansquotation', 25)}
text_format20 = {'font' : ('latin modern sansquotation', 20)}

# Defino el tamaño de laa ventanas
window_size_big = (600, 500)
window_margins150 = (150, 100)
window_margins90 = (90, 75)

# Más constantes:
tags_header = ['path','description','resolution','size','mimetype','tags','last user','last edit time']