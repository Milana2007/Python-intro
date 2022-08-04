import pygame
import sys
from math import floor

#count milliseconds
#count only on clik/

def millis_to_time(millis):
    mins = floor(millis/(1000*60))
    leftover = millis %(1000*60)
    secs = floor(leftover / 1000 )
    mils = leftover % 1000
    return(mins,seconds,mils)


pygame.init()
win = pygame.display.set_mode((300,300))
pygame.display.set_caption('stopwatch')

theFont = pygame.font.SysFont(False,80)


t0 = pygame.time.get_ticks()
millis = 0
timer_on = False



def run():
    global t0
    global millis
    global timer_on
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            timer_on = not timer_on
            if timer_on:
                millis = 0
                t0 = pygame.time.get_ticks() 
    
    if timer_on:
        millis = pygame.time.get_ticks() - t0
    
    win.fill ((255,255,255))

    time_tup = millis_to_time(millis) # (min, sec, ms)
    timerText = theFont.render(f"{time_tup[0]}:{time_tup[1]}:{time_tup[2]}", True, (0,0,0), (255,255,255))
    timerRect = 

    win.blit(timerText, timerRect)

    pygame.draw.rect(win, (255,255,255), timeRect)
    
    pygame.display.update()
while True:
    run()