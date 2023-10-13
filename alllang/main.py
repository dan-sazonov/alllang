from unidecode import unidecode
from deep_translator import GoogleTranslator
import re


def _file_to_list(path: str) -> list[str]:
    """
    Converts a txt file with words on separate lines to a list of strings.
    Empty strings would be deleted

    :param path: absolute or relative path to the txt file
    :return: list of str
    """
    with open(path, 'r', encoding='utf-8') as f:
        file_content = f.read().split('\n')
        words = list(filter(None, file_content))  # remove empty strings

    return words


def _is_latin(string: str) -> bool:
    """
    Checks whether all characters from the received string are Latin or extended Latin characters

    :param string: the string being checked
    :return: True if there are no other symbols
    """
    pattern = r'^[a-zA-Z\u0080-\u024F]+$'
    return bool(re.match(pattern, string.replace("'", "")))  # remove the apostrophe beforehand


class Translator:
    """
    Translator is a namespace for all functions
    """

    def __init__(self, lang_list: list[str] = None, latin_spelling: bool = False):
        """
        Translator is a namespace for all functions

        :param lang_list: A list of languages to be translated into. By default - all supported languages from the list
        in the `supported_langs` field
        :param latin_spelling: If you want to get the spelling of all words in Latin in the output, set the value to
        True
        """
        self.supported_langs = list(GoogleTranslator().get_supported_languages())
        self.lang_list = lang_list if lang_list else self.supported_langs
        self.latin_spelling = latin_spelling

    def set_lang_list(self, lang_list: list[str]) -> None:
        """
        Set list of languages after Translator init

        :param lang_list: ['lang1', ..., 'lang-n']. Notation for languages is available in the `supported_langs` field
        :return:
        """
        self.lang_list = lang_list

    def _convert_spelling(self, word: str) -> str:
        """
        Transliterates the spelling of a word into Latin if the corresponding class parameter is specified

        :param word: the word for transliteration
        :return: transliterated or unmodified word
        """
        return unidecode(word) if (self.latin_spelling and not _is_latin(word)) else word

    def all_lang_trans(self, word: str) -> dict[str:dict[str:str]]:
        """
        Translates a word into all languages from the `lang_list` list

        :param word: the word that will be translated
        :return: dict {'word': {'lang': 'translation', ...}}
        """
        translated = dict()
        out = dict()

        for lang in self.lang_list:
            my_translator = GoogleTranslator(source='auto', target=lang)
            result = my_translator.translate(text=word)
            translated[lang] = self._convert_spelling(result)

        out[word] = translated
        return out

    def transl_word_list(self, word_list: list[str]) -> dict[str:dict[str:str]]:
        """
        Translates words from the got list into all languages from the `lang_list` list

        :param word_list: list ['word1', ..., 'word-n']. All of them will be translated
        :return: dict {'word1': {'lang': 'translation', ...}, ...}
        """
        out = dict()
        for word in word_list:
            out.update(self.all_lang_trans(word=word))
        return out

    def transl_from_file(self, path_to_file: str) -> dict[str:dict[str:str]]:
        """
        Parse a file with words on separate lines and translates all words into languages from the `lang_list` list

        :param path_to_file: absolute or relative path to the txt file
        :return: {'word1': {'lang': 'translation', ...}, ...}
        """
        return self.transl_word_list(_file_to_list(path_to_file))
