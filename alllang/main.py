import os


def file_to_list(path: str) -> list[str]:
    """
    Converts a file with words on separate lines to a list of strings

    :param path: absolute or relative path to the file
    :return: list of str
    """

    if (not os.path.exists(path)) or (not os.path.isfile(path)):
        print("Path of the file is Invalid")

    with open(path, 'r', encoding='utf-8') as f:
        file_content = f.read().split('\n')
        words = list(filter(None, file_content))  # remove empty strings

    return words
