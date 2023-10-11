import os
import alllang.config as config

_c = config.ColorMethods()


def file_to_list(path: str) -> list[str]:
    """
    Converts a txt file with words on separate lines to a list of strings

    :param path: absolute or relative path to the txt file
    :return: list of str
    """

    if (not os.path.exists(path)) or (not os.path.isfile(path)):
        print(f"{_c.red}[err]{_c.reset} Path of the file is Invalid")

    if not path.endswith('.txt'):
        print(f"{_c.yellow}[warn]{_c.reset} The path does not go to a text file, encoding error is possible")

    with open(path, 'r', encoding='utf-8') as f:
        file_content = f.read().split('\n')
        words = list(filter(None, file_content))  # remove empty strings

    return words
