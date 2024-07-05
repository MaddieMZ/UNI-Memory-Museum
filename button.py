import pygame 
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Button')


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.xpos = pos[0]
        self.ypos = pos[1]
        self.text_input = text_input
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text = self.font.render(self.text_input, True, self.base_color)

        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.xpos, self.ypos))
        self.text_rect = self.text.get_rect(center=(self.xpos, self.ypos))

    def update(self, screen):
        if self.image is None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input,True, self.hovering_color)

        else:
            self.text = self.font.render(self.text_input, True, self.base_color)