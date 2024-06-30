

class ShaderProgram:
    def __init__(self,ctx):
        self.ctx = ctx
        self.programs={}
        self.programs['default'] = self.get_program('default')

    def get_program(self, nombre_program):
        with open(f'shaders/{nombre_program}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{nombre_program}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader,fragment_shader=fragment_shader)
        return program
    
    def destroy(self):
        [program.release() for program in self.programs.values()]