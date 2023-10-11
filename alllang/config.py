import colorama


class ColorMethods:
    def __init__(self):
        colorama.init()
        self.reset = colorama.Style.RESET_ALL
        self.red = colorama.Fore.RED
        self.green = colorama.Fore.GREEN
        self.yellow = colorama.Fore.YELLOW
        self.bright = colorama.Style.BRIGHT
        self.dim = colorama.Style.DIM
