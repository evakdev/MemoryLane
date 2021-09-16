from enum import Enum
from pathlib import Path


### File Getter
def file_getter(folder, accepted_suffixes=[".jpg", ".jpeg", ".png"]):
    """Returns list of all files in a folder."""

    file_list = [
        str(file) for file in folder.iterdir() if file.suffix in accepted_suffixes
    ]
    return file_list


###############

game_title = "Memory Lane"

# Options
class Difficulty(Enum):
    SIZE4 = "4 x 4"
    SIZE6 = "6 x 6"
    SIZE8 = "8 x 8"
    SIZE10 = "10 x 10"
    # SIZE12 = "12 x 12"


difficulties = {
    Difficulty.SIZE4: 4,
    Difficulty.SIZE6: 6,
    Difficulty.SIZE8: 8,
    Difficulty.SIZE10: 10,
    # Difficulty.SIZE12: 12,
}


# Measurements
card_measures = {
    Difficulty.SIZE4: 148,
    Difficulty.SIZE6: 98,
    Difficulty.SIZE8: 73,
    Difficulty.SIZE10: 58,
    # Difficulty.SIZE12: 48,
}

button_measures = {
    Difficulty.SIZE4: (55 + 85, 350),
    Difficulty.SIZE6: (55 + 85 + 22 + 150, 350),
    Difficulty.SIZE8: (55 + 85, 411),
    Difficulty.SIZE10: (55 + 85 + 22 + 150, 411),
}


windowsize = 602
card_sides = 2
title_measures = (112, 200)
title_font_size = 55
title_color = (0, 0, 0)
button_text_color = (0, 0, 0)
button_font_size = 20
button_size = (150, 40)
line_thickness = 2

# File Paths

folder = Path(__file__).resolve().parent
images = Path.joinpath(folder, "images")
fonts = Path.joinpath(folder, "fonts")

title_font = str(Path.joinpath(fonts, "HighlandGothicFLF-Bold.ttf"))
button_font = str(Path.joinpath(fonts, "SansPosterBold.ttf"))

black_pic = icon_pic = Path.joinpath(images, "black.png")
welcome_pic = str(Path.joinpath(images, "welcome backs", "jungle1.jpg"))
icon_pic = Path.joinpath(images, "icon.png")
backgrounds_all = file_getter(Path.joinpath(images, "backgrounds"))
cardbacks_all = file_getter(Path.joinpath(images, "cardbacks"))
cardfronts_all = file_getter(Path.joinpath(images, "cardfronts"))
buttons_all = file_getter(Path.joinpath(images, "buttons"))
