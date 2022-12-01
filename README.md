\\PROJET  NSI//
JEU 2D



A MODIFIER:

import pygame
from pygame.locals import*
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.key.set_repeat(30,30)
 
class Background:
    def __init__(self,win):
        self.win = win
        self.rect = [-100,-100,700,700]
  
    def show(self):
        pygame.draw.rect(self.win, (0,255,0), self.rect)
 
class Rond:
    def __init__(self, back):
        self.size = 10
        self.speed = 10
        self.back = back
        self.win = self.back.win
 
    def apply_events(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.back.rect[1] += self.speed
                if event.key == K_DOWN:
                    self.back.rect[1] += -self.speed
                if event.key == K_RIGHT:
                    self.back.rect[0] += -self.speed
                if event.key == K_LEFT:
                    self.back.rect[0] += self.speed
 
    def get_pos(self):
        return [-self.back.rect[0] + self.win.get_rect().w//2 , -self.back.rect[1] + self.win.get_rect().h//2]
 
    def show(self):
        pygame.draw.circle(self.win, (0,0,255), (win.get_rect().w//2, win.get_rect().h//2), self.size)
 
B = Background(win)
R = Rond(B)
 
play = True   
while play:
    win.fill((0,0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            play = False
             
    R.apply_events(events)
    B.show()
    R.show()
 
    print(R.get_pos())
    pygame.display.flip()
pygame.quit()
