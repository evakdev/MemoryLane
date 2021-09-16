import random
import time

import config
from exceptions import NumTooHigh, WindowSizeIsWrong


### Decorators
def timeme(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"ran {func.__name__} in {end-start} seconds")
        return result

    return wrapper


# Random Picker


def random_picker(items: list, num_to_pick: int):
    """returns a single item if num_to_pick is 1.
    returns a list of items if num_to_pick is >1.
    """
    if num_to_pick > len(items):
        raise NumTooHigh

    if num_to_pick == 1:
        return random.choice(items)

    choices = []
    while len(choices) < num_to_pick:
        chosen = random.choice(items)
        if chosen not in choices:
            choices.append(chosen)
    return choices


# For Changing default window size, card size, and config.difficulties.
def card_sizer(card_num_in_row, windowsize=config.windowsize):
    """
    Returns cardsize based on number of cards in row/col (e.g. 4 for "4 x 4").
    Use this if you changed config.windowsize and/or config.difficulties to figure out the new card size.
    """
    borders = 2 * config.card_sides
    space_between_cards = (card_num_in_row - 1) * config.card_sides
    cards_combined = config.windowsize - (borders + space_between_cards)
    card_size = cards_combined / card_num_in_row
    if card_size == int(card_size):
        return int(card_size)
    raise WindowSizeIsWrong(msg=f"Calculated {card_size}, which is not an integer")


def window_size_finder(minimum=100, maximum=800):
    """
    Returns list of numbers that can be divided to equal cards for all config.difficulties.
    """

    options = []
    for num in range(minimum, maximum + 1):
        cnt = 0

        for size in config.difficulties.values():

            try:
                card_sizer(size, windowsize=num)
                cnt += 1
            except:
                break

        if cnt == len(list(config.difficulties.values())):
            options.append(num)
    return options
