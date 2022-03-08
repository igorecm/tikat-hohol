import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.font.init()
pygame.mixer.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
sound1 = pygame.mixer.Sound('res/hog.wav')

screen_width = 800
screen_height = 480
FPS = 60
tile_size = 32
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Тыкать хохлика v1.0 <3')
icon = pygame.image.load('res/icon.png')
pygame.display.set_icon(icon)

run = True
score = 0
    
class Hand():
    def __init__(self, x, y):
        img = pygame.image.load('res/hand.png')
        self.image = pygame.transform.scale(img, (151, 400))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        dx = 0
        dy = 0
        # draw
        screen.blit(self.image, self.rect)

        if self.rect.y > -120:
            dy -= 10

        # pos update
        self.rect.x += dx
        self.rect.y += dy
        
def hohol(x,y):
    img = pygame.image.load('res/hohol.png')
    img = pygame.transform.scale(img, (320, 200))
    screen.blit(img, (x,y))
    
hand = Hand (320, -120)
while run:
    screen.fill((255, 255, 255))
    hohol(240, 250)
    hand.update()
    
    textsurface1 = myfont.render('тыкать хохлика - ЛКМ', False, (0, 0, 0))
    screen.blit(textsurface1,(0,0))
    
    textsurface2 = myfont.render('тыкнуто раз: {0}'.format(score), False, (0, 0, 0))
    screen.blit(textsurface2,(0,460))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                hand = Hand (320, -70)
                score += 1
                sound1.play()

    pygame.display.update()
    fps_clock.tick(FPS)
pygame.quit()
