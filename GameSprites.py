import pygame
from pygame.locals import RLEACCEL
import config


class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, pic, size):
        super().__init__()
        self.surf = pygame.image.load(pic)
        self.surf = pygame.Surface.convert_alpha(self.surf)
        self.surf = pygame.transform.scale(self.surf, size)
        self.rect = self.surf.get_rect()

    def blit(self, screen):
        screen.blit(self.surf, self.rect)

    def move(self, coordinations):
        self.rect.move_ip(coordinations)

    def fix_transparency(self):
        self.surf.set_alpha(250)


class Front(ImageSprite):
    ...  # Front Cards


class Back(ImageSprite):
    ...  # Back of the Cards


class Background(ImageSprite):
    ...  # The Background to be Revealed


class Text(pygame.sprite.Sprite):
    def __init__(self, text, font, font_size, color):
        super().__init__()
        font = pygame.font.Font(font, font_size, bold=True)
        self.surf = font.render(text, False, color)
        self.rect = self.surf.get_rect()
        self.text = text

    def blit(self, screen):
        screen.blit(self.surf, self.rect)

    def move(self, coordinations):
        self.rect.move_ip(coordinations)


class Title(Text):
    def __init__(self, text):
        super().__init__(
            text, config.title_font, config.title_font_size, config.title_color
        )


class Lines:
    def __init__(self, difficulty, screen):
        self.thickness = config.line_thickness
        self.color = config.title_color
        self.card_width = config.card_measures.get(difficulty)
        self.line_num = self.get_num_of_lines_for_difficulty(difficulty)
        self.horizontal_lines = self.add_horizontal_lines(screen)
        self.vertical_lines = self.add_vertical_lines(screen)

    def get_num_of_lines_for_difficulty(self, difficulty):
        card_num_in_row = config.difficulties.get(difficulty)
        line_num = config.windowsize - (card_num_in_row * self.card_width)
        line_num = line_num // self.thickness

        return line_num

    def draw(self, start, end, screen):
        return pygame.draw.line(
            screen,
            self.color,
            start,
            end,
            self.thickness,
        )

    def add_vertical_lines(self, screen):
        lines = []
        start_at = 0
        for i in range(0, self.line_num):
            new_line = self.draw((start_at, 0), (start_at, config.windowsize), screen)
            lines.append(new_line)
            start_at += self.thickness + self.card_width
        return lines

    def add_horizontal_lines(self, screen):
        lines = []
        start_at = 0

        for i in range(0, self.line_num):
            new_line = self.draw((0, start_at), (config.windowsize, start_at), screen)
            lines.append(new_line)
            start_at += self.thickness + self.card_width
        return lines


class Button:
    def __init__(self, text):
        self.name = self.get_text_or_difficulty(text)
        self.size = config.button_size
        self.text = Text(
            self.name,
            config.button_font,
            config.button_font_size,
            config.button_text_color,
        )
        self.initial = ImageSprite(config.buttons_all[0], self.size)
        self.hover = ImageSprite(config.buttons_all[1], self.size)
        self.click = ImageSprite(config.buttons_all[2], self.size)
        self.fix_transparency()

    def fix_transparency(self):
        self.initial.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.hover.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.click.surf.set_colorkey((0, 0, 0), RLEACCEL)

    def get_text_or_difficulty(self, text):
        if isinstance(text, config.Difficulty):
            self.difficulty = text
            return text.value
        return text

    def move(self, coordination):
        self.initial.rect.move_ip(coordination)
        self.hover.rect.move_ip(coordination)
        self.click.rect.move_ip(coordination)
        self.textcenter = (
            coordination[0] + (self.size[0] - self.text.surf.get_width()) / 2,
            coordination[1] + (self.size[1] - self.text.surf.get_height()) / 2,
        )
        self.text.rect.move_ip(self.textcenter)
        return

    def is_hovered(self, cursor):
        return self.initial.rect.collidepoint(cursor)

    def blit_initial(self, screen):
        screen.blit(self.initial.surf, self.initial.rect)
        screen.blit(self.text.surf, self.text.rect)
        return

    def blit_hover(self, screen):
        screen.blit(self.hover.surf, self.hover.rect)
        screen.blit(self.text.surf, self.text.rect)
        return

    def blit_click(self, screen):
        screen.blit(self.click.surf, self.click.rect)
        screen.blit(self.text.surf, self.text.rect)
        return
