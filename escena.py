from model import *
import pygame as pg
class Escena:
    def __init__(self, app):
        self.app= app
        self.objetos= []
        self.cargar()
        #skybox
        self.skybox= SkyBox(app)
        pg.mixer.init()
        pg.mixer.music.load("sonido/background.mp3") 
        pg.mixer.music.play(-1,0.0)

    def add_objetos(self,obj):
        self.objetos.append(obj)

    def cargar(self):
        app=self.app
        add= self.add_objetos

        n, s = 130, 2

        for x in range(-20, n, s):  # Expand in the positive x-direction
            for z in range(0, -n, -s):  # Expand in the negative z-direction
                add(Cubo(app, pos=(x, -s, z)))

        #inicio
        add(Pilar(app, pos=(0,0,-5)))
        add(Pilar(app, pos=(5,0,-8)))
        add(Quad(app,pos=(2,3,-3), rot=(0,90,0), tex_id=3))
        add(Letrero(app,pos=(-2,0,-5),escala=(2,2,2), rot=(0,45,0)))

        #exposicion 1
        add(Pilar(app, pos=(15,0,-20)))
        add(Pilar(app, pos=(20,0,-23)))
        add(Quad(app,pos=(17,3,-18), rot=(0,90,0), tex_id=4))
        add(Letrero(app,pos=(13,0,-20),escala=(2,2,2), rot=(0,45,0), tex_id=14))  

        #exposicion 2
        add(Pilar(app, pos=(30,0,-35)))
        add(Pilar(app, pos=(35,0,-38)))
        add(Quad(app,pos=(32,3,-33), rot=(0,90,0), tex_id=5))
        add(Letrero(app,pos=(28,0,-35),escala=(2,2,2), rot=(0,45,0), tex_id=15))

        #exposicion 3
        add(Pilar(app, pos=(45,0,-50)))
        add(Pilar(app, pos=(50,0,-53)))
        add(Quad(app,pos=(47,3,-48), rot=(0,90,0), tex_id=6))
        add(Letrero(app,pos=(43,0,-50),escala=(2,2,2), rot=(0,45,0), tex_id=10))

        #exposicion 4
        add(Pilar(app, pos=(60,0,-65)))
        add(Pilar(app, pos=(65,0,-68)))
        add(Quad(app,pos=(62,3,-63), rot=(0,90,0), tex_id=7))
        add(Letrero(app,pos=(58,0,-65),escala=(2,2,2), rot=(0,45,0), tex_id=11))

        #exposicion 5
        add(Pilar(app, pos=(75,0,-80)))
        add(Pilar(app, pos=(80,0,-83)))
        add(Quad(app,pos=(77,3,-78), rot=(0,90,0), tex_id=8))
        add(Letrero(app,pos=(73,0,-80),escala=(2,2,2), rot=(0,45,0), tex_id=12))

        #exposicion 6
        add(Pilar(app, pos=(90,0,-95)))
        add(Pilar(app, pos=(95,0,-98)))
        add(Quad(app,pos=(92,3,-93), rot=(0,90,0), tex_id=9))
        add(Letrero(app,pos=(88,0,-95),escala=(2,2,2), rot=(0,45,0), tex_id=13))

        #exposicion 7
        add(Pilar(app, pos=(105,0,-110)))
        add(Pilar(app, pos=(110,0,-113)))
        add(Quad(app,pos=(107,3,-108), rot=(0,90,0), tex_id=16))
        add(Letrero(app,pos=(103,0,-110),escala=(2,2,2), rot=(0,45,0), tex_id=17))

    def render(self):
        for obj in self.objetos:
            obj.render()
        self.skybox.render()

    def destroy(self):
        pg.quit()