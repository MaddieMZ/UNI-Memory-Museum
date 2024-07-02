import numpy as np
import glm
import pygame as pg


class BaseModel:
    def __init__(self, app, vao_nombre, tex_id,pos=(0,0,0)):
        self.app= app
        self.pos=pos
        self.m_model = self.get_matriz_modelo()
        self.tex_id = tex_id
        self.vao= app.mesh.vao.vaos[vao_nombre]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self): ...

    def get_matriz_modelo(self):
        m_model = glm.mat4()

        #traslacion
        m_model= glm.translate(m_model,self.pos)
        return m_model
    
    def render(self):
        self.update()
        self.vao.render()

class Cubo(BaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0,0,0)):
        super().__init__(app, vao_name, tex_id,pos)
        self.on_init()

    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.camera.posicion)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.amb'].write(self.app.light.amb)
        self.program['light.dif'].write(self.app.light.dif)
        self.program['light.spec'].write(self.app.light.spec)
