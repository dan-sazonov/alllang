import os
import colorama


class _ColorMethods:
    # todo add fucking docstring
    def __init__(self):
        colorama.init()
        self.reset = colorama.Style.RESET_ALL
        self.red = colorama.Fore.RED
        self.green = colorama.Fore.GREEN
        self.yellow = colorama.Fore.YELLOW
        self.bright = colorama.Style.BRIGHT
        self.dim = colorama.Style.DIM

    def red_txt(self, txt): return f"{self.red}{txt}{self.reset}"
    def yel_txt(self, txt): return f"{self.yellow}{txt}{self.reset}"


_c = _ColorMethods()


def is_txt_file(path: str) -> bool:
    """
    Print err and warns, if the file don't exist, or it's non txt

    :param path: absolute or relative path to the checking file
    :return: True, if everything is fine
    """
    flag = True

    if (not os.path.exists(path)) or (not os.path.isfile(path)):
        print(f"{_c.red_txt('[err]')} Path of the file is Invalid")
        flag = False

    if not path.endswith('.txt'):
        print(f"{_c.yel_txt('[warn]')} The path does not go to a text file, encoding error is possible")
        flag = False

    return flag
