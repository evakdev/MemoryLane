import config
from gameinit import display, screen
from sprites import Background, Button, Title


class WelcomePage:
    def __init__(self):
        self.buttons = self.make_buttons()
        self.make_backgrounds()
        self.make_title()
        self.blit_all()

    def make_buttons(self):
        buttons = []
        for difficulty, measure in config.button_measures.items():
            button = Button(difficulty)
            button.move(measure)
            buttons.append(button)
        return buttons

    def make_backgrounds(self):
        self.background = Background(
            config.welcome_pic, (config.windowsize, config.windowsize)
        )

    def make_title(self):
        self.title = Title(config.game_title)
        self.title.move(config.title_measures)

    def blit_all(self):
        self.background.blit(screen)
        self.title.blit(screen)
        for button in self.buttons:
            button.blit_initial(screen)
        display.flip()

    def hover_action(self, cursor):
        for button in self.buttons:
            if button.is_hovered(cursor):
                button.blit_hover(screen)
            else:
                button.blit_initial(screen)
            display.flip()

    def click_action(self, cursor):
        for button in self.buttons:
            if button.is_hovered(cursor):
                button.blit_click(screen)
                display.flip()
                return True
        return False

    def get_button_clicked(self, cursor):
        for button in self.buttons:
            if button.is_hovered(cursor):
                return button.difficulty


welcome = WelcomePage()
welcome.make_title()
