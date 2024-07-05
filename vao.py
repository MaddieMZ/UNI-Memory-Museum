from vbo import VBO
from shader_program import ShaderProgram

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])
        
        # Pilar vao
        self.vaos['pillar'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['pillar'])
        
        # Letrero vao
        self.vaos['sign'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['sign'])        

        #skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo= self.vbo.vbos['skybox'])
        
        #quad vao
        self.vaos['quad'] = self.get_vao(
            program= self.program.programs['default'],
            vbo = self.vbo.vbos['quad'])
        




    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
