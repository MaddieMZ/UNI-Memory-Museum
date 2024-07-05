#version 330 core

layout (location =0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;

struct Light{
    vec3 position;
    vec3 amb;
    vec3 spec;
    vec3 dif;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;

vec3 getLight(vec3 color){
    vec3 Normal= normalize(normal);

    vec3 ambiente = light.amb;

    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0,dot(lightDir,Normal));
    vec3 difusa = diff * light.dif;

    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float specu = pow(max(dot(viewDir,reflectDir),0),32);
    vec3 specular = specu * light.spec;

    return color * (ambiente+ difusa + specular);
}
void main(){
    float gamma= 2.2;
    vec3 color= texture(u_texture_0,uv_0).rgb;

    color= pow(color,vec3(gamma));

    color = getLight(color);
    color= pow(color, 1/ vec3(gamma));
    fragColor= vec4(color,1.0);
}