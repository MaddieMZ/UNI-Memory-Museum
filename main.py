import pygame
import sys
from button import Button
import ctypes
import jueguito

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Menu')

# Get the screen width and height
screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)

BG = pygame.image.load('texturas/museo.jpg')
BG = pygame.transform.scale(BG, (screen_width, screen_height))
UNI_IMG = pygame.image.load('texturas/UNI.png')

bling = pygame.mixer.Sound('sonido/smw_coin.wav')

def get_font(size):
    return pygame.font.SysFont('comicsans', size)

def show_uni_image():
    pygame.mixer.init()
    pygame.mixer.Sound.play(bling)
    screen.blit(UNI_IMG, (screen_width/2 -154, screen_height/2 -95))
    pygame.display.update()
    pygame.time.delay(2000)  # Show the image for 2 seconds

def fade_in():
    
    fade = pygame.Surface((screen_width, screen_height))
    fade.fill((0, 0, 0))
    
    for alpha in range(0, 200):
        fade.set_alpha(200 - alpha)
        screen.blit(BG, (0, 0))
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(2)

def musiquita():
    pygame.mixer.music.load("sonido/menu.mp3") 
    pygame.mixer.music.play(-1, 0.0)

def main_menu(showLogo):
    if showLogo:
        show_uni_image()
        fade_in()
        musiquita()

    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(int(screen_height * 0.12)).render('Cave of memories', True, (182,250,247))
        MENU_RECT = MENU_TEXT.get_rect(center=(screen_width // 2, screen_height // 6))

        PLAY_BUTTON = Button(image=None, pos=(screen_width // 2, screen_height // 2), text_input='Comenzar', font=get_font(int(screen_height * 0.1)), base_color=(123,40,240), hovering_color='blue')
        CREDITS_BUTTON = Button(image=None, pos=(screen_width // 2, screen_height * 2 // 3), text_input='Créditos', font=get_font(int(screen_height * 0.1)), base_color=(123,40,240), hovering_color='blue')
        QUIT_BUTTON = Button(image=None, pos=(screen_width // 2, screen_height * 5 // 6), text_input='Salir', font=get_font(int(screen_height * 0.1)), base_color=(123,40,240), hovering_color='blue')

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def play():
    pygame.quit()  # Quit pygame instance of the menu
    jueguito.Comenzar()  # Start the game

def credits():
    pygame.display.set_caption('Credits')
    
    logo_left = pygame.image.load('texturas/logo.png')
    logo_left = pygame.transform.scale(logo_left, (int(screen_width * 0.125), int(screen_height * 0.125)))
    
    logo_right = pygame.image.load('texturas/RUSB.png')
    logo_right = pygame.transform.scale(logo_right, (int(screen_width * 0.125), int(screen_height * 0.125)))
    
    while True:
        CREDIT_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill((126, 213, 250))
        screen.blit(logo_left, (screen_width * 0.025, screen_height * 0.025))
        screen.blit(logo_right, (screen_width * 0.85, screen_height * 0.025))
        
        CREDIT_TEXT_1 = get_font(int(screen_height * 0.04)).render('UNIVERSIDAD NACIONAL DE INGENIERÍA', True, 'Black')
        CREDIT_RECT_1 = CREDIT_TEXT_1.get_rect(center=(screen_width // 2, screen_height * 0.13))
        screen.blit(CREDIT_TEXT_1, CREDIT_RECT_1)
        
        CREDIT_TEXT_2 = get_font(int(screen_height * 0.03)).render('Área de Conocimiento de Tecnología de la Información y Comunicación', True, 'Black')
        CREDIT_RECT_2 = CREDIT_TEXT_2.get_rect(center=(screen_width // 2, screen_height * 0.23))
        screen.blit(CREDIT_TEXT_2, CREDIT_RECT_2)
        
        CREDIT_TEXT_3 = get_font(int(screen_height * 0.034)).render('Proyecto UNI Cave of Memories', True, 'Black')
        CREDIT_RECT_3 = CREDIT_TEXT_3.get_rect(center=(screen_width // 2, screen_height * 0.30))
        screen.blit(CREDIT_TEXT_3, CREDIT_RECT_3)

        CREDIT_TEXT_4 = get_font(int(screen_height * 0.05)).render('Integrantes:', True, 'Black')
        CREDIT_RECT_4 = CREDIT_TEXT_4.get_rect(center=(screen_width * 0.25, screen_height * 0.40))
        screen.blit(CREDIT_TEXT_4, CREDIT_RECT_4)

        CREDIT_TEXT_5 = get_font(int(screen_height * 0.05)).render('Marín Zelaya José Antonio.  2021-0056U', True, 'white')
        CREDIT_RECT_5 = CREDIT_TEXT_5.get_rect(center=(screen_width // 2, screen_height * 0.48))
        screen.blit(CREDIT_TEXT_5, CREDIT_RECT_5)

        CREDIT_TEXT_6 = get_font(int(screen_height * 0.05)).render('Martínez González Sergio Daniel.  2022-0353U', True, 'white')
        CREDIT_RECT_6 = CREDIT_TEXT_6.get_rect(center=(screen_width // 2, screen_height * 0.53))
        screen.blit(CREDIT_TEXT_6, CREDIT_RECT_6)

        CREDIT_TEXT_7 = get_font(int(screen_height * 0.05)).render('Vargas Salinas Caroline Gabriela.  2022-0342U', True, 'white')
        CREDIT_RECT_7 = CREDIT_TEXT_7.get_rect(center=(screen_width // 2, screen_height * 0.58))
        screen.blit(CREDIT_TEXT_7, CREDIT_RECT_7)

        CREDIT_TEXT_8 = get_font(int(screen_height * 0.05)).render('Villalobo Soza Camilo Sebastian.  2022-0291U', True, 'white')
        CREDIT_RECT_8 = CREDIT_TEXT_8.get_rect(center=(screen_width // 2, screen_height * 0.63))
        screen.blit(CREDIT_TEXT_8, CREDIT_RECT_8)
        
        CREDIT_TEXT_9 = get_font(int(screen_height * 0.05)).render('Docente: Ing. Danny Oswaldo Chávez Miranda', True, 'black')
        CREDIT_RECT_9 = CREDIT_TEXT_9.get_rect(center=(screen_width // 2, screen_height * 0.73))
        screen.blit(CREDIT_TEXT_9, CREDIT_RECT_9)

        CREDIT_BACK = Button(image=None, pos=(screen_width * 0.9, screen_height * 0.9), text_input='Back', font=get_font(int(screen_height * 0.07)), base_color='black', hovering_color='blue')

        CREDIT_BACK.changeColor(CREDIT_MOUSE_POS)
        CREDIT_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDIT_BACK.checkForInput(CREDIT_MOUSE_POS):
                    main_menu(False) 

        pygame.display.update()

main_menu(True)
