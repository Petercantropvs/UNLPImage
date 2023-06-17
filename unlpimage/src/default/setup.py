import PySimpleGUI as sg

sg.theme('light green 3')

# Defino las fuentes de las ventanas
text_format8 = {'font': ('latin modern sansquotation', 8)}
text_format10 = {'font': ('latin modern sansquotation', 10)}
text_format15 = {'font': ('latin modern sansquotation', 15)}
text_format20 = {'font': ('latin modern sansquotation', 20)}
text_format25 = {'font': ('latin modern sansquotation', 25)}

# Defino el tamaño de laa ventanas
window_size_big = (600, 500)
window_margins150 = (150, 100)
window_margins90 = (90, 75)

# Más constantes:
tags_header = ['path', 'description', 'resolution', 'size',
               'mimetype', 'tags', 'last user', 'last edit time']
IMG_SIZE = (300, 400)
DESIGNS = {'-L1-': {1: {'coords': (0, 0), 'size': (300, 200)},
                    2: {'coords': (0, 200), 'size': (300, 200)}},
           '-L2-': {1: {'coords': (0, 0), 'size': (150, 400)},
                    2: {'coords': (150, 0), 'size': (150, 400)}},
           '-L3-': {1: {'coords': (0, 0), 'size': (300, 133)},
                    2: {'coords': (0, 133), 'size': (300, 133)},
                    3: {'coords': (0, 266), 'size': (300, 133)}},
           '-L4-': {1: {'coords': (0, 0), 'size': (150, 200)},
                    2: {'coords': (150, 0), 'size': (150, 200)},
                    3: {'coords': (0, 200), 'size': (150, 200)},
                    4: {'coords': (150, 200), 'size': (150, 200)}},
           '-L5-': {1: {'coords': (0, 0), 'size': (150, 400)},
                    2: {'coords': (150, 0), 'size': (150, 200)},
                    3: {'coords': (150, 200), 'size': (150, 200)}},
           '-L6-': {1: {'coords': (0, 0), 'size': (150, 200)},
                    2: {'coords': (0, 200), 'size': (150, 200)},
                    3: {'coords': (150, 0), 'size': (150, 133)},
                    4: {'coords': (150, 133), 'size': (150, 133)},
                    5: {'coords': (150, 266), 'size': (150, 133)}}}
