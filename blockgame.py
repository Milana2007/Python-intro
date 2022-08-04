import pygame
import sys




pygame.init()
window = pygame.display.set_mode((500,400))
pygame.display.set_caption('blockgame')


BLUE = (50, 84, 168)
PINK = (230, 7, 140)

def change_color(curr_color):
    if curr_color == PINK:
        curr_color = BLUE
        print(curr_color)
    else:
        curr_color = PINK
        print(curr_color)
    return curr_color


p1 = pygame.Rect(100,130,40,40)
    
p2 = pygame.Rect(350,130,40,40)

pygame.display.update()

BGcolor = PINK
window.fill(BGcolor)

def run():
    global BGcolor, p1, p2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    curr_time = pygame.time.get_ticks()
    if curr_time % 2000 == 0:
        BGcolor = change_color(BGcolor)

    keys=pygame.key.get_pressed()
    if keys[ord('w')]:
        p1.y -= 1
      
        keys=pygame.key.get_pressed()
    if keys[ord('s')]:
        p1.y += 1

    keys=pygame.key.get_pressed()
    if keys[ord('a')]:
        p1.x -= 1
        
        keys=pygame.key.get_pressed()
    if keys[ord('d')]:
        p1.x += 1

        keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        p2.x -= 1

    if keys[pygame.K_RIGHT]:
        p2.x += 1

    if keys[pygame.K_UP]:
        p2.y -= 1

    if keys[pygame.K_DOWN]:
        p2.y += 1
        


    window.fill(BGcolor)
    
    

    pygame.draw.rect(window, (50,84,161), p1)
    pygame.draw.rect(window, (0, 0, 0), p1, width = 1)

    
    
    pygame.draw.rect(window, (230,7,133), p2)
    pygame.draw.rect(window, (0, 0, 0), p2, width = 1)


    pygame.display.update()

while True:
    run()