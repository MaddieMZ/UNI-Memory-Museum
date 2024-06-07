#ifndef EBO_CLASS_H
#define EBO_CLASS_H
#include<glad/glad.h> 
//Creamos una clase EBO
class EBO
{
public:
	//Le asignamos su id
	GLuint ID;
	//En el constructor generamos el arreglo de indices y su tamaño
	EBO(GLuint* indices, GLsizeiptr size);
	void Bind(); void Unbind(); void Delete();
};

#endif 