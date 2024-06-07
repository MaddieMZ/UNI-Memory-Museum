#include"VAO.h"
//Se generan los arreglos de vertices
VAO::VAO()
{
	glGenVertexArrays(1, &ID);
}

//Se enlaza los distintos arreglos de vertices y el indice para los atributos
void VAO::LinkVBO(VBO VBO, GLuint layout)
{
	VBO.Bind();
	glEnableVertexAttribArray(layout);
	glVertexAttribPointer(layout, 3, GL_FLOAT, GL_FALSE, 0, (void*)0);
	VBO.Unbind();
}
void VAO::Bind()
{
	glBindVertexArray(ID);
}
void VAO::Unbind()
{
	glBindVertexArray(0);
}
void VAO::Delete()
{
	glDeleteVertexArrays(1, &ID);
}