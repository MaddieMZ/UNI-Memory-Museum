#ifndef SHADER_CLASS_H
#define SHADER_CLASS_H
#include<glad/glad.h> 
#include<iostream>
#include<fstream> 
#include<sstream>
#include<iostream> 
#include<cerrno>

//Nos permite leer archivos y retorna una cadena de caracteres
std::string get_file_contents(const char* filename); 

//Creamos una clase shader
class Shader {
public:
	//Asignamos un id
	GLuint ID;
	//Los parametros de los archivos de vertices y fragmentos
	Shader(const char* vertexFile, const char* fragmentFile);
	//Activamos el programa y eliminamos el programa
	void Activate(); void Delete();
};

#endif