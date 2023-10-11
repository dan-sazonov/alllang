from alllang.cli import is_txt_file as _check_path

from deep_translator import GoogleTranslator

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


class Translator:
    def __init__(self):
        self.path_to_file = None
        self.lang_list = _lang_list

    def set_file(self, path):
        _check_path(path)
        self.path_to_file = path

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
            out[lang] = result

        return out

    def transl_from_file(self):
        word_list = _file_to_list(self.path_to_file)
        out = dict()

        for word in word_list:
            out[word] = self.all_lang_trans(word=word)

        return out
