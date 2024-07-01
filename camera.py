
import glm
import pygame as pg

FOV= 50 #grados xd
NEAR= 0.1
FAR= 100
SPEED = 0.01
SENSITIVITY = 0.05
class Camera:
    def __init__(self, app, posicion=(0,0,4), yaw=-90, pitch=0):
        self.app = app
        self.resolucion= app.WIN_SIZE[0]/app.WIN_SIZE[1]
        self.posicion = glm.vec3(2,3,3)
        self.up = glm.vec3(0,1,0)
        self.right= glm.vec3(1,0,0)
        self.forward= glm.vec3(0,0,-1)

        #angulos de euler
        self.yaw=yaw
        self.pitch=pitch
        #matriz vista
        self.m_view = self.getvista()
        #matriz de proyección
        self.m_proj = self.getproyeccion()

    def rotate(self):
        rel_x,rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw,pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0,1,0)))
        self.up = glm.normalize(glm.cross(self.right,self.forward))
    
    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.getvista()

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys= pg.key.get_pressed()
        if keys[pg.K_w]:
            self.posicion += self.forward * velocity
        if keys[pg.K_s]:
            self.posicion -= self.forward * velocity
        if keys[pg.K_a]:
            self.posicion -= self.right * velocity
        if keys[pg.K_d]:
            self.posicion += self.right * velocity
        if keys[pg.K_q]:
            self.posicion += self.up * velocity
        if keys[pg.K_e]:
            self.posicion -= self.up * velocity

    def getvista(self):
        return glm.lookAt(self.posicion,self.posicion + self.forward, self.up)
    
    def getproyeccion(self):
        return glm.perspective(glm.radians(FOV), self.resolucion, NEAR, FAR)