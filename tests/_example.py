import alllang

if __name__ == '__main__':
    # Simple usage:
    tr = alllang.Translator()
    translations = tr.transl_word_list(['hello', 'world'])
    # these words will be translated into all supported languages

    # The list of words can be obtained from a txt file, where each word must be written on a separate line:
    translations2 = tr.transl_from_file('words_list.txt')

    # List of supported languages:
    print(tr.supported_langs)

    # Translations of words can be transliterated into Latin. To initialize the class as follows:
    tr = alllang.Translator(latin_spelling=True)

    # The list of languages to translate can be changed after the initialization of the class:
    tr.set_lang_list(['afrikaans', 'albanian', 'amharic'])

    # You can write translations of all words in a xlsx or json file:
    alllang.create_json(translations)
    alllang.create_xlsx(translations, dest_path='/home/Documents')
    # you can specify the path where the file will be saved
