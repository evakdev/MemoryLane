import pygame

from config import game_title, icon_pic, windowsize

pygame.init()
display = pygame.display
screen = display.set_mode((windowsize, windowsize))
icon = pygame.image.load(icon_pic)
display.set_icon(icon)
display.set_caption(game_title)
screen.fill((0, 0, 0))
