import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from escena import Escena

class GraphicsEngine:
    def __init__(self, ventana_size=(1000,800)):
        #incializamos módulo de pygame
        pg.init()
        #tamaño ventana
        self.WIN_SIZE= ventana_size
        #atributos de openGL
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,3)
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        #detectar y usar el contexto de OpenGL
        self.ctx = mgl.create_context()
        self.ctx.enable(flags= mgl.DEPTH_TEST |mgl.CULL_FACE)
        #objeto reloj para el gameloop
        self.clock= pg.time.Clock()

        self.time= 0
        self.delta_time= 0

        #iluminacion de phong
        self.light = Light()
        #camara
        self.camera = Camera(self)
        #mesh
        self.mesh= Mesh(self)
        #escena
        self.escena = Escena(self)


    def check_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type== pg.KEYDOWN and evento.key== pg.K_ESCAPE):
                self.escena.destroy()
                self.mesh.destroy()
                pg.quit()
                sys.exit()
    
    def render(self):
        #limpiar framebuffer
        self.ctx.clear(color=(0.08,0.16,0.18))
        #renderizar escena
        self.escena.render()
        #cambiar buffers
        pg.display.flip()

    def get_time(self):
        self.time= pg.time.get_ticks()*0.001

    def run(self):
        while True:
            self.get_time()
            self.check_eventos()
            self.camera.update()
            self.render()
            self.delta_time= self.clock.tick(60)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()