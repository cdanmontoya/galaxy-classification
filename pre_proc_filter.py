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

import cv2                              # libreria de OpenCV
import numpy as np                      # libreria numpy
from matplotlib import pyplot as plt    # libreria matplotlib


#--------------------------------------------------------------------------
#--2. Función de filtro gaussiano -----------------------------------------
#---Definición de la función que recibe los parametros del path de --------
#--- la imagen, fase(test,training) y nombre de la imagen------------------

def gaussian_filter(path_to_read, phase, image_name):           # Definición de la función
    img = cv2.imread(path_to_read)                              # lee la imagen
    filter_image = cv2.GaussianBlur(img,(5,5), 0)                  # Se le aplica el filtro gaussiano a la imagen
    full_path = None                                            # Inicializo variable de ruta para guardar imagen
    if phase == 'test':                                         # Si el conjunto de imagenes es de test
        full_path = './filter_preproc/test/' + image_name   # Ruta de las imagenes de test para guardar
        cv2.imwrite(full_path, filter_image)                    # Guarda imagen    
    elif phase == 'train':                                      # Si el conjunto de imagenes es de train
        full_path = './filter_preproc/train/' + image_name  # Ruta de las imagenes de train para guardar
        cv2.imwrite(full_path, filter_image)                    # Guarda imagen 
    return
    
#--------------------------------------------------------------------------
#---------------------------  FIN DEL PROGRAMA ----------------------------
#--------------------------------------------------------------------------    
    
