import numpy as np
import glm
import pygame as pg

class BaseModel:
    def __init__(self, app, vao_nombre, tex_id, pos=(0,0,0), rot=(0,0,0), escala=(1,1,1)):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(p) for p in rot])
        self.escala = escala
        self.m_model = self.get_matriz_modelo()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_nombre]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self): 
        pass

    def get_matriz_modelo(self):
        m_model = glm.mat4()

        # traslacion
        m_model = glm.translate(m_model, self.pos)
        # rotacion en los tres ejes
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1,0,0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0,1,0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0,0,1))
        
        # escalacion
        m_model = glm.scale(m_model, self.escala)
        return m_model
    
    def render(self):
        self.update()
        self.vao.render()

class BaseModelPompeado(BaseModel):
    def __init__(self, app, vao_name, tex_id, pos, rot, escala):
        super().__init__(app, vao_name, tex_id, pos, rot, escala)
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


class Cubo(BaseModelPompeado):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0,0,0), rot=(0,0,0), escala=(1,1,1)):
        super().__init__(app, vao_name, tex_id, pos, rot, escala)

class Quad(BaseModelPompeado):
    def __init__(self, app, vao_name='quad', tex_id=2, pos=(0, 0, 0), rot=(0, 0, 0), escala=(2, 2, 2)):
        super().__init__(app, vao_name, tex_id, pos, rot, escala)

class Pilar(BaseModelPompeado):
    def __init__(self, app, vao_name='pillar', tex_id=1, pos=(0,0,0), rot=(0,0,0), escala=(1,1,1)):
        super().__init__(app, vao_name, tex_id, pos, rot, escala)

class Letrero(BaseModelPompeado):
    def __init__(self, app, vao_name='sign', tex_id=2, pos=(0,0,0), rot=(0,0,0), escala=(1,1,1)):
        super().__init__(app, vao_name, tex_id, pos, rot, escala)

class SkyBox(BaseModel):
    def __init__(self, app, vao_name='skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), escala=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, escala)
        self.on_init()

    def update(self):
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))
