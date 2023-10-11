import os
import alllang.config as config

_c = config.ColorMethods()


def is_txt_file(path: str) -> bool:
    """
    Print err and warns, if the file don't exist, or it's non txt

    :param path: absolute or relative path to the checking file
    :return: True, if everything is fine
    """
    flag = True

    if (not os.path.exists(path)) or (not os.path.isfile(path)):
        print(f"{_c.red}[err]{_c.reset} Path of the file is Invalid")
        flag = False

    if not path.endswith('.txt'):
        print(f"{_c.yellow}[warn]{_c.reset} The path does not go to a text file, encoding error is possible")
        flag = False

    return flag
