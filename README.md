# Project Description

This project is an interactive exhibition that showcases the challenges overcome during a Computer Engineering degree. It utilizes graphics programming techniques with OpenGL and Python to create a virtual cave with exhibitions representing various levels of difficulty faced and overcome throughout the course.

## Demonstration video
  https://youtu.be/OcSZMGajLJE
  
# Features:

  ## Interactive 3D Environment: 
  Navigate through a dungeon cave with multiple exhibitions.
  
  ## Dynamic Lighting: 
  Implemented using Phong shading for realistic lighting effects.
  
  ## Sound Effects: 
  Background music to enhance the experience.
    
  ## Multiple Exhibitions: 
  Seven exhibitions showcasing different challenges and their solutions.

# Requirements

    Python 3.x
    Pygame
    ModernGL
    PyWavefront

# Installation
## Clone the repositiory
```
git clone https://github.com/MaddieMZ/UNI-Memory-Museum.git
cd UNI-Memory-Museum
```
## Install the dependencies:

```
    pip install pygame moderngl pywavefront
    Add Textures and Models:
        Ensure you have the necessary textures in the textures directory.
        Ensure you have the necessary models in the models directory.
```
# Usage

## To start the application, run:
```
python main.py
```
## Use the following controls to navigate the environment:

    A: Move left
    D: Move right
    ESC: Exit the application

# File Structure

  ### main.py: 
  The main entry point of the application.
  
  ### jueguito.py: 
  Class containing the entire project GUI, including the scene itself
  
  ### model.py: 
  Contains classes for 3D models and their properties.
  
  ### camera.py: 
  Manages camera controls and movements.
  
  ### light.py: 
  Handles lighting and shading.
  
  ### mesh.py: 
  Manages the creation and rendering of mesh objects. Combines both VBOss and VAOs

  ### vao.py:
  Vertex array object handling, assigning them to their respective VBO

  ### vbo.py:
  Vertex information for every model contained in the project

  ### light.py:
  Phong's light model information: Diffuse, specular and ambient lighting.

  ### shader_program.py:
  Dictionary that contains information about fragment shaders and vertex shaders.

  ### texture.py
  Class containing a dictionary with all texture files implemented.
  
  ### scene.py: 
  Contains the Scene class that loads and manages all objects in the environment.

  ### button.py:
  Class containing a simple pygame button implementation
  
  ### texturas: 
  Directory containing texture images.
  
  ### objetos: 
  Directory containing 3D model files.

  ### shaders:
  Directory containing GLSL vertex and fragment shaders.
  
  ### sonido:
  Directory containing sound effects.
  
  # Credits:

  ## Music:

Menu Track: The midnight Tea Shop – Laura Shigihara
https://www.youtube.com/watch?v=X2vlmjuyHBw

Scne track: Exhale – Lena Raine
https://www.youtube.com/watch?v=q7QMTo-P6H0

## Models:

Pillar: reza0310
https://free3d.com/3d-model/pillar-360101.html

Sign: 3Dmae
https://www.turbosquid.com/3d-models/simple-wooden-sign-3d-model-2215001

Floor: Iron Block – Mojang AB
https://minecraft.fandom.com/wiki/Block_of_Iron

## Libraries:

Pygame - https://www.pygame.org/docs/

ModernGL - https://moderngl.readthedocs.io/en/5.10.0/

Numpy - https://numpy.org/doc/1.26/

PyWavefront - https://pypi.org/project/PyWavefront
