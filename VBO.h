#ifndef VBO_CLASS_H 
#define VBO_CLASS_H
#include<glad/glad.h> 

//Creamos una clase VBO
class VBO
{
public:
	//Asignamos un id
	GLuint ID;
	//Constructos que toma el arreglo de vertices, y el tamaño que utilizan
	VBO(GLfloat* vertices, GLsizeiptr size);
	//Enlaza con el programa shader
	void Bind(); 
	//Desenlaza con el programa shader
	void Unbind();
	//Elimina el programa shader para ahorrar recursos
	void Delete();
};

#endif