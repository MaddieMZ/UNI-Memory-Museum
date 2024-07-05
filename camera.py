import glm
import pygame as pg
import time

FOV = 50 # grados xd
NEAR = 0.1
FAR = 100
SPEED = 0.0290
SENSITIVITY = 0.05
MOVE_DURATION = 0.5 # seconds

class Camera:
    def __init__(self, app, posicion=(0,0,4), yaw=-90, pitch=0):
        self.app = app
        self.resolucion = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.posicion = glm.vec3(2, 3, 3)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        # angulos de euler
        self.yaw = yaw
        self.pitch = pitch
        # matriz vista
        self.m_view = self.getvista()
        # matriz de proyección
        self.m_proj = self.getproyeccion()

        self.moving = False

        # Movement timing
        self.move_start_time = {}
        self.movement_triggered = {

            pg.K_a: False,
            pg.K_d: False,

        }

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        #self.rotate()
        self.update_camera_vectors()
        self.m_view = self.getvista()

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        current_time = time.time()

        
        for key in [pg.K_a, pg.K_d ]:
            if keys[key] and not self.movement_triggered[key]:
                self.move_start_time[key] = current_time
                self.movement_triggered[key] = True

        #
        for key, direccion1, direccion2 in [
            (pg.K_a, -self.right, -self.forward),
            (pg.K_d, self.right, self.forward)
        ]:
            if key in self.move_start_time and current_time - self.move_start_time[key] < MOVE_DURATION :
                
                self.posicion += direccion1 * velocity
                self.posicion += direccion2 * velocity
                

            elif key in self.move_start_time and current_time - self.move_start_time[key] >= MOVE_DURATION :
                self.movement_triggered[key] = False
                

    def getvista(self):
        return glm.lookAt(self.posicion, self.posicion + self.forward, self.up)

    def getproyeccion(self):
        return glm.perspective(glm.radians(FOV), self.resolucion, NEAR, FAR)
