import random
from time import sleep

import pygame

import config
from gameinit import display, screen
from GameSprites import Back, Background, Front, Lines
from tools import random_picker


class Card:
    def __init__(self, pic_front, pic_back, size):
        self.size = size
        self.pic_front = pic_front
        self.pic_back = pic_back
        self.front = Front(pic_front, (size, size))
        self.back = Back(pic_back, (size, size))

    def blit_front(self, screen):
        screen.blit(self.front.surf, self.front.rect)

    def blit_back(self, screen):
        screen.blit(self.back.surf, self.back.rect)

    def blit_both(self, screen):
        self.blit_front(screen)
        self.blit_back(screen)

    def move_both(self, coordinations):
        self.front.move(coordinations)
        self.back.move(coordinations)

    def kill_both(self):
        self.back.kill()
        self.front.kill()


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.picture = ""
        self.cardpic_back = list()
        self.cardpic_fronts = list()
        self.cardfront_order = list()
        self.cards = list()
        self.remaining_cards = list()
        self.sprite_group = pygame.sprite.Group()
        self.card_size = config.card_measures.get(difficulty)
        self.card_num_in_row = config.difficulties.get(difficulty)
        self.cards_facing_front = []
        self.prepare_for_run()

    def prepare_for_run(self):
        self.variety_num = self.set_cardfront_variety_num()
        self.set_random_pics()
        self.set_cardfront_order()
        self.make_picture()
        self.make_cards()
        self.blit_all_initial()

    @property
    def num_facing_front(self):
        return len(self.cards_facing_front)

    def proccess(self, cursor):
        for card in self.remaining_cards:
            if not card.back.rect.collidepoint(cursor):
                continue
            if card in self.cards_facing_front:
                continue
            self.check_card(card)

    def set_cardfront_variety_num(self):
        return self.card_num_in_row

    def set_random_pics(self):
        self.picture = random_picker(config.backgrounds_all, 1)
        self.cardpic_fronts = random_picker(config.cardfronts_all, self.variety_num)
        self.cardpic_back = random_picker(config.cardbacks_all, 1)

    def set_cardfront_order(self):
        self.cardfront_order = []
        total_cards_num = self.card_num_in_row ** 2
        while len(self.cardfront_order) < total_cards_num:
            choice = random.choice(self.cardpic_fronts)
            duplicate_count = self.cardfront_order.count(choice)
            if duplicate_count < self.variety_num:
                self.cardfront_order.append(choice)

    def make_picture(self):
        size = (config.windowsize, config.windowsize)
        self.picture_sprite = Background(self.picture, size)

    def make_lines(self):
        self.lines = Lines(self.difficulty, screen)

    def make_cards(self):
        total_cards_num = len(self.cardfront_order)
        for i in range(total_cards_num):
            pic_front = self.cardfront_order[i]
            card = Card(pic_front, self.cardpic_back, self.card_size)
            self.cards.append(card)
            self.sprite_group.add(card.front, card.back)
        self.remaining_cards = self.cards.copy()

    def blit_cards_initial(self):
        x, y = config.card_sides, config.card_sides

        for row in range(self.card_num_in_row):
            for col in range(self.card_num_in_row):
                index = col + (row * self.card_num_in_row)
                card = self.cards[index]
                card.move_both((x, y))
                card.blit_both(screen)
                x += config.card_sides + self.card_size
            x = config.card_sides
            y += config.card_sides + self.card_size

    def blit_all_initial(self):
        self.picture_sprite.blit(screen)
        self.blit_cards_initial()
        self.make_lines()
        display.flip()

    def blit_all_during(self):
        self.picture_sprite.blit(screen)
        for card in self.remaining_cards:
            card.blit_both(screen)
            self.make_lines()
        display.flip()

    def close_unmatching_cards(self):
        for card in self.cards_facing_front:
            card.blit_back(screen)
            display.flip()
        self.cards_facing_front = []

    def show_card_front(self, card):
        card.blit_front(screen)
        display.flip()
        if not (card in self.cards_facing_front):
            self.cards_facing_front.append(card)

    def remove_matching_cards(self):
        for card in self.cards_facing_front:
            card.kill_both()
            self.remaining_cards.remove(card)
        self.cards_facing_front = []
        self.blit_all_during()
        display.flip()

    def fronts_match(self):
        if self.cards_facing_front:
            card1 = self.cards_facing_front[0]
            card2 = self.cards_facing_front[1]
            return card1.pic_front == card2.pic_front

    def check_card(self, card):
        self.show_card_front(card)
        if self.num_facing_front == 2:
            sleep(0.7)
            if self.fronts_match():
                self.remove_matching_cards()
            else:
                self.close_unmatching_cards()
