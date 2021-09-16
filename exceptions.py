class NumTooHigh(Exception):
    "Raised when random picker has to choose more files than are available in the folders"
    pass


class WindowSizeIsWrong(Exception):
    "Raised when resizer is given a window size that does not return int tile sizes."

    def __init__(self, msg):
        super().__init__(msg)
