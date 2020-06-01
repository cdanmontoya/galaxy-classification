#--------------------------------------------------------------------------
#------- PLANTILLA DE CÓDIGO FILTRO GAUSSIANO------------------------------
#--------------------------------------------------------------------------
#------- Por: Carlos Daniel Montoya Hurtado carlos.montoyah@udea.edu.co ---
#-------      Jose David Tello Medina  jose.tello@udea.edu.co -------------
#------- Curso Básico de Procesamiento de Imágenes y Visión Artificial-----
#-------  Mayo de 2020-----------------------------------------------------
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
#--1. Se importan las librerias y funciones necesarias --------------------
#--------------------------------------------------------------------------

from os import listdir                              # Importa la libreria os con listdir para listar archivos de una carpeta
from pre_proc_filter import gaussian_filter         # Importa la función gaussian_filter
from pre_proc_erode import erode_and_dilate_image   # Importa la función erode_and_dilate_image
from os.path import isfile, join                    # Importa librerias para el procesado de los archivos
import numpy                                        # libreria numpy

#--------------------------------------------------------------------------
#--2. Código para leer y procesar las imagenes  ---------------------------
#--------------------------------------------------------------------------

mypath='./images_test_rev1/'                    # Se define la carpeta que contiene las imagenes a procesar
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ] # Se obtiene el nombre de cada archivo (imagen) 
for n in range(len(onlyfiles)):                                      # Se recorre cada imagen para procesarla
    full_path = join(mypath,onlyfiles[n])                            # Obtiene la ruta absoluta de la imagen
    gaussian_filter(full_path, 'test', onlyfiles[n])                 # Se le aplica el filtro gaussiano
    erode_and_dilate_image(full_path, 'test', onlyfiles[n])          # Se le aplica erosión y dilatación
    print("testing phase",n)                                         # Imprime en que fase está   

mypath='./images_training_rev1/'                # Se define la carpeta que contiene las imagenes a procesar
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ] # Se obtiene el nombre de cada archivo (imagen)   
for n in range(len(onlyfiles)):                                      # Se recorre cada imagen para procesarla
    full_path = join(mypath,onlyfiles[n])                            # Obtiene la ruta absoluta de la imagen
    gaussian_filter(full_path, 'train', onlyfiles[n])                # Se le aplica el filtro gaussiano
    erode_and_dilate_image(full_path, 'train', onlyfiles[n])         # Se le aplica erosión y dilatación
    print("training phase",n)                                        # Imprime en que fase está 

#--------------------------------------------------------------------------
#---------------------------  FIN DEL PROGRAMA ----------------------------
#--------------------------------------------------------------------------