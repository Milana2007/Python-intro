import pygame
import sys

class RGB:

    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue

    def tuple(self):
        return (self.r, self.g, self.b)
    
    def css_string(self):
        return f"rgb({self.r}, {self.g}, {self.b},)"
    
    def adjust_red(self, delta):
        cand = self.r + delta
        if cand < 0:
            self.r = 0
        elif cand > 255:
            self.r = 255
        else:
            self.r = cand

pygame.init()
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption("RGB Helper")

current_color = RGB(200,5,80)
def run():
    #x-cord, y-cord, width, height
    appFont = pygame.font.SysFont('ubuntu', 18)

    redText = appFont.render(f'{current_color.r}red', True,(0,0,0),(255,255,255))
    redRect = pygame.Rect(30, 20, 100, 30)
    greenText = appFont.render(f'{current_color.r}green', True,(0,0,0),(255,255,255))
    greenRect =  pygame.Rect(30, 20, 100, 30)
    blueRect = pygame.Rect(30, 20, 100, 30)
    blueText = appFont.render(f'{current_color.r}blue', True,(0,0,0),(255,255,255))
    
    swatchRect = pygame.Rect(150, 50, 150,50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame. K_r:
                current_color.adjust_red(1)
            elif event.key == pygame.K_t:
                current_color.adjust_red(8)
            elif event.key == pygame.K_e:                
                current_color.adjust_red(-1)
            elif event.key == pygame.K_w:
                current_color.adjust_red(-8)


    window.fill((255,255,255))
    window.blit(redText, redRect)

    pygame.draw.rect(window, (0,0,0), redRect, width=1)

    pygame.draw.rect(window, current_color.tuple(), swatchRect)
    pygame.display.update()

while True:
    run()