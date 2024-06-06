#version 330 core // Definimos la version del lenguaje de sombreado
layout (location = 0) in vec3 aPos; //Definimos un atributo posicion de los vertices
void main()
{
gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0); //Definimos la posicion que va a tener segun el valor de aPos
}