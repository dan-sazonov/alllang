from alllang.cli import is_txt_file as _check_path

from deep_translator import GoogleTranslator

_lang_list = list(GoogleTranslator().get_supported_languages())


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


def all_lang_trans(word: str, lang_list=None) -> dict[str, str]:
    """
    Translates the `word` into all languages

    :param lang_list: list[str]. Languages into which the word will be translated. By default, all supported languages
    :param word: the word to be translated
    :return: dict where the key is the name of the language, the value is the translation
    """
    if lang_list is None:
        lang_list = _lang_list

    out = dict()
    for lang in lang_list:
        my_translator = GoogleTranslator(source='auto', target=lang)
        result = my_translator.translate(text=word)
        out[lang] = result

    return out


def transl_from_file(path: str, lang_list=None):
    if lang_list is None:
        lang_list = _lang_list

    word_list = file_to_list(path)
    out = dict()

    for word in word_list:
        out[word] = all_lang_trans(word, lang_list=lang_list)

    return out
