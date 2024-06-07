#ifndef VAO_CLASS_H
#define VAO_CLASS_H
#include<glad/glad.h>
#include"VBO.h"

//Creamos una clase VAO 
class VAO
{
public:
	//Asignamos un id
	GLuint ID; 
	VAO();
	//Le asignamos un VBO para que se manejen los atributos de los vertices, el layout es el indice
	void LinkVBO(VBO VBO, GLuint layout); 
	//Activa el programa shader
	void Bind();
	//Desactiva el programa shader
	void Unbind();
	//Elimina el programa shader para liberar recursos
	void Delete();
};

#endif