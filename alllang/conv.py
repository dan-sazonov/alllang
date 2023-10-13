import json
import os
from datetime import datetime
from itertools import product

import openpyxl
from openpyxl.styles import Font, Alignment


class _Excel:
    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data
        self._book = openpyxl.Workbook()
        self._sheet = self._book.active

        self._words = list(self.data.keys())
        self._langs = list(self.data[self._words[0]].keys())

    def _gen_words_keys(self):
        if len(self._words) <= 25:
            tmp = [chr(ltr) for ltr in range(66, (66 + len(self._words)))]
            return tmp[:len(self._words)]

        tmp = [chr(ltr) for ltr in range(66, 91)]  # letters from B to Z
        letters = [chr(ltr) for ltr in range(65, 91)]  # letters from A to Z
        factor = 1
        while True:
            if len(tmp) >= len(self._words):
                return tmp[:len(self._words)]
            factor += 1
            tmp += [''.join(tuples) for tuples in product(letters, repeat=factor)]

    def _stylize_title_cell(self, index):
        self._sheet[index].font = Font(b=True)
        self._sheet[index].alignment = Alignment(horizontal="center", vertical="center")

    def create_titles(self):
        cols_keys = self._gen_words_keys()

        for word_title_index in range(0, len(self._words)):
            cell_index = f'{cols_keys[word_title_index]}1'
            self._sheet[cell_index].value = self._words[word_title_index]
            self._stylize_title_cell(cell_index)

        for lang_title_index in range(0, len(self._langs)):
            cell_index = f'A{lang_title_index + 2}'
            self._sheet[cell_index].value = self._langs[lang_title_index]
            self._stylize_title_cell(cell_index)

    def add_data(self):
        col_index = 0  # column numbering starts from zero, rows from one
        cols_keys = self._gen_words_keys()

        for cols_data in self.data.values():
            row_index = 1
            for cell_data in cols_data.values():
                row_index += 1
                self._sheet[f'{cols_keys[col_index]}{row_index}'].value = cell_data
            col_index += 1

    def save_file(self):
        self._book.save(self.file_name)
        self._book.close()


def _get_file_name(path, ext):
    if (path is None) or (not os.path.exists(path)):
        path = './'
    file_name = f"{datetime.today().isoformat('-').replace(':', '-').split('.')[0]} .{ext}"

    res = os.path.join(path, file_name)
    return os.path.normpath(res)


def create_json(data, dest_path=None):
    file_name = _get_file_name(dest_path, 'json')

    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)


def create_xlsx(data, dest_path=None):
    file_name = _get_file_name(dest_path, 'xlsx')

    table = _Excel(data=data, file_name=file_name)
    table.create_titles()
    table.add_data()
    table.save_file()
