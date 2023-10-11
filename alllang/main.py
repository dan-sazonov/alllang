from unidecode import unidecode

from alllang.cli import is_txt_file as _check_path

from deep_translator import GoogleTranslator
import re

_lang_list = list(GoogleTranslator().get_supported_languages())


def _file_to_list(path) -> list[str]:
    """
    Converts a txt file with words on separate lines to a list of strings

    :param path: absolute or relative path to the txt file
    :return: list of str
    """

    with open(path, 'r', encoding='utf-8') as f:
        file_content = f.read().split('\n')
        words = list(filter(None, file_content))  # remove empty strings

    return words


def _is_latin(string):
    pattern = r'^[a-zA-Z\u0080-\u024F]+$'
    return bool(re.match(pattern, string.replace("'", "")))


class Translator:

    def __init__(self, lang_list=None, latin_spelling=False):
        self.lang_list = lang_list if lang_list else _lang_list
        self.latin_spelling = latin_spelling

    def set_lang_list(self, lang_list):
        self.lang_list = lang_list

    def all_lang_trans(self, word: str) -> dict[str, str]:
        """
        Translates the `word` into all languages

        :param lang_list: list[str]. Languages into which the word will be translated. By default, all supported languages
        :param word: the word to be translated
        :return: dict where the key is the name of the language, the value is the translation
        """
        out = dict()
        for lang in self.lang_list:
            my_translator = GoogleTranslator(source='auto', target=lang)
            result = my_translator.translate(text=word)
            result = unidecode(result) if (self.latin_spelling and not _is_latin(result)) else result
            out[lang] = result

        return out

    def transl_word_list(self, word_list):
        out = dict()

        for word in word_list:
            out[word] = self.all_lang_trans(word=word)

        return out

    def transl_from_file(self, path_to_file):
        return self.transl_word_list(_file_to_list(path_to_file))
