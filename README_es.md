# Descripción del Proyecto

Este proyecto es una exhibición interactiva que muestra los desafíos superados durante un grado de Ingeniería Informática. Utiliza técnicas de programación gráfica con OpenGL y Python para crear una cueva virtual con exposiciones que representan varios niveles de dificultad enfrentados y superados a lo largo del curso.

# Características:

  ## Entorno 3D Interactivo: 
  Navega a través de una cueva con múltiples exposiciones.
  
  ## Iluminación Dinámica: 
  Implementada usando sombreado Phong para efectos de iluminación realistas.
  
  ## Efectos de Sonido: 
  Música de fondo para mejorar la experiencia.
    
  ## Múltiples Exposiciones: 
  Siete exposiciones que muestran diferentes desafíos y sus soluciones.

# Requisitos

    Python 3.x
    Pygame
    ModernGL
    PyWavefront

# Instalación
## Clona el repositorio
```
git clone https://github.com/MaddieMZ/UNI-Memory-Museum.git
cd UNI-Memory-Museum
```
## Instala las dependencias:

```
pip install pygame moderngl pywavefront
```

## Añadir Texturas y Modelos:
```
Asegúrate de tener las texturas necesarias en el directorio de texturas.
Asegúrate de tener los modelos necesarios en el directorio de modelos.
```
# Uso

## Para iniciar la aplicación, ejecuta:
```
python main.py
```
## Usa los siguientes controles para navegar por el entorno:

    A: Mover a la izquierda
    D: Mover a la derecha
    ESC: Salir de la aplicación

# Estructura de Archivos

  ### main.py: 
  El punto de entrada principal de la aplicación.
  
  ### jueguito.py: 
  Clase que contiene toda la GUI del proyecto, incluida la escena misma.
  
  ### model.py: 
  Contiene clases para modelos 3D y sus propiedades.
  
  ### camera.py: 
  Gestiona los controles y movimientos de la cámara.
  
  ### light.py: 
  Maneja la iluminación y el sombreado.
  
  ### mesh.py: 
  Gestiona la creación y renderizado de objetos de malla. Combina tanto VBOs como VAOs.

  ### vao.py:
  Manejo de objetos de array de vértices, asignándolos a sus respectivos VBOs.

  ### vbo.py:
  Información de vértices para cada modelo contenido en el proyecto.

  ### light.py:
  Información del modelo de iluminación de Phong: Iluminación difusa, especular y ambiental.

  ### shader_program.py:
  Diccionario que contiene información sobre shaders de fragmentos y shaders de vértices.

  ### texture.py
  Clase que contiene un diccionario con todos los archivos de texturas implementados.
  
  ### scene.py: 
  Contiene la clase Scene que carga y gestiona todos los objetos en el entorno.

  ### button.py:
  Clase que contiene una implementación simple de botones en pygame.
  
  ### texturas: 
  Directorio que contiene imágenes de texturas.
  
  ### objetos: 
  Directorio que contiene archivos de modelos 3D.

  ### shaders:
  Directorio que contiene shaders de vértices y fragmentos GLSL.
  
  ### sonido:
  Directorio que contiene efectos de sonido.
  
  # Créditos:

  ## Música:

Pista del Menú: The midnight Tea Shop – Laura Shigihara
https://www.youtube.com/watch?v=X2vlmjuyHBw

Pista de la Escena: Exhale – Lena Raine
https://www.youtube.com/watch?v=q7QMTo-P6H0

## Modelos:

Pilar: reza0310
https://free3d.com/3d-model/pillar-360101.html

Cartel: 3Dmae
https://www.turbosquid.com/3d-models/simple-wooden-sign-3d-model-2215001

Suelo: Bloque de Hierro – Mojang AB
https://minecraft.fandom.com/wiki/Block_of_Iron

## Librerías:

Pygame - https://www.pygame.org/docs/

ModernGL - https://moderngl.readthedocs.io/en/5.10.0/

Numpy - https://numpy.org/doc/1.26/

PyWavefront - https://pypi.org/project/PyWavefront
