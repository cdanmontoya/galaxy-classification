#--------------------------------------------------------------------------
#------- PLANTILLA DE CÓDIGO EROSIÓN Y DILATACIÓN--------------------------
#--------------------------------------------------------------------------
#------- Por: Carlos Daniel Montoya Hurtado carlos.montoyah@udea.edu.co ---
#-------      Jose David Tello Medina  jose.tello@udea.edu.co -------------
#------- Curso Básico de Procesamiento de Imágenes y Visión Artificial-----
#-------  Mayo de 2020-----------------------------------------------------
#--------------------------------------------------------------------------



#--------------------------------------------------------------------------
#--1. Se importan las librerias y funciones necesarias --------------------
#--------------------------------------------------------------------------

import cv2                            # libreria de OpenCV
import numpy as np                    # libreria numpy
from matplotlib import pyplot as plt  # libreria matplotlib

#--------------------------------------------------------------------------
#--2. Función de erosión y dilatación -------------------------------------
#---Definición de la función que recibe los parametros del path de --------
#--- la imagen, fase(test,training) y nombre de la imagen------------------

def erode_and_dilate_image(path_to_read, phase, image_name):    # Definición de la función
    img = cv2.imread(path_to_read)                              # lee la imagen
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))  # Se obtiene el elemento estructurante
    mask = cv2.erode(img, element, iterations = 1)              # Se hace erosión con una iteración
    mask = cv2.dilate(mask, element, iterations = 1)            # Se hace dilatación con una iteración
    mask = cv2.erode(mask, element, iterations= 1)              # Se hace erosión con una iteración
    full_path = None                                            # Inicializo variable de ruta para guardar imagen
    if phase == 'test':                                         # Si el conjunto de imagenes es de test
        full_path = './dilat_erod_preproc/test/' + image_name   # Ruta de las imagenes de test para guardar
        cv2.imwrite(full_path, mask)                            # Guarda imagen
    elif phase == 'train':                                      # Si el conjunto de imagenes es de train
        full_path = './dilat_erod_preproc/train/' + image_name  # Ruta de las imagenes de train para guardar
        cv2.imwrite(full_path, mask)                            # Guarda imagen 
    return

#--------------------------------------------------------------------------
#---------------------------  FIN DEL PROGRAMA ----------------------------
#--------------------------------------------------------------------------  