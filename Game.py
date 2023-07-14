import os
import numpy
import pygame

def main():
    print("Start Game")
    x = 0
    y = 0
    face = pygame.image.load("face.png")    
    screen= pygame.display.set_mode((650,650), flags=0, depth=32)
    face1 = face.convert(screen)
    screen.blit(face1, (x,y))
    pygame.display.flip()
    pygame.display.set_caption("Play_Tetris")
    while True:
        e=pygame.event.wait()
        if e.type==pygame.KEYDOWN and e.key==pygame.K_LEFT:
            print("left")
            x = x - 10
            if x < 0: 
                x = 0
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_DOWN:
            print("down")
            y = y + 10
            if y > 600:
                y = 600     
        if e.type==pygame.KEYDOWN and e.key==pygame.K_UP:
            print("up")
            y = y - 10
            if y < 0:
                y = 0 
        elif e.type==pygame.KEYDOWN and e.key==pygame.K_RIGHT:
            print("right")
            x = x + 10  
            if x > 600:
                x = 600                     
        elif e.type==pygame.QUIT:
            return
        screen.fill("white")
        screen.blit(face1, (x,y))
        pygame.display.flip()


if __name__== '__main__':
    main()