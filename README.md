# Galaxy Classification

En este proyecto se exploró el efecto del preprocesamiento para disminuir el ruido de las imágenes del conjunto de datos del [Galaxy-Zoo](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge) y su impacto en la precisión y costo en el entrenamiento del modelo. En este [video de YouTube](https://www.youtube.com/watch?v=qqiEUqKTnmM&feature=youtu.be) se puede encontrar una explicación de las técnicas empleadas y de los resultados obtenidos.

![](/img/training-loss.png)

Del experimento pudimos concluir que aplicar un filtro gaussiano para reducir el ruido impacta positivamente en el entrenamiento del modelo.


# Requisitos

## Para la ejecución de los algoritmos de pre-procesamiento
1. Tener python en su última versión
2. Tener instalado OpenCV, matplotlib y numpy
3. Crear 2 carpeta en el mismo directorio donde se encuentran los archivos de python que se llamen '/dilat_erod_preproc/' y 'filter_preproc', una vez dentro de ellas crear en cada carpeta otras dos carpetas que se llamen 'test' y 'train'
4. Se debe poseer el dataset en el mismo directorio donde se encuentran los archivos de python.
5. Ejecutar 'python3 read_multi_files.py'

## Para la ejecución de los algoritmos de Machine Learning
1. Es indispensable tener una GPU y tener instalados sus drivers (en el caso de nvidia sería los drivers de CUDA)
2. Se debe tener instalado python3, Jupyter, tensorflow y Keras.
3. Tener el dataset, de preferencia en el mismo directorio donde esta contenido el archivo a ejecutar
4. Abrir con jupyter 'galaxy-classification.ipynb' y ejecutar cada instrucción

# Autores 

Desarrollado para el curso de Procesamiento Digital de Imágenes (2019-2), dictado por David Fernández (david.fernandez@udea.edu.co) en la [Universidad de Antioquia](http://udea.edu.co/), por 

| Nombre | GitHub | Correo electrónico |
|---|---| ---|
|Jose David Tello Medina | [@joseda77](https://github.com/joseda77) |  jose.tello@udea.edu.co |
| Carlos Daniel Montoya Hurtado | [@cdanmontoya](https://github.com/cdanmontoya) | carlos.montoyah@udea.edu.co |
