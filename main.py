import pygame
import os
import add

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 640,360
size = (width, height)

pygame.init()
pygame.display.set_caption("Симуляция Жизни, Conway's")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 59

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)
red = (255,0,0)
green = (0,255,0)

scaler = 10  # Размер одной клетки
offset = 1 # Линия включена или отключена

Grid = add.Grid(width,height, scaler, offset)
Grid.random2d_array()


run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Grid.Conway(off_color=white, on_color=green, surface=screen)
    pygame.display.update()

pygame.quit()