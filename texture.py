import pygame as pg
import moderngl as mgl
from PIL import Image, ImageSequence

class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='texturas/piso.jpg')
        self.textures[1] = self.get_texture(path='texturas/pilar.jpg')
        self.textures[2] = self.get_texture(path='texturas/letrero.png')
        self.textures['skybox'] = self.get_texture_cube(dir_path='texturas/skybox/', ext='png')

        #expos
        self.textures[3] = self.get_texture(path= 'texturas/1.jpg')
        self.textures[4] = self.get_texture(path= 'texturas/2.jpg')
        self.textures[5] = self.get_texture(path= 'texturas/3.jpg')
        self.textures[6] = self.get_texture(path= 'texturas/4.jpg')
        self.textures[7] = self.get_texture(path= 'texturas/5.jpg')
        self.textures[8] = self.get_texture(path= 'texturas/6.jpg')
        self.textures[9] = self.get_texture(path= 'texturas/7.jpg')
        self.textures[16] = self.get_texture(path= 'texturas/8.jpg')

        #letreros
        self.textures[14] = self.get_texture(path= 'texturas/letrero2.png')
        self.textures[15] = self.get_texture(path= 'texturas/letrero3.png')    
        self.textures[10] = self.get_texture(path= 'texturas/letrero4.png')
        self.textures[11] = self.get_texture(path= 'texturas/letrero5.png')    
        self.textures[12] = self.get_texture(path= 'texturas/letrero6.png')
        self.textures[13] = self.get_texture(path= 'texturas/letrero7.png')
        self.textures[17] = self.get_texture(path= 'texturas/letrero8.png')    

    def get_texture_cube(self, dir_path, ext='png'):
        faces = ['right', 'left', 'top', 'bot'] + ['front', 'back'][::-1]
        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=False)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]

