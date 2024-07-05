import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from escena import Escena
import ctypes


class GraphicsEngine:
    def __init__(self, ventana_size=(ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))):
        # Inicializamos módulo de pygame
        pg.init()
        # Tamaño ventana
        self.WIN_SIZE = ventana_size
        screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        # Atributos de OpenGL
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # Detectar y usar el contexto de OpenGL
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # Objeto reloj para el gameloop
        self.clock = pg.time.Clock()

        self.time = 0
        self.delta_time = 0

        # Iluminación de Phong
        self.light = Light()
        # Cámara
        self.camera = Camera(self)
        # Mesh
        self.mesh = Mesh(self)
        # Escena
        self.escena = Escena(self)
        
        self.fade_duration = 1.0  # Fade duration in seconds
        self.start_time = pg.time.get_ticks() * 0.001  # Start time in seconds
    def check_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                self.escena.destroy()
                self.mesh.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        self.ctx.clear(color=(0,0,0))
        # Renderizar escena
        self.escena.render()
        # Cambiar buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_eventos()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)

def Comenzar():
    app = GraphicsEngine()
    app.run()
