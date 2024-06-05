
//#include <GL/glew.h>
#include <GLAD/glad.h>
#include <GLM/glm.hpp>
#include <GLFW/glfw3.h>
#include<iostream>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>


void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
    glViewport(0, 0, width, height);
}

int main() {
    // Inicialización de GLFW
    if (!glfwInit()) {
        std::cout << "Fallo en la inicialización de GLFW." << std::endl;
        return -1;
    }

    // Configuración de GLFW
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // Creación de la ventana GLFW
    GLFWwindow* window = glfwCreateWindow(800, 600, "Mariposa Bonita", NULL, NULL);
    if (window == NULL) {
        std::cout << "Fallo en la creación de la ventana GLFW." << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    // Carga de GLAD
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        std::cout << "Fallo en la inicialización de GLAD." << std::endl;
        return -1;
    }

    // Definición y compilación de shaders (vertex y fragment)
    const char* vertexShaderSource = "#version 330 core\n"
        "layout (location = 0) in vec3 aPos;\n"
        "layout (location = 1) in vec3 aColor;\n"
        "out vec3 ourColor;\n"
        "uniform mat4 transform;\n"
        "void main()\n"
        "{\n"
        "   gl_Position = transform * vec4(aPos, 1.0);\n"
        "   ourColor = aColor;\n"
        "}\0";
    const char* fragmentShaderSource = "#version 330 core\n"
        "in vec3 ourColor;\n"
        "out vec4 FragColor;\n"
        "void main()\n"
        "{\n"
        "   FragColor = vec4(ourColor, 1.0f);\n"
        "}\n\0";

    // Compilación de shaders
    unsigned int vertexShader, fragmentShader;
    int success;
    char infoLog[512];

    // Vertex Shader
    vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
    glCompileShader(vertexShader);
    glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
    if (!success) {
        glGetShaderInfoLog(vertexShader, 512, NULL, infoLog);
        std::cout << "Error de compilación del Vertex Shader: " << infoLog << std::endl;
    }

    // Fragment Shader
    fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
    glCompileShader(fragmentShader);
    glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &success);
    if (!success) {
        glGetShaderInfoLog(fragmentShader, 512, NULL, infoLog);
        std::cout << "Error de compilación del Fragment Shader: " << infoLog << std::endl;
    }

    // Enlace de shaders en un programa de sombreado
    unsigned int shaderProgram;
    shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    glLinkProgram(shaderProgram);
    glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
    if (!success) {
        glGetProgramInfoLog(shaderProgram, 512, NULL, infoLog);
        std::cout << "Error de enlace del Shader Program: " << infoLog << std::endl;
    }

    // Liberar memoria de shaders (ya no necesitamos los shaders individuales)
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    // Vértices de la mariposa (definidos como varios triángulos) y colores
    float vertices[] = {
        // Posiciones          // Colores
        // Ala izquierda superior
        -0.5f,  0.2f, 0.0f,   1.0f, 0.0f, 0.0f,
        -0.2f,  0.5f, 0.0f,   1.0f, 0.0f, 0.0f,
        -0.3f,  0.1f, 0.0f,   1.0f, 0.0f, 0.0f,

        // Ala izquierda inferior
        -0.5f, -0.2f, 0.0f,   0.0f, 1.0f, 0.0f,
        -0.2f, -0.5f, 0.0f,   0.0f, 1.0f, 0.0f,
        -0.3f, -0.1f, 0.0f,   0.0f, 1.0f, 0.0f,

        // Ala derecha superior
         0.5f,  0.2f, 0.0f,   0.0f, 0.0f, 1.0f,
         0.2f,  0.5f, 0.0f,   0.0f, 0.0f, 1.0f,
         0.3f,  0.1f, 0.0f,   0.0f, 0.0f, 1.0f,

         // Ala derecha inferior
          0.5f, -0.2f, 0.0f,   1.0f, 1.0f, 0.0f,
          0.2f, -0.5f, 0.0f,   1.0f, 1.0f, 0.0f,
          0.3f, -0.1f, 0.0f,   1.0f, 1.0f, 0.0f
    };

    unsigned int VBO, VAO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);

    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    // Posiciones de los vértices
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    // Colores
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1);

    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);

    // Bucle principal
    while (!glfwWindowShouldClose(window)) {
        // Procesamiento de entradas
        glfwPollEvents();

        // Renderizado
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        // Calcular matriz de transformación de rotación
        float angle = glfwGetTime() * 50.0f; // velocidad de rotación
        glm::mat4 rotation = glm::rotate(glm::mat4(1.0f), glm::radians(angle), glm::vec3(0.0f, 0.0f, 1.0f));

        // Obtener la ubicación de la matriz de transformación en el shader
        unsigned int transformLoc = glGetUniformLocation(shaderProgram, "transform");
        glUniformMatrix4fv(transformLoc, 1, GL_FALSE, glm::value_ptr(rotation));

        // Dibujar la mariposa
        glUseProgram(shaderProgram);
        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, 12);
        glBindVertexArray(0);

        // Intercambio de buffers y manejo de eventos
        glfwSwapBuffers(window);
    }

    // Limpieza
    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glfwTerminate();
    return 0;
}



