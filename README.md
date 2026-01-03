# UNLPImage - Gestor y Editor de Imágenes

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-GPL_v3-green)
![Status](https://img.shields.io/badge/Status-Academic_Project-orange)
5-2023

## 📄 Descripción del Proyecto
Este software es un manipulador de imágenes, desarrollado como proyecto universitario final de la materia "Seminario de Lenguaje Python".
La aplicación permite gestionar perfiles de usuario, crear collages, generar memes y organizar repositorios personales mediante un sistema de etiquetado (tags) para facilitar la búsqueda.
El sistema incluye un módulo de **Business Intelligence** (vía Jupyter Notebooks) que procesa los logs de actividad para analizar patrones de uso y estadísticas de la aplicación.

## 🚀 Funcionalidades Principales
* **Gestión de Usuarios:** Creación, selección y edición de perfiles personalizados.
* **Manipulación de Imágenes:** Generación de memes y collages utilizando la librería Pillow.
* **Sistema de Etiquetado:** Tagging de imágenes para búsquedas rápidas dentro del repositorio local.
* **Logging y Análisis:** Registro de eventos de usuario en archivos logs para posterior análisis estadístico.

*Versión de muestra (Academic Release).*

## 📂 Datos de Prueba
Para facilitar la revisión y ejecución del análisis de datos sin necesidad de generar tráfico nuevo, este repositorio incluye **datos precargados**:

* `unlpimage/src/log` & `unlpimage/src/users-data`: Archivos de registro con usuarios y eventos simulados.
* `/Pictures`, `/collages` & `/memes`: Banco de imágenes de prueba utilizadas para validar las funciones de edición y el Notebook *estadisticas_jupyter.ipynb*.
* Además, se incluye un informe final acerca de la utilización de este software con herramientas de accesibilidad.

Liberías utilizadas: 

PySimpleGUI v 4.60.4
https://github.com/PySimpleGUI/PySimpleGUI

Pillow v 9.5.0
https://python-pillow.org

## 👨‍💻 Desarrollado por:
* Villegas, Pedro
* Celi, Marcos
* Curín, Daniela

---
*Licencia GPL 5-2023*
