from enum import Enum

import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT

from main import MemoryGame
from welcome import WelcomePage


# Game Run Tools
def clicked(event):
    return event.type == MOUSEBUTTONDOWN and event.button == 1


def quitted(event):
    return event.type == QUIT


class Screen(Enum):
    Welcome = "welcome"
    Game = "game"


screen_on = Screen.Welcome
welcome_screen = WelcomePage()
game_screen = None

while screen_on:
    for event in pygame.event.get():
        cursor = pygame.mouse.get_pos()

        if quitted(event):
            screen_on = None
            break
        elif screen_on == Screen.Welcome:
            welcome_screen.hover_action(cursor)
            if clicked(event):
                click_action = welcome_screen.click_action(cursor)
                if click_action:
                    difficulty = welcome_screen.get_button_clicked(cursor)
                    print("Loading ....")
                    game_screen = MemoryGame(difficulty)
                    screen_on = Screen.Game
        elif screen_on == Screen.Game and clicked(event):
            game_screen.proccess(cursor)

            pygame.event.pump()
