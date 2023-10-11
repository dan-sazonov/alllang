from alllang.cli import is_txt_file as _check_path

from deep_translator import GoogleTranslator

_lang_list = GoogleTranslator().get_supported_languages()


def file_to_list(path: str) -> list[str]:
    """
    Converts a txt file with words on separate lines to a list of strings

    :param path: absolute or relative path to the txt file
    :return: list of str
    """
    _check_path(path)

    with open(path, 'r', encoding='utf-8') as f:
        file_content = f.read().split('\n')
        words = list(filter(None, file_content))  # remove empty strings

    return words


def translate_all(word: str) -> dict[str, str]:
    """
    Translates the `word` into all languages

    :param word: the word to be translated
    :return: dict where the key is the name of the language, the value is the translation
    """
    out = dict()

    for lang in _lang_list:
        my_translator = GoogleTranslator(source='auto', target=lang)
        result = my_translator.translate(text=word)
        out[lang] = result

    return out
