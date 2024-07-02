from model import *

class Escena:
    def __init__(self, app):
        self.app= app
        self.objetos= []
        self.cargar()

    def add_objetos(self,obj):
        self.objetos.append(obj)

    def cargar(self):
        app=self.app
        add= self.add_objetos

        
        add(Cubo(app,tex_id=0, pos=(-2.5,0,0)))
        add(Cubo(app,tex_id=0, pos= (2.5,0,0)))
        add(Cubo(app,tex_id=0, pos= (2.5,2,0)))

    def render(self):
        for obj in self.objetos:
            obj.render()